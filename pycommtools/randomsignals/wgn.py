import numpy as np

def wgn(m, n, p, imp=1, seed=None, powertype="dBW", output="real"):
  # Convert the input power level to linear scale based on powertype
  if powertype == "dB" or powertype == "dBW":
    p = 10**(p / 10)
  elif powertype == "dBm":
    p = 10**((p - 30) / 10)
  
  # Calculate the variance of the noise
  variance = p * imp
  
  if seed is not None:
    np.random.seed(seed)
  
  if output == "real":
    # Generate real-valued noise samples
    noiseReal = np.random.normal(0, np.sqrt(variance), (m, n))
    return noiseReal
  elif output == "complex":
    # Generate complex-valued noise samples
    noiseReal = np.random.normal(0, np.sqrt(variance / 2), (m, n))
    noiseImag = np.random.normal(0, np.sqrt(variance / 2), (m, n))
    noiseComplex = noiseReal + 1j * noiseImag
    return noiseComplex
  else:
    raise ValueError("The 'output' parameter must be 'real' or 'complex.")
