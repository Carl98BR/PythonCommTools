def pamdemod(modulated_signal, M, phi=0, symorder='bin'):
  # Check if 'symorder' is valid (either 'bin' or 'gray')
  if symorder.lower() not in ["bin", "gray"]:
    raise ValueError("Invalid symorder. Must be 'bin' or 'gray'.")
  
  # Define the PAM constellation symbols
  symbols = np.arange(-M + 1, M, 2) * np.exp(-1j * phi)
  
  # Determine the closest symbol for each modulated signal point
  symbol_index = np.argmin(np.abs(np.array(modulated_signal)[:, np.newaxis] - symbols), axis=1)
  
  # Demodulate based on the specified 'symorder'
  if symorder == "bin":
    return symbol_index
  elif symorder == "gray":
    # Generate Gray-coded mapping for demodulation
    m = np.arange(M)
    mapping = np.bitwise_xor(m, np.right_shift(m, 1))
    return mapping[symbol_index]
