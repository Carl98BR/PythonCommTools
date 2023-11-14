from PythonCommTools.pycommtools.utilityfunctions import *
import numpy as np
def berawgn(EbNo, modtype, M):
  def Pb(k, gamma, M):
    return 1 / np.sqrt(M) * np.sum([w(i, k, M) * erfc((2 * i + 1) * np.sqrt(3 / 2 * np.log2(M) * gamma / (M - 1))) for i in range(int((1 - 2 ** (-k)) * np.sqrt(M)))])
  
  def w(i, k, M):
    return (-1) ** np.floor(i * 2 ** (k - 1) / np.sqrt(M)) * (2 ** (k - 1) - np.floor(i * 2 ** (k - 1) / np.sqrt(M) + 1 / 2))
    
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
    result = np.vectorize(lambda x: 1 / np.log2(np.sqrt(M)) * np.sum([Pb(k, x, M) for k in range(1, int(np.log2(np.sqrt(M))) + 1)]))
    return result(gamma_b)
  else:
    raise ValueError("BERAWGN: Invalid modulation type")

  return h1 * qfunc(h2 * np.sqrt(g))
