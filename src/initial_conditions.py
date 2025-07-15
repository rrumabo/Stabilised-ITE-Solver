import numpy as np
def single_soliton_1d(grid_size=128, L=10.0):
    x = np.linspace(-L / 2, L / 2, grid_size, endpoint=False)
    psi0 = 1 / np.cosh(x)
    dx = L / grid_size
    norm = np.trapz(np.abs(psi0)**2, dx=dx)
    psi0 = psi0 / np.sqrt(norm)
    return psi0.astype(np.complex128)