# μ-Stabilized ITE Solver

This repository implements a norm-stabilized imaginary-time evolution (ITE) solver for the 1D nonlinear Schrödinger equation (NLSE), using an adaptive feedback term μ(τ). The goal is to reach ground-state solitons (e.g. sech(x)) without requiring explicit renormalization at each step.

## Features

- RK4 evolution with adaptive feedback control
- Stabilized norm without post-step normalization
- α-parameter sweeps to explore convergence dynamics
- L² error computation vs sech(x)
- Baseline ITE (no µ) comparison
- Exported plots to `figures/` folder
- Clean, modular `src/` structure and Jupyter notebook

## Notebook

All results, comparisons, and plots are reproducible in:

```
notebooks/demo_1D.ipynb
```

Run it inside Jupyter or VS Code to see:

- Norm evolution
- Feedback signal μ(τ)
- Final |ψ| vs analytical sech(x)
- Comparison with baseline ITE

## Usage (CLI-style)

To run the main solver from terminal:

```
python main.py
```

To test future 3D extensions:

```
python src/muITE3D.py
```

## Requirements

Install dependencies from `requirements.txt`:

```
pip install -r requirements.txt
```

## Future Work

- 2D and 3D NLSE support with spectral Laplacians
- Comparisons with gradient flow and energy-damped solvers
- Interactive visualization of μ(τ), ψ(x), and convergence
- LaTeX paper + results

## License

MIT License — free to use, modify, and distribute.
