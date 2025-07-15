import numpy as np

def make_laplacian_1d(grid_size=128, L=10.0):
    dx = L / grid_size
    k = 2 * np.pi * np.fft.fftfreq(grid_size, d=dx)
    k_squared = -k**2

    def laplacian(psi):
        psi_hat = np.fft.fft(psi)
        lap_hat = k_squared * psi_hat
        return np.fft.ifft(lap_hat)

    return laplacian