# aqua_milp_solve.py
# Carga el modelo y los datos, y lo resuelve.

from pyomo.environ import *
import logging
from datetime import datetime
import hashlib
import json
import aqua_milp_model # Importa la estructura del modelo

# Configuración de logging
logging.basicConfig(level=logging.INFO)

def solve_aqua_milp(model_file, data_file):
    
    # 1. Cargar el modelo
    model = aqua_milp_model.build_model()
    
    # 2. Cargar los datos desde el archivo .dat
    try:
        instance = model.create_instance(data_file)
    except Exception as e:
        logging.error(f"Error al cargar el archivo de datos {data_file}: {e}")
        return None, None

    # 3. Buscar y usar un solver
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
        logging.error("No se encontró un solver disponible. Instale gurobi, cbc o glpk.")
        return None, None
    
    logging.info(f"Usando solver: {solver_name}")
    solver = SolverFactory(solver_name)
    
    # 4. Resolver
    results = solver.solve(instance, tee=False)

    if results.solver.termination_condition != TerminationCondition.optimal:
        logging.error(f"Solución no óptima. Condición: {results.solver.termination_condition}")
        return None, None
        
    # 5. Extracción y Trazabilidad (UTCS-MI)
    plan = {'x':{}, 'q':{}}
    T_list = [int(t) for t in instance.T]
    S_list = list(instance.S)
    Q_list = list(instance.Q)
    
    for t in T_list:
        plan['x'][t] = {s: value(instance.x[s,t]) for s in S_list}
        plan['q'][t] = {q: int(round(value(instance.qact[q,t]))) for q in Q_list}

    results_summary = {
        "ObjectiveValue": value(instance.OBJ),
        "TotalEmissions": sum(instance.e_s[s].value*plan['x'][t][s] for s in S_list for t in T_list) + sum(instance.e_q[q].value*plan['q'][t][q] for q in Q_list for t in T_list),
        "TotalSyncDeviation": value(sum(instance.delta[t] for t in instance.T))
    }
    
    # Función simplificada de generación UTCS (simulación de trazabilidad)
    def generate_utcs_snapshot(plan, summary):
        timestamp = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
        base_id = f"UTCS-Avionics-IntegratedControl-MILP_Planner-v1.0-Operational-{timestamp}"
        short_hash = hashlib.sha256(base_id.encode('utf-8')).hexdigest()[:8]
        utcs_id = f"{base_id}-{short_hash}"
        
        snapshot = {
            "UTCS_ID": utcs_id,
            "Timestamp_UTC": timestamp,
            "Plan_Optimization_Horizon": plan,
            "Optimization_Results_Summary": summary
        }
        snap_bytes = json.dumps(snapshot, sort_keys=True).encode('utf-8')
        snapshot['Content_Hash_SHA256'] = hashlib.sha256(snap_bytes).hexdigest()
        return snapshot

    snapshot = generate_utcs_snapshot(plan, results_summary)
    
    print("\n--- Resultados ---")
    print(f"Objetivo: {results_summary['ObjectiveValue']:.2f}")
    print(f"Emisiones Totales: {results_summary['TotalEmissions']:.6f}")
    print(f"UTCS ID: {snapshot['UTCS_ID']}")
    print(f"Hash de Integridad: {snapshot['Content_Hash_SHA256']}")

    # Guardar el snapshot
    file_name = "aqua_pyomo_solve_utcs.json"
    with open(file_name,"w") as f:
        json.dump(snapshot, f, indent=2)
    
    return instance, snapshot

if __name__ == "__main__":
    solve_aqua_milp("aqua_milp_model.py", "aqua_milp.dat")
