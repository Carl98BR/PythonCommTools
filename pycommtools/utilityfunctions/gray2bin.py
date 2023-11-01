import numpy as np

def gray2bin(gray_matrix, msbf=True):
  binary_matrix = np.zeros_like(gray_matrix)
  
  # Handle the case where gray_matrix is 1D (a single binary number)
  if len(gray_matrix.shape) == 1:
    binary_matrix[0] = gray_matrix[0]
    for i in range(1, gray_matrix.shape[0]):
      binary_matrix[i] = np.bitwise_xor(binary_matrix[i - 1], gray_matrix[i])
  else:
    binary_matrix[:, 0] = gray_matrix[:, 0]
    for i in range(1, gray_matrix.shape[1]):
      binary_matrix[:, i] = np.bitwise_xor(binary_matrix[:, i - 1], gray_matrix[:, i])

  if not msbf:
    binary_matrix = np.flip(binary_matrix, axis=-1)

  return binary_matrix
