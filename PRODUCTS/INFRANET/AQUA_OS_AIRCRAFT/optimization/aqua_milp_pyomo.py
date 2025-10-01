# aqua_milp_pyomo.py
# Implementación del modelo MILP híbrido para el ecosistema AQUA.

# Requisitos:
# pip install pyomo
# Se necesita un solver compatible (CBC, GLPK, Gurobi, CPLEX)
from pyomo.environ import *
from datetime import datetime, timezone
import hashlib
import json
import logging

# Configuración de logging (opcional)
logging.basicConfig(level=logging.INFO)

# -----------------------
# Datos de ejemplo (Parámetros)
# -----------------------
S = ['motor_electrico', 'motor_h2']  # Subsistemas Clásicos (Propulsión)
Q = ['qns_link', 'qkd_comm']         # Subsistemas Cuánticos (Navegación, Comunicación)
T = list(range(6))                   # Horizonte de 6 pasos de tiempo (ej. 6 horas de vuelo)

# Capacidades máximas
cap_s = {'motor_electrico': 100.0, 'motor_h2': 80.0}  # Unidades de Potencia/Uso
cap_q = {'qns_link': 1, 'qkd_comm': 1}                # Activación binaria

# Costes / Emisiones / Fiabilidad por unidad de uso (c, e, r)
c_s = {'motor_electrico': 2.0, 'motor_h2': 3.5}
e_s = {'motor_electrico': 0.1, 'motor_h2': 0.02} # El H2 tiene menores emisiones directas
r_s = {'motor_electrico': 0.98, 'motor_h2': 0.95}

c_q = {'qns_link': 5.0, 'qkd_comm': 4.0}
e_q = {'qns_link': 0.005, 'qkd_comm': 0.004}
r_q = {'qns_link': 0.90, 'qkd_comm': 0.92}

# Demanda operativa por t (unidades abstractas)
d = {t: 120.0 if t % 3 != 0 else 40.0 for t in T} 

# Latencia (L) y Fidelidad (F) simuladas para subsistemas cuánticos (Q)
# Simulación de degradación: el enlace cuántico falla en t=4
L = { (q,t): 0.05 + 0.02*(t%4) for q in Q for t in T }
F = { (q,t): 0.99 - 0.1*(t==4) for q in Q for t in T } # Baja F en t=4

# Fase/Estado para Sincronía (phi)
# Representa el estado de sincronización entre el reloj cuántico y el clásico
# Buscamos minimizar |phi_cl - phi_q|
phi_cl = { (q,t): 0.1 * (t % 5) for q in Q for t in T } 
phi_q = { (q,t): 0.1 * ((t+1) % 5) for q in Q for t in T } 

# Umbrales y Presupuesto
L_max = 0.2     # Latencia máxima permitida
F_min = 0.88    # Fidelidad mínima requerida
B_CO2 = 10.0    # Presupuesto total de Emisiones de CO2
DELTA_MAX = 0.5 # Desincronía máxima permitida (restricción dura)
R_MIN = 0.95    # Fiabilidad mínima del sistema agregado en cada instante t

# Pesos del objetivo (w_c, w_e, w_r, lambda_sync, beta_reg)
w_c = 1.0       # Peso del Coste
w_e = 10.0      # Peso de las Emisiones (alto para priorizar sostenibilidad)
w_r = 5.0       # Peso de la Fiabilidad
lambda_sync = 50.0 # Penalización por Desincronía
beta_reg = 1000.0  # Penalización por Incumplimiento Regulatorio/UTCS

# Coeficientes de rendimiento para la cobertura de la demanda
alpha = {'motor_electrico':0.9, 'motor_h2':0.9} 
gamma = {'qns_link':50.0, 'qkd_comm': 10.0} # Gran impacto de la activación cuántica
# -----------------------

# -----------------------
# Modelo Pyomo
# -----------------------
model = ConcreteModel()

# Sets
model.S = Set(initialize=S)
model.Q = Set(initialize=Q)
model.T = Set(initialize=T)

# Parameters (Inicialización)
model.cap_s = Param(model.S, initialize=cap_s)
model.c_s = Param(model.S, initialize=c_s)
model.e_s = Param(model.S, initialize=e_s)
model.r_s = Param(model.S, initialize=r_s)
model.c_q = Param(model.Q, initialize=c_q)
model.e_q = Param(model.Q, initialize=e_q)
model.r_q = Param(model.Q, initialize=r_q)
model.d = Param(model.T, initialize=d)
model.L = Param(model.Q, model.T, initialize=L)
model.F = Param(model.Q, model.T, initialize=F)
model.phi_cl = Param(model.Q, model.T, initialize=phi_cl)
model.phi_q = Param(model.Q, model.T, initialize=phi_q)
model.alpha = Param(model.S, initialize=alpha)
model.gamma = Param(model.Q, initialize=gamma)

