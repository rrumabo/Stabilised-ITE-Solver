import numpy as np

def laplacian_spectral_3D(ψ, kx, ky, kz):
    ψ_k = np.fft.fftn(ψ)
    Δψ_k = -(kx**2 + ky**2 + kz**2) * ψ_k
    return np.fft.ifftn(Δψ_k)

def normalize(ψ, x):
    return ψ / np.sqrt(np.trapezoid(np.trapezoid(np.trapezoid(np.abs(ψ)**2, x), x), x))

def compute_norm(ψ, x):
    return np.trapezoid(np.trapezoid(np.trapezoid(np.abs(ψ)**2, x), x), x)
