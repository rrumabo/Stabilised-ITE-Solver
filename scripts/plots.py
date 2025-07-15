import matplotlib.pyplot as plt
import numpy as np

def plot_results(x, ψ, norms, μ_log, dτ, T):
    steps = int(T / dτ)
    τ = np.linspace(0, T, steps)
    ψ_soliton = 1.0 / np.cosh(x)
    ψ_soliton /= np.sqrt(np.trapz(np.abs(ψ_soliton)**2, x))
    L2_error = np.sqrt(np.trapz(np.abs(np.abs(ψ) - ψ_soliton)**2, x))

    print(f"L² Error vs sech(x) = {L2_error:.6e}")

    plt.figure()
    plt.plot(x, np.abs(ψ), label='|ψ| final')
    plt.plot(x, ψ_soliton, '--', label='sech(x)')
    plt.legend()
    plt.title("Final Wavefunction vs Analytical Soliton")
    plt.tight_layout()
    plt.savefig("figures/final_psi.png")

    plt.figure()
    plt.plot(τ, norms)
    plt.title("Norm Evolution")
    plt.xlabel("Imaginary time τ")
    plt.ylabel("∥ψ∥²")
    plt.tight_layout()
    plt.savefig("figures/norm_evolution.png")

    plt.figure()
    plt.plot(τ, μ_log)
    plt.title("μ(τ) Adaptive Feedback")
    plt.xlabel("Imaginary time τ")
    plt.ylabel("μ(τ)")
    plt.tight_layout()
    plt.savefig("figures/mu_evolution.png")
    plt.show()
