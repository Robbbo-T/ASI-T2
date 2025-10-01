# aqua_milp_model.py
# Estructura del modelo MILP híbrido AQUA (sin datos).
# Los datos se cargarán desde aqua_milp.dat o un archivo similar.

from pyomo.environ import *
import logging

def build_model():
    model = ConcreteModel()

    # ========================
    # Sets (Leídos del .dat)
    # ========================
    model.S = Set() # Subsistemas Clásicos
    model.Q = Set() # Subsistemas Cuánticos
    model.T = Set() # Horizonte de Tiempo

    # ========================
    # Parámetros (Leídos del .dat)
    # ========================
    model.cap_s = Param(model.S)
    model.c_s = Param(model.S)
    model.e_s = Param(model.S)
    model.r_s = Param(model.S)
    model.c_q = Param(model.Q)
    model.e_q = Param(model.Q)
    model.r_q = Param(model.Q)
    model.d = Param(model.T)
    model.L = Param(model.Q, model.T)
    model.F = Param(model.Q, model.T)
    model.phi_cl = Param(model.Q, model.T)
    model.phi_q = Param(model.Q, model.T)
    model.alpha = Param(model.S)
    model.gamma = Param(model.Q)

    # Parámetros de umbrales y pesos (Leídos del .dat)
    model.L_max = Param()
    model.F_min = Param()
    model.B_CO2 = Param()
    model.DELTA_MAX = Param()
    model.R_MIN = Param()
    model.w_c = Param()
    model.w_e = Param()
    model.w_r = Param()
    model.lambda_sync = Param()
    model.beta_reg = Param()
    model.BIG_D = Param()

    # ========================
    # Variables
    # ========================
    def x_bounds(m, s, t):
        return (0, m.cap_s[s])
    model.x = Var(model.S, model.T, domain=NonNegativeReals, bounds=x_bounds)
    model.qact = Var(model.Q, model.T, domain=Binary)
    
    # Variables auxiliares para sincronía
    model.u = Var(model.Q, model.T, domain=NonNegativeReals)
    model.v = Var(model.Q, model.T, domain=NonNegativeReals)
    model.delta = Var(model.T, domain=NonNegativeReals)
    model.delta_q = Var(model.Q, model.T, domain=NonNegativeReals)
    model.bad_utcs = Var(model.T, domain=Binary)

    # ========================
    # Función Objetivo Multi-Criterio
    # ========================
    def objective_rule(m):
        cost_classic = sum(m.c_s[s]*m.x[s,t] for s in m.S for t in m.T)
        cost_quantum = sum(m.c_q[q]*m.qact[q,t] for q in m.Q for t in m.T)
        emis_classic = sum(m.e_s[s]*m.x[s,t] for s in m.S for t in m.T)
        emis_quantum = sum(m.e_q[q]*m.qact[q,t] for q in m.Q for t in m.T)
        rel_classic = sum(m.r_s[s]*m.x[s,t] for s in m.S for t in m.T)
        rel_quantum = sum(m.r_q[q]*m.qact[q,t] for q in m.Q for t in m.T)
        
        sync_pen = m.lambda_sync * sum(m.delta[t] for t in m.T)
        reg_pen = m.beta_reg * sum(m.bad_utcs[t] for t in m.T)
        
        return (m.w_c*(cost_classic + cost_quantum) 
                + m.w_e*(emis_classic + emis_quantum) 
                - m.w_r*(rel_classic + rel_quantum) 
                + sync_pen 
                + reg_pen)

    model.OBJ = Objective(rule=objective_rule, sense=minimize)

    # ========================
    # Restricciones
    # ========================

    # 1. Cobertura de Demanda
    def demand_rule(m, t):
        return sum(m.alpha[s]*m.x[s,t] for s in m.S) + sum(m.gamma[q]*m.qact[q,t] for q in m.Q) >= m.d[t]
    model.demand_cons = Constraint(model.T, rule=demand_rule)

    # 2. Presupuesto Global de Emisiones
    def emissions_rule(m):
        return sum(m.e_s[s]*m.x[s,t] for s in m.S for t in m.T) + sum(m.e_q[q]*m.qact[q,t] for q in m.Q for t in m.T) <= m.B_CO2
    model.emissions_cons = Constraint(rule=emissions_rule)

    # 3. Restricciones de Calidad Cuántica (Fidelidad/Latencia)
    def quality_constraint_rule(m, q, t):
        # Si F < F_min o L > L_max, forzar desactivación qact = 0
        if m.F[q,t] < m.F_min or m.L[q,t] > m.L_max:
            return m.qact[q,t] == 0
        else:
            return Constraint.Skip
    model.quality_cons = Constraint(model.Q, model.T, rule=quality_constraint_rule)

    # 4. Sincronía: Linearización de |phi_cl - phi_q| (Valor absoluto)
    def u_def_rule(m, q, t):
        return m.u[q,t] >= m.phi_cl[q,t] - m.phi_q[q,t]
    def v_def_rule(m, q, t):
        return m.v[q,t] >= m.phi_q[q,t] - m.phi_cl[q,t]
    model.u_def = Constraint(model.Q, model.T, rule=u_def_rule)
    model.v_def = Constraint(model.Q, model.T, rule=v_def_rule)

    # 5. Sincronía: Linearización del producto (delta_q = |A| * qact)
    def delta_upper_bound_active(m, q, t):
        # delta_q <= |A| + BIG_D * (1 - qact)
        return m.delta_q[q,t] <= m.u[q,t] + m.v[q,t] + m.BIG_D * (1 - m.qact[q,t])
    def delta_upper_bound_inactive(m, q, t):
        # delta_q <= BIG_D * qact (Fuerza delta_q a 0 si qact=0)
        return m.delta_q[q,t] <= m.BIG_D * m.qact[q,t] 
    
    model.delta_q_active = Constraint(model.Q, model.T, rule=delta_upper_bound_active)
    model.delta_q_inactive = Constraint(model.Q, model.T, rule=delta_upper_bound_inactive)

    # 6. Desincronía Total
    def total_delta_rule(m, t):
        return m.delta[t] == sum(m.delta_q[q,t] for q in m.Q)
    model.total_delta_cons = Constraint(model.T, rule=total_delta_rule)

    # 7. Restricción de Desincronía Máxima (Dura)
    def delta_max_rule(m, t):
        return m.delta[t] <= m.DELTA_MAX
    model.delta_max = Constraint(model.T, rule=delta_max_rule)

    # 8. Fiabilidad Mínima por Tiempo
    def reliability_min_rule(m, t):
        return sum(m.r_s[s]*m.x[s,t] for s in m.S) + sum(m.r_q[q]*m.qact[q,t] for q in m.Q) >= m.R_MIN
    model.reliability_min_cons = Constraint(model.T, rule=reliability_min_rule)

    # 9. Placeholder UTCS (para verificación externa, forzado a 0)
    def utcs_placeholder(m, t): 
        return m.bad_utcs[t] == 0
    model.utcs_place = Constraint(model.T, rule=utcs_placeholder)
    
    return model

if __name__ == "__main__":
    print("Este archivo contiene la estructura del modelo. Use 'aqua_milp_solve.py' para ejecutarlo.")
