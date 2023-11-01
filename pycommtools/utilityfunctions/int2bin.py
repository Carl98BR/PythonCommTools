import numpy as np

def int2bin(x, n, msbf=True):
  # Import the NumPy library

  # Convert the integer 'x' to a binary representation with width 'n' using NumPy
  binary_repr = np.vectorize(lambda i: np.binary_repr(i, width=n))

  # Create a NumPy array with binary representations
  binary_array = binary_repr(x)

  # Flatten the array in the specified order
  flattened_array = binary_array.flatten('F')  # 'F' for Most Significant Bit First, 'C' for Least Significant Bit First

  # Convert the flattened array into a list of lists
  binary_list = [list(i) for i in flattened_array]

  # Convert the list of lists into a NumPy matrix of integers
  binary_matrix = np.array(binary_list).astype(int)

  if not msbf:
    # If 'msbf' is False, flip the order of bits within each subarray
    binary_matrix = np.flip(binary_matrix, axis=-1)

  # Return the matrix of binary representations
  return binary_matrix