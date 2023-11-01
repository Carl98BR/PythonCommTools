def qammod(signal, M, symorder='gray'):
  # Check if M is a perfect square and a power of 2
  if not (M and (M & (M - 1) == 0) and int(np.sqrt(M)) == np.sqrt(M)):
    raise ValueError("qammod: M must be a perfect square and a power of 2.")
  
  # Create a vector 'm' containing integers from 0 to M-1
  m = np.arange(0, M)
  
  # Check if all elements in 'signal' are in the range [0, M-1]
  if not np.all(np.isin(signal, m)):
    raise ValueError("qammod: All elements of signal must be integers in the range [0, M-1].")
  
  # Define the QAM constellation points
  x = -np.sqrt(M) + 1 + 2 * np.arange(0, np.sqrt(M))
  I, Q = np.meshgrid(x, x)
  constellation = np.reshape(I - 1j * Q, M, order='F')
  
  if symorder.lower() == "bin":
    # Map the signal using binary symbol order
    return constellation[signal]
  elif symorder.lower() == "gray":
    # Generate Gray-coded mapping for demodulation
    gray_coded = np.bitwise_xor(m, np.right_shift(m, 1))
    gray_coded = np.reshape(gray_coded, [int(np.sqrt(M)), int(np.sqrt(M))])
    gray_coded[1::2] = gray_coded[1::2, ::-1]
    return constellation[gray_coded.flatten()[signal]]
  else:
    raise ValueError("Invalid symorder. Must be 'bin' or 'gray'.")
