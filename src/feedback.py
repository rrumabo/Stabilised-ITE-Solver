def compute_mu(norm, d_norm_dt, alpha, eps=1e-4):
    return alpha * d_norm_dt / (norm + eps)