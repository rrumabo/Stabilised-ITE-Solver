from muITE3D import laplacian_spectral_3D, normalize, compute_norm
import numpy as np
import matplotlib.pyplot as plt

def run_mu_ITE_3D(N=64, L=10.0, dτ=0.001, T=1.0, α=1.0, g=1.0, μ_max=2.0, save_slices=False):
    x = np.linspace(-L/2, L/2, N, endpoint=False)
    dx = x[1] - x[0]
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    k = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')

    ψ = np.exp(-(X**2 + Y**2 + Z**2)).astype(np.complex128)
    ψ = normalize(ψ, x)

    steps = int(T / dτ)
    μ_log = []
    norm_prev = compute_norm(ψ, x)
    μ = 0.0

    for step in range(steps):
        Δψ = laplacian_spectral_3D(ψ, kx, ky, kz)
        nonlinear = g * np.abs(ψ)**2 * ψ
        RHS = -Δψ + nonlinear + 1j * μ * ψ

        ψ += dτ * RHS
        ψ = normalize(ψ, x)

        norm_curr = compute_norm(ψ, x)
        dnorm = (norm_curr - norm_prev) / dτ
        μ = α * dnorm / (norm_curr + 1e-12)
        μ = np.clip(μ, -μ_max, μ_max)

        μ_log.append(μ)
        norm_prev = norm_curr

    print(f"Final norm = {norm_curr:.6f}")
    print(f"Final μ    = {μ:.6e}")

    if save_slices:
        slice_xy = np.abs(ψ[N//2, :, :])**2
        proj_xy = np.sum(np.abs(ψ)**2, axis=2)
        return ψ, np.array(μ_log), norm_curr, slice_xy, proj_xy

    return ψ, np.array(μ_log), norm_curr
