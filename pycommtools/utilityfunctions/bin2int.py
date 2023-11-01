import numpy as np

def bin2int(x, msbf=True, isSigned=False):
  # Determine the number of bits in the input 'x' using NumPy.
  n = np.array(x).shape[-1]

  if msbf:
    # If 'msbf' is True, generate weights for MSB-first representation.
    p = 2 ** np.arange(n - 1, -1, -1)
    if isSigned:
      # If 'isSigned' is True, the most significant bit (MSB) has a negative weight.
      p[0] *= -1
  else:
    # If 'msbf' is False, generate weights for LSB-first representation.
    p = 2 ** np.arange(n)
    if isSigned:
      # If 'isSigned' is True, the least significant bit (LSB) has a negative weight.
      p[-1] *= -1

  # Calculate the integer value by taking the dot product of the binary representation and the weights.
  return np.dot(x, p)
