import pandas as pd, numpy as np


n = 10 
arr = [np.random.randint(1, 5) for _ in range(n)]
arr = pd.Series(arr)
print(arr.rank(method="first"))
print(arr.rank(method="max"))
