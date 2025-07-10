from solver import run_mu_solver
from plots import plot_results

if __name__ == "__main__":
    results = run_mu_solver()
    plot_results(*results)
