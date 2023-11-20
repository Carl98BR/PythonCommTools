def acceptance_rejection_sampler(pdf, x, n_samples, *args):

  pdf_x = pdf(x, *args)
  pdf_min, pdf_max  = np.min(pdf_x), np.max(pdf_x)

  if not np.isfinite(pdf_max):
    raise ValueError("pdf has nan or inf values.")

  n_samples = int(n_samples)
  x_min, x_max = np.min(x), np.max(x)
  accepted_samples = []
  acceptance_fraction = []

  while len(accepted_samples) < n_samples:
    unif_x = np.random.uniform(low=x_min, high=x_max, size=n_samples)
    unif_y = np.random.uniform(low=pdf_min, high=pdf_max, size=n_samples)
    accept = unif_y <= pdf(unif_x, *args)
    accepted_samples = np.concatenate([accepted_samples, unif_x[accept]])
    acceptance_fraction = np.concatenate([acceptance_fraction, [np.sum(accept)/n_samples]])

  return accepted_samples[:n_samples], acceptance_fraction
