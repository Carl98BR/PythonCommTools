from PythonCommTools.pycommtools.utilityfunctions import *
import numpy as np

def serawgn(EbNo, modtype, M):
  gamma_b = 10 ** (EbNo / 10)
  gamma_s = np.log2(M) * gamma_b
  
  if modtype.upper() in ["BFSK", "BPSK", "QPSK"]:
    pass
  elif modtype.upper() == "MPAM":
    return 2 * (1 - 1 / M) * qfunc(np.sqrt( 6 * gamma_s / (M ** 2 - 1)))
  elif modtype.upper() == "MPSK":
    pass
  elif modtype.upper() == "QAM":
    return 1 - (1 - 2 * (1 - 1 / np.sqrt(M)) * qfunc(np.sqrt(3 * gamma_s / (M - 1)))) ** 2
  else:
    raise ValueError("BERAWGN: Invalid modulation type")