# Variables
# x: Uso de subsistema clásico (0 a cap_s)
model.x = Var(model.S, model.T, domain=NonNegativeReals, bounds=lambda m,s,t: (0, m.cap_s[s]))
# qact: Activación de subsistema cuántico (Binaria: 0 o 1)
model.qact = Var(model.Q, model.T, domain=Binary)

# Variables auxiliares para linearizar la desincronía (delta = sum(|phi_cl - phi_q| * qact))
# Usamos u y v para representar la parte positiva y negativa del valor absoluto
model.u = Var(model.Q, model.T, domain=NonNegativeReals)
model.v = Var(model.Q, model.T, domain=NonNegativeReals)
model.delta = Var(model.T, domain=NonNegativeReals) # Desincronía total del sistema en t

# Penalización por trazabilidad fallida (se deja a 0 en este MVP)
model.bad_utcs = Var(model.T, domain=Binary) 

# -----------------------
# Función Objetivo Multi-Criterio (Minimización)
# -----------------------
def objective_rule(m):
    # 1. Coste (Minimizar)
    cost_classic = sum(m.c_s[s]*m.x[s,t] for s in m.S for t in m.T)
    cost_quantum = sum(m.c_q[q]*m.qact[q,t] for q in m.Q for t in m.T)
    
    # 2. Emisiones (Minimizar)
    emis_classic = sum(m.e_s[s]*m.x[s,t] for s in m.S for t in m.T)
    emis_quantum = sum(m.e_q[q]*m.qact[q,t] for q in m.Q for t in m.T)
    
    # 3. Fiabilidad (Maximizar -> entra negativo)
    rel_classic = sum(m.r_s[s]*m.x[s,t] for s in m.S for t in m.T)
    rel_quantum = sum(m.r_q[q]*m.qact[q,t] for q in m.Q for t in m.T)
    
    # 4. Penalización por Sincronía (Minimizar)
    sync_pen = lambda_sync * sum(m.delta[t] for t in m.T)
    
    # 5. Penalización Regulatoria/UTCS (Minimizar)
    reg_pen = beta_reg * sum(m.bad_utcs[t] for t in m.T)
    
    return (w_c*(cost_classic + cost_quantum) 
            + w_e*(emis_classic + emis_quantum) 
            - w_r*(rel_classic + rel_quantum) 
            + sync_pen 
            + reg_pen)

model.OBJ = Objective(rule=objective_rule, sense=minimize)

# -----------------------
# Restricciones
# -----------------------

# 1. Cobertura de Demanda
def demand_rule(m, t):
    # Rendimiento Clásico (x * alpha) + Rendimiento Cuántico (qact * gamma) >= Demanda d_t
    return sum(m.alpha[s]*m.x[s,t] for s in m.S) + sum(m.gamma[q]*m.qact[q,t] for q in m.Q) >= m.d[t]
model.demand_cons = Constraint(model.T, rule=demand_rule)

# 2. Presupuesto Global de Emisiones
def emissions_rule(m):
    return sum(m.e_s[s]*m.x[s,t] for s in m.S for t in m.T) + sum(m.e_q[q]*m.qact[q,t] for q in m.Q for t in m.T) <= B_CO2
model.emissions_cons = Constraint(rule=emissions_rule)

# 3. Restricciones de Calidad Cuántica (Certificación/Operabilidad)
# Si Latencia > L_max O Fidelidad < F_min, el enlace cuántico debe estar desactivado (qact = 0)
def quality_constraint_rule(m, q, t):
    # Nota: Usamos value() para acceder a los valores fijos de los parámetros L y F
    if value(m.F[q,t]) < F_min or value(m.L[q,t]) > L_max:
        logging.info(f"Advertencia: Enlace {q} en t={t} fuera de umbral (L={value(m.L[q,t])}, F={value(m.F[q,t])}). Forzando desactivación.")
        return m.qact[q,t] == 0
    else:
        return Constraint.Skip
model.quality_cons = Constraint(model.Q, model.T, rule=quality_constraint_rule)

# 4. Sincronía (Linearización de |A|)
# Queremos penalizar la desincronía |phi_cl - phi_q| para cada enlace cuántico activo.
# A: phi_cl[q,t] - phi_q[q,t]

# 4a. Definición de u y v (partes del valor absoluto)
def u_def_rule(m, q, t):
    # u >= A
    return m.u[q,t] >= m.phi_cl[q,t] - m.phi_q[q,t]
