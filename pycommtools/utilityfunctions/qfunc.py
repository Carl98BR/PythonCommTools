from scipy.special import erfc
import numpy as np

def qfunc(x):
  return erfc(x / np.sqrt(2)) / 2
