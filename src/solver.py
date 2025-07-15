import numpy as np
from feedback import compute_mu

def rk4_step(psi, hamiltonian_fn, mu, dt):
    i_mu_psi = lambda ψ: 1j * mu * ψ

    def dpsi_dt(ψ):
        return -hamiltonian_fn(ψ) + i_mu_psi(ψ)

    k1 = dpsi_dt(psi)
    k2 = dpsi_dt(psi + 0.5 * dt * k1)
    k3 = dpsi_dt(psi + 0.5 * dt * k2)
    k4 = dpsi_dt(psi + dt * k3)

    return psi + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

def run_simulation(psi0, hamiltonian_fn, alpha, dt, steps, dx):
    psi = psi0.copy()
    norm_history = []
    mu_history = []
    psi_history = []

    prev_norm = np.trapz(np.abs(psi)**2, dx=dx)

    for _ in range(steps):
        norm = np.trapz(np.abs(psi)**2, dx=dx)
        d_norm_dt = (norm - prev_norm) / dt
        mu = compute_mu(norm, d_norm_dt, alpha)

        psi = rk4_step(psi, hamiltonian_fn, mu, dt)

        norm_history.append(norm)
        mu_history.append(mu)
        psi_history.append(psi.copy())

        prev_norm = norm

    return {
        "psi_final": psi,
        "psi_history": psi_history,
        "norm_history": norm_history,
        "mu_history": mu_history
    }
    
def run_baseline_simulation(psi0, hamiltonian_fn, dt, steps, dx):
    psi = psi0.copy()
    norm_history = []
    psi_history = []

    for _ in range(steps):
        def dpsi_dt(ψ):
            return -hamiltonian_fn(ψ)  # no µ(τ) term

        k1 = dpsi_dt(psi)
        k2 = dpsi_dt(psi + 0.5 * dt * k1)
        k3 = dpsi_dt(psi + 0.5 * dt * k2)
        k4 = dpsi_dt(psi + dt * k3)

        psi += (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        norm = np.trapz(np.abs(psi)**2, dx=dx)
        norm_history.append(norm)
        psi_history.append(psi.copy())

    return {
        "psi_final": psi,
        "psi_history": psi_history,
        "norm_history": norm_history
    }