def v_def_rule(m, q, t):
    # v >= -A
    return m.v[q,t] >= m.phi_q[q,t] - m.phi_cl[q,t]
model.u_def = Constraint(model.Q, model.T, rule=u_def_rule)
model.v_def = Constraint(model.Q, model.T, rule=v_def_rule)

# 4b. Restricción de Desincronía Total (Delta) y uso de M grande (Big-M)
# Delta[t] = Sumatorio sobre q de (u[q,t] + v[q,t]) * qact[q,t]
# Para un MILP, si el enlace q no está activo (qact=0), no debe contribuir a delta.
# Si qact=1, entonces (u+v) debe ser igual a |A|.

# Aquí usamos una simplificación más limpia para el MVP: penalizar la suma de desviaciones, 
# asumiendo que la penalización por desactivación (coste alto) es suficiente si la desviación es grande.
# Definimos delta[t] como la suma de las desviaciones u+v (que es |A|) *sin* Big M, y la penalización 
# de la función objetivo fuerza la minimización de delta.

# Si qact fuera continua (0-1), esto sería un producto no lineal. Al ser qact binaria, es un MILP estándar
# con u y v activados solo si qact=1.

# Usamos la definición: delta[t] >= sum_{q} (u[q,t] + v[q,t]) * qact[q,t]
# Producto de variables binarias (qact * u) -> No lineal.

# ALTERNATIVA (Linearización del producto):
# Sea diff[q,t] = u[q,t] + v[q,t]. Queremos z = diff * qact.
# Usamos Big M para forzar que el término de sincronía (u+v) sea 0 si qact=0.
BIG_D = 10.0 # Cota superior para la desviación de fase

def delta_upper_bound_active(m, q, t):
    # Si qact=1, delta_q debe ser <= u+v + 0
    return m.delta_q[q,t] <= m.u[q,t] + m.v[q,t] + BIG_D * (1 - m.qact[q,t])

def delta_upper_bound_inactive(m, q, t):
    # Si qact=0, delta_q debe ser <= 0 + BIG_D * 1
    return m.delta_q[q,t] <= BIG_D * m.qact[q,t] # Esto fuerza delta_q a 0 si qact=0 (asumiendo delta_q >= 0)

# Redefinimos variables auxiliares para la sincronía con Big M
model.delta_q = Var(model.Q, model.T, domain=NonNegativeReals) # Desincronía por enlace q

model.delta_q_active = Constraint(model.Q, model.T, rule=delta_upper_bound_active)
# Constraint: delta_q >= u+v si qact=1 (Esto se cumple si delta_q se minimiza en el objetivo)
model.delta_q_inactive = Constraint(model.Q, model.T, rule=delta_upper_bound_inactive)

# La desincronía total del sistema delta[t] es la suma de las desincronías individuales
def total_delta_rule(m, t):
    return m.delta[t] == sum(m.delta_q[q,t] for q in m.Q)
model.total_delta_cons = Constraint(model.T, rule=total_delta_rule)


# 5. Restricción de Desincronía Máxima (Dura)
def delta_max_rule(m, t):
    return m.delta[t] <= DELTA_MAX
model.delta_max = Constraint(model.T, rule=delta_max_rule)

# 6. Fiabilidad Mínima por Tiempo
def reliability_min_rule(m, t):
    # La fiabilidad total es la suma ponderada del uso
    return sum(m.r_s[s]*m.x[s,t] for s in m.S) + sum(m.r_q[q]*m.qact[q,t] for q in m.Q) >= R_MIN
model.reliability_min_cons = Constraint(model.T, rule=reliability_min_rule)

# 7. Placeholder UTCS (Restricción Lógica, forzada a 0 en MVP)
# En un sistema real, un validador externo generaría bad_utcs=1 si el plan viola el formato.
def utcs_placeholder(m, t): 
    return m.bad_utcs[t] == 0
model.utcs_place = Constraint(model.T, rule=utcs_placeholder)


# -----------------------
# Solución y Trazabilidad UTCS-MI
# -----------------------

