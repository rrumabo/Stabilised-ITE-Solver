import numpy as np

def compute_l2_error(psi, psi_ref, dx):
    diff_squared = np.abs(psi - psi_ref)**2
    return np.sqrt(np.trapezoid(diff_squared, dx=dx))