# μ-Stabilized ITE Solver

This repository implements an adaptive imaginary-time evolution (ITE) solver for the nonlinear Schrödinger equation. The method dynamically adjusts a feedback parameter μ(τ) to maintain wavefunction normalization and improve convergence toward soliton solutions.

## Features
- Norm-preserving ITE via log-derivative μ(τ)
- RK4 evolution with optional damping
- Parameter sweeps over (g, α)
- Heatmaps of L² error, norm drift, μ variability
- Final ψ vs analytical sech(x) comparison
- Full LaTeX paper included

### 🧠 3D μ-Stabilized ITE Extension

This module extends the μ(τ)-regulated imaginary time evolution to 3D grids using spectral methods.

- Preserves norm across 3D domains
- Allows projection and slice visualization
- Ready for external potentials and parametre sweeps

Run:
```bash
python solver_3D.py

## Usage
```bash
python main.py
