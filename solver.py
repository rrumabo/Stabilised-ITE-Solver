import numpy as np

def run_mu_solver(N=512, T=2.0, dτ=0.001, g=1.0, α=1.0, damping=1e-4, T_ramp=0.1, mu_max=2.0):
    x = np.linspace(-10, 10, N, endpoint=False)
    dx = x[1] - x[0]
    steps = int(T / dτ)
    k = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    eps = 1e-12

    def normalize(u): return u / np.sqrt(np.trapezoid(np.abs(u)**2, x) + eps)
    def lap(u): return np.fft.ifft(-k**2 * np.fft.fft(u))
    def H(u, g): return -lap(u) + g * np.abs(u)**2 * u
    def rhs(u, μ, g): return -H(u, g) + 1j * μ * u

    ψ = normalize(1.0 / np.cosh(x)).astype(np.complex128)
    norms, μ_log = [], []
    norm_prev, μ_prev = np.trapezoid(np.abs(ψ)**2, x), 0.0

    for n in range(steps):
        τ = n * dτ
        g_eff = g * min(τ / T_ramp, 1.0)

        k1 = dτ * rhs(ψ, μ_prev, g_eff)
        ψ1 = normalize(ψ + 0.5 * k1)

        k2 = dτ * rhs(ψ1, μ_prev, g_eff)
        ψ2 = normalize(ψ + 0.5 * k2)

        k3 = dτ * rhs(ψ2, μ_prev, g_eff)
        ψ3 = normalize(ψ + k3)

        k4 = dτ * rhs(ψ3, μ_prev, g_eff)

        ψ = ψ + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        ψ *= np.exp(-damping * dτ)
        ψ = normalize(ψ)

        norm_curr = np.trapezoid(np.abs(ψ)**2, x)
        dnorm = (norm_curr - norm_prev) / dτ
        μ_curr = α * dnorm / (norm_curr + eps)
        μ_curr = np.clip(μ_curr, -mu_max, mu_max)

        norms.append(norm_curr)
        μ_log.append(μ_curr)
        μ_prev = μ_curr
        norm_prev = norm_curr

    return x, ψ, np.array(norms), np.array(μ_log), dτ, T
