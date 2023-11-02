import numpy as np
from .wgn import wgn

def awgn(x, snr, pwr=None, seed=None, powertype="dB"):
  # If pwr is not specified, set it to 0
  if pwr is None:
    pwr = 0
  
  # If pwr is set to "measured", calculate the power from the input signal x
  if pwr == "measured":
    pwr = np.mean(np.abs(x)**2)
    if powertype == "dB":
      pwr = 10 * np.log10(pwr)
  
  # Calculate the noise power based on SNR and power type
  if powertype == "linear":
    noise_power = pwr / snr
  else:
    noise_power = pwr - snr
  
  # Generate complex or real-valued noise based on the input signal x
  if np.iscomplexobj(x):
    noise = wgn(m, noise_power, 1, seed, powertype, output="complex")
  else:
    noise = wgn(m, noise_power, 1, seed, powertype, output="real")
  
  # Add generated noise to the input signal x
  return x + noise
