import numpy as np

def pskdemod(signal, M, phi=0, symorder='gray'):
  # Check if 'symorder' is valid (either 'bin' or 'gray')
  if symorder.lower() not in ["bin", "gray"]:
    raise ValueError("Invalid symorder. Must be 'bin' or 'gray'.")
  
  # Create a vector 'm' containing integers from 0 to M-1
  m = np.arange(0, M)
  
  # Calculate the symbol index based on phase difference and 'M'
  symbol_index = np.mod(np.round((np.angle(signal) - phi) * M / (2 * np.pi)), M).astype(int)
  
  # Demodulate based on the specified 'symorder'
  if symorder == "bin":
    return symbol_index
  elif symorder == "gray":
    m = np.arange(M)
    mapping = np.bitwise_xor(m, np.right_shift(m, 1))
    return mapping[symbol_index]

