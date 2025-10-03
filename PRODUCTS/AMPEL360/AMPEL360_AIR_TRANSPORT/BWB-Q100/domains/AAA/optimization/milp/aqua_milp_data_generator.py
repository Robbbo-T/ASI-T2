# aqua_milp_data_generator.py
# Genera el archivo aqua_milp.dat a partir de los datos de ejemplo originales.

import json

# ========================
# Datos de ejemplo (copia exacta del script anterior)
# ========================
S = ['motor_electrico', 'motor_h2'] 
Q = ['qns_link', 'qkd_comm']         
T_list = list(range(6)) 
T_str = [str(t) for t in T_list]

cap_s = {'motor_electrico': 100.0, 'motor_h2': 80.0}
cap_q = {'qns_link': 1, 'qkd_comm': 1}

c_s = {'motor_electrico': 2.0, 'motor_h2': 3.5}
e_s = {'motor_electrico': 0.1, 'motor_h2': 0.02}
r_s = {'motor_electrico': 0.98, 'motor_h2': 0.95}

c_q = {'qns_link': 5.0, 'qkd_comm': 4.0}
e_q = {'qns_link': 0.005, 'qkd_comm': 0.004}
r_q = {'qns_link': 0.90, 'qkd_comm': 0.92}

d = {t: 120.0 if t % 3 != 0 else 40.0 for t in T_list} 

L = { (q,t): 0.05 + 0.02*(t%4) for q in Q for t in T_list }
F = { (q,t): 0.99 - 0.1*(t==4) for q in Q for t in T_list }

phi_cl = { (q,t): 0.1 * (t % 5) for q in Q for t in T_list }
phi_q = { (q,t): 0.1 * ((t+1) % 5) for q in Q for t in T_list }

alpha = {'motor_electrico':0.9, 'motor_h2':0.9} 
gamma = {'qns_link':50.0, 'qkd_comm': 10.0}

# Umbrales y Pesos
params_scalars = {
    'L_max': 0.2,
    'F_min': 0.88,
    'B_CO2': 10.0,
    'DELTA_MAX': 0.5,
    'R_MIN': 0.95,
    'w_c': 1.0,
    'w_e': 10.0,
    'w_r': 5.0,
    'lambda_sync': 50.0,
    'beta_reg': 1000.0,
    'BIG_D': 10.0 # Cota M para el Big M en sincronía
}

def write_dat_file(filename="aqua_milp.dat"):
    with open(filename, 'w') as f:
        f.write("param L_max := {};\n".format(params_scalars['L_max']))
        f.write("param F_min := {};\n".format(params_scalars['F_min']))
        f.write("param B_CO2 := {};\n".format(params_scalars['B_CO2']))
        f.write("param DELTA_MAX := {};\n".format(params_scalars['DELTA_MAX']))
        f.write("param R_MIN := {};\n".format(params_scalars['R_MIN']))
        f.write("param w_c := {};\n".format(params_scalars['w_c']))
        f.write("param w_e := {};\n".format(params_scalars['w_e']))
        f.write("param w_r := {};\n".format(params_scalars['w_r']))
        f.write("param lambda_sync := {};\n".format(params_scalars['lambda_sync']))
        f.write("param beta_reg := {};\n".format(params_scalars['beta_reg']))
        f.write("param BIG_D := {};\n".format(params_scalars['BIG_D']))
        
        f.write("\nset S := {};\n".format(' '.join(S)))
        f.write("set Q := {};\n".format(' '.join(Q)))
        f.write("set T := {};\n".format(' '.join(T_str)))
        
        # Parámetros indexados por un solo Set
        def write_param_one_index(param_name, data):
            f.write(f"\nparam {param_name} :=\n")
            for key, val in data.items():
                f.write(f"  {key} {val}\n")
            f.write(";\n")
        
        write_param_one_index('cap_s', cap_s)
        write_param_one_index('c_s', c_s)
        write_param_one_index('e_s', e_s)
        write_param_one_index('r_s', r_s)
        write_param_one_index('c_q', c_q)
        write_param_one_index('e_q', e_q)
        write_param_one_index('r_q', r_q)
        write_param_one_index('alpha', alpha)
        write_param_one_index('gamma', gamma)
        
        # Demanda (indexada por T)
        f.write("\nparam d :=\n")
        for t in T_list:
            f.write(f"  {t} {d[t]}\n")
        f.write(";\n")

        # Parámetros indexados por Q y T
        def write_param_two_indices(param_name, data):
            f.write(f"\nparam {param_name} :=\n")
            for (q, t), val in data.items():
                f.write(f"  {q} {t} {val}\n")
            f.write(";\n")

        write_param_two_indices('L', L)
        write_param_two_indices('F', F)
        write_param_two_indices('phi_cl', phi_cl)
        write_param_two_indices('phi_q', phi_q)

    print(f"Archivo de datos {filename} generado correctamente.")

if __name__ == "__main__":
    write_dat_file()
