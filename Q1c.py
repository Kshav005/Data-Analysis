import numpy as np


arr = np.array([np.nan, 0, 34, 23, 9, 0, np.nan])

null = []
non_null = []
zeroes = []

print(list(np.where(arr==0)[0]))
print(list(np.where(arr!=0)[0]))
print(list(np.where(np.isnan(arr))[0]))