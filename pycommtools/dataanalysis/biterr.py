import numpy as np
from pycommtools.utilityfunctions.int2bin import int2bin

def biterr(x, y, k=None, flag=None):
  if x.ndim > 2 or y.ndim > 2:
    raise ValueError("Input arrays cannot have more than two dimensions.")
  
  if np.any(x < 0) or np.any(y < 0):
    raise ValueError("biterr: all elements of A and B must be non-negative integers")
  
  if flag not in ["overall", "row-wise", "column-wise", None]:
    raise ValueError("Invalid 'flag' value. It should be 'overall', 'row-wise', 'column-wise', or None.")
  
  
  try:
    xr, xc = x.shape
  except ValueError:
    xr = 1
    xc = x.shape[0]
  
  try:
    yr, yc = y.shape
  except ValueError:
    yr = 1
    yc = y.shape[0]
  
  max_value = max(np.max(x), np.max(y))
  m = int(np.log2(max_value) + 1)
  
  if k is None:
    k = m
  elif not isinstance(k, int):
    raise ValueError("biterr: K must be a non-negative integer")
  elif k < m:
    raise ValueError("biterr: K must be >= the number of bits in the elements of A and B")
  
  if xr == yr and xc == yc:
    if flag == None:
      flag = "overall"
  elif xr == 1 or yr == 1:
    if flag == "overall":
      raise ValueError("biterr: A and B must have the same size")
    elif flag == "column-wise":
      raise ValueError("biterr: column-wise comparison not possible with row inputs")
    if flag == None:
      flag = "row-wise"
    if xc != yc:
      raise ValueError("biterr: A and B must have the same number of columns for row-wise comparison")
  elif xc == 1 or yc == 1:
    if flag == "overall":
      raise ValueError("biterr: A and B must have the same size")
    elif flag == "row-wise":
      raise ValueError("biterr: row-wise comparison not possible with column inputs")
    if flag == None:
      flag = "column-wise"
    if xr != yr:
      raise ValueError("biterr: A and B must have the same number of rows for column-wise comparison")
  else:
    raise ValueError("biterr: A and B must have the same size")
  
  if flag == 'row-wise':
    numerrs = np.sum(int2bin(np.bitwise_xor(x, y), k).reshape(-1, xc), axis=1)
    total_bits = k * x.shape[0]
  elif flag == 'column-wise':
    numerrs = np.sum(int2bin(np.bitwise_xor(x, y), k).reshape(xr, -1), axis=0)
    total_bits = k * x.shape[-1]
  else:  # flag == 'overall'
    numerrs = np.sum(int2bin(np.bitwise_xor(x, y), k))
    total_bits = k * x.size
  
  ratio = numerrs / total_bits
  
  return numerrs, ratio
