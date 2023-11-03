from PythonCommTools.pycommtools.utilityfunctions import *
import numpy as np

def berawgn(EbNo, modtype, M):
  gamma_b = 10 ** (EbNo / 10)
  
  if modtype.upper() in ["BFSK", "BPSK", "QPSK"]:
    h1 = 1
    h2 = 1
    g = 2 * gamma_b
  elif modtype.upper() == "MPAM":
    h1 = 2 * (M - 1) / (M * np.log2(M))
    h2 = 1
    g = 6 * gamma_b * np.log2(M) / (M ** 2 - 1)
  elif modtype.upper() == "MPSK":
    h1 = 2 / np.log2(M)
    h2 = np.sin(np.pi / M)
    g = 2 * gamma_b * np.log2(M)
  elif modtype.upper() == "QAM":
    h1 = 4 / np.log2(M)
    h2 = 1
    g = 3 * gamma_b * np.log2(M) / (M - 1)
  else:
    raise ValueError()

  return h1 * qfunc(h2 * np.sqrt(g))
