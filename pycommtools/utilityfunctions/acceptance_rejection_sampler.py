def acceptance_rejection_sampler(pdf_function, domain_values, n_samples, *args):

  pdf_values = pdf_function(domain_values, *args)
  min_pdf, max_pdf = np.min(pdf_values), np.max(pdf_values)
  
  if not np.isfinite(max_pdf):
    raise ValueError("The PDF has NaN or infinite values.")
  
  n_samples = int(n_samples)
  min_domain, max_domain = np.min(domain_values), np.max(domain_values)
  accepted_samples = []
  acceptance_rate = []
  
  while len(accepted_samples) < n_samples:
    uniform_x = np.random.uniform(low=min_domain, high=max_domain, size=n_samples)
    uniform_y = np.random.uniform(low=min_pdf, high=max_pdf, size=n_samples)
    acceptance_condition = uniform_y <= pdf_function(uniform_x, *args)
    accepted_samples = np.concatenate([accepted_samples, uniform_x[acceptance_condition]])
    acceptance_rate = np.concatenate([acceptance_rate, [np.sum(acceptance_condition)/n_samples]])
  
  return accepted_samples[:n_samples], acceptance_rate