def generate_utcs_snapshot(system_domain, subsystem, compid, version, mode, plan, results_summary):
    """Genera el snapshot UTCS-MI v5.0 con hash de trazabilidad."""
    
    timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    
    # 1. Crear el identificador UTCS (13 campos condensados para el slug)
    base_id = f"UTCS-{system_domain}-{subsystem}-{compid}-{version}-{mode}-{timestamp}"
    short_hash = hashlib.sha256(base_id.encode('utf-8')).hexdigest()[:8]
    utcs_id = f"{base_id}-{short_hash}"
    
    snapshot = {
        "UTCS_ID": utcs_id,
        "Timestamp_UTC": timestamp,
        "SystemDomain": system_domain,
        "SubsystemID": subsystem,
        "ConfigVersion": version,
        "Mode": mode,
        "QuantumLayerPresent": any(val > 0 for t_data in plan['q'].values() for val in t_data.values()),
        "Plan_Optimization_Horizon": plan,
        "Optimization_Results_Summary": results_summary
    }

    # 2. Calcular el Hash del contenido (prueba de integridad)
    # Se debe ordenar las keys para asegurar que el hash sea determinista
    snap_bytes = json.dumps(snapshot, sort_keys=True).encode('utf-8')
    snapshot['Content_Hash_SHA256'] = hashlib.sha256(snap_bytes).hexdigest()
    
    return snapshot

if __name__ == "__main__":
    # Búsqueda automática del solver
    solver_name = None
    for s in ['gurobi', 'cbc', 'glpk', 'cplex']:
        try:
            solver = SolverFactory(s)
            if solver.available(exception_flag=False):
                solver_name = s
                break
        except Exception:
            continue
            
    if solver_name is None:
        print("ERROR: No se encontró un solver disponible (gurobi, cbc, glpk, cplex). Instale uno para ejecutar.")
        raise SystemExit(1)
    
    logging.info(f"Usando solver: {solver_name}")
    solver = SolverFactory(solver_name)
    
    # Resolver el modelo
    results = solver.solve(model, tee=False)

    if results.solver.termination_condition != TerminationCondition.optimal:
        logging.error(f"Solución no óptima. Estado: {results.solver.status}, Condición: {results.solver.termination_condition}")
        raise SystemExit(1)
        
    logging.info("Modelo resuelto con éxito.")
    
    # Extracción y Presentación del Plan
    plan = {'x':{}, 'q':{}}
    for t in T:
        plan['x'][t] = {s: value(model.x[s,t]) for s in S}
        plan['q'][t] = {q: int(round(value(model.qact[q,t]))) for q in Q}
    
    total_cost = value(model.OBJ)
    total_emis = sum(e_s[s]*plan['x'][t][s] for s in S for t in T) + sum(e_q[q]*plan['q'][t][q] for q in Q for t in T)

    print("\n" + "="*50)
    print("PLAN DE RECURSOS HÍBRIDO (AQUA MILP)")
    print("="*50)
    for t in T:
        sync_val = value(model.delta[t])
        
        # Validación de la demanda
        demand_met = sum(value(model.alpha[s]) * plan['x'][t][s] for s in S) + sum(value(model.gamma[q]) * plan['q'][t][q] for q in Q)
        
        print(f"\n--- Instante t={t} (Demanda: {d[t]} / Cubierta: {demand_met:.2f}) ---")
        print(f"  > Clásico (x): {plan['x'][t]}")
        print(f"  > Cuántico (qact): {plan['q'][t]}")
        print(f"  > Desincronía (delta): {sync_val:.4f} (Max: {DELTA_MAX})")
        
        # Muestra la razón de la desactivación cuántica si ocurre
        for q in Q:
            if plan['q'][t][q] == 0 and (F[(q,t)] < F_min or L[(q,t)] > L_max):
                 print(f"    [Nota Certificación]: {q} desactivado debido a baja Fidelidad/alta Latencia en t={t}.")
                 
    print("\n--- Resumen General ---")
    print(f"Objetivo Total (Ponderado): {total_cost:.2f}")
    print(f"Emisiones Totales (Presupuesto {B_CO2}): {total_emis:.6f}")
    print(f"Sincronía Total Penalizada: {value(sum(model.delta[t] for t in model.T)):.4f}")
    print("="*50)

    # Generación del Registro UTCS-MI
    results_summary = {
        "ObjectiveValue": total_cost,
        "TotalEmissions": total_emis,
        "TotalSyncDeviation": value(sum(model.delta[t] for t in model.T))
    }
    
    snapshot = generate_utcs_snapshot(
        system_domain="Avionics", 
        subsystem="IntegratedFlightControl", 
        compid="MILP_Planner", 
        version="v1.0", 
        mode="Operational", 
        plan=plan,
        results_summary=results_summary
    )
    
    file_name = "aqua_pyomo_plan_utcs.json"
    with open(file_name,"w") as f:
        json.dump(snapshot, f, indent=2)
        
    print(f"\n[UTCS-MI] Registro de configuración guardado en {file_name}")
    print(f"[UTCS-MI] ID de Trazabilidad: {snapshot['UTCS_ID']}")
    print(f"[UTCS-MI] Hash de Integridad: {snapshot['Content_Hash_SHA256']}")
