import numpy as np
import matplotlib.pyplot as plt
import os
import sys

os.makedirs("output", exist_ok=True)
sys.path.append(os.path.abspath("src"))

from solver import run_simulation
from laplacian import make_laplacian_1d
from hamiltonians import make_nlse_hamiltonian
from initial_conditions import single_soliton_1d
from l2_error import compute_l2_error

grid_size = 128
L = 10.0
g = 1.5
alphas = [0.1, 0.3, 0.5, 0.7, 1.0]
dt = 0.001
steps = 2000

dx = L / grid_size
x = np.linspace(-L / 2, L / 2, grid_size, endpoint=False)
np.save("output/grid_x.npy", x)

plt.figure(figsize=(10, 6))

for alpha in alphas:
    psi0 = single_soliton_1d(grid_size=grid_size, L=L)
    psi_ref = psi0.copy()
    
    laplacian = make_laplacian_1d(grid_size=grid_size, L=L)
    hamiltonian = make_nlse_hamiltonian(laplacian, g=g)
    results = run_simulation(psi0, hamiltonian, alpha, dt, steps, dx)
    
    psi_final = results["psi_final"]
    np.save(f"output/psi_final_alpha_{alpha}.npy", psi_final)

    errors = [
        compute_l2_error(psi_t, psi_ref, dx)
        for psi_t in results["psi_history"]
    ]

    plt.plot(errors, label=f"α={alpha}")

plt.title("L² Error Over Time for Different α")
plt.xlabel("Time Step")
plt.ylabel("L² Error")
plt.legend()
plt.tight_layout()
plt.show()