import pandas as pd, numpy as np

n = 10 
arr = [np.random.randint(1, 5000) for _ in range(10)]
arr = pd.Series(arr)
print(arr)
print(arr.idxmax())
print(arr.idxmin())