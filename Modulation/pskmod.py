def pskmod(signal, M, phi=0, symorder='gray'):
    # Create a vector 'm' containing integers from 0 to M-1
    m = np.arange(0, M)
    
    # Check if all elements of 'signal' are within the valid range [0, M-1]
    if not np.all(np.isin(signal, m)):
        raise ValueError("pskmod: All elements of 'signal' should be integers in the range [0, M-1]")
    
    # Calculate the PSK constellation points
    constellation = np.exp(1j * 2 * np.pi * m / M + 1j * phi)
    
    # Choose modulation order based on 'symorder' ('bin' or 'gray')
    if symorder.lower() == "bin":
        modulated_signal = constellation[signal]
    elif symorder.lower() == "gray":
        # Generate Gray-coded vector
        gray_coded = np.argsort(np.bitwise_xor(m, np.right_shift(m, 1)))
        modulated_signal = constellation[gray_coded[signal]]
    else:
        raise ValueError("Invalid symorder")
    
    # If the modulated signal is real (no imaginary part), cast it to real numbers
    if np.all(np.imag(modulated_signal) == 0):
        modulated_signal = np.real(modulated_signal).astype(int)
    
    return modulated_signal

