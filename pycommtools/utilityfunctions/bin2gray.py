import numpy as np

def bin2gray(x, msbf=True, isSigned=False):
  if not msbf:
    x = x[::-1]
  
  # Shift the input bits one position to the right
  x_right = np.roll(x, 1, axis=-1)
  
  # Handle the case where x is 1D (a single binary number)
  if len(x_right.shape) == 1:
    x_right[0] = 0
  else:
    # Handle the case where x is 2D (a matrix of binary numbers)
    x_right[:, 0] = 0
  
  # Perform an XOR operation between x and x_right to obtain the Gray code
  gray_code = np.bitwise_xor(x, x_right)
  
  return gray_code

