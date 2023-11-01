import numpy as np
from scipy.spatial.distance import cdist
from .qammod import *

def qamdemod(modulated_signal, M, symorder='gray'):
  # Create a QAM constellation based on the specified 'symorder'
  constellation = qammod(np.arange(0, M), M, symorder)
  
  # Extract the real and imaginary parts of the constellation and modulated signals
  constellation = np.column_stack((np.real(constellation), np.imag(constellation)))
  modulated_signal = np.column_stack((np.real(modulated_signal), np.imag(modulated_signal)))
  
  # Calculate the Euclidean distance between each modulated point and constellation points
  return np.argmin(cdist(modulated_signal, constellation, metric='euclidean'), axis=1)
