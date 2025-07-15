import numpy as np

def make_nlse_hamiltonian(laplacian_fn, g=1.5):
    def hamiltonian(psi):
        nonlinear = g * np.abs(psi)**2 * psi
        kinetic = -laplacian_fn(psi)
        return kinetic + nonlinear
    return hamiltonian