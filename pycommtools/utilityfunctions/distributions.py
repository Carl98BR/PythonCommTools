from scipy.special import iv, gamma
from numpy import sqrt, exp, pi

def eta_mu_pdf(x, eta, mu):
  return 4 * sqrt(pi) * mu ** (mu + 0.5) * x ** (2 * mu) * exp(- 2 * mu * x ** 2 / (1 - eta ** 2)) * iv(mu - 0.5, 2 * eta * mu * x ** 2 / (1 - eta ** 2)) / (eta ** (mu - 0.5) * sqrt(1 - eta ** 2) * gamma(mu))

def kappa_mu_pdf(x, kappa, mu):
  return 2 * mu * (1 + kappa) ** ((mu + 1) / 2) * x ** mu * exp(-mu * (1 + kappa) * x ** 2) * iv(mu - 1, 2 * mu * sqrt(kappa * (1 + kappa)) * x) / (kappa ** ((mu - 1) / 2) * exp(kappa * mu))

def alpha_mu_pdf(x, alpha, mu):
  return alpha * mu ** mu * x ** (alpha * mu - 1) * exp(-mu * x ** alpha) / gamma(mu)
