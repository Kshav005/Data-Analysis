import pandas as pd 

arr = [5, 6, 2, 4, 3]
ind = ["Del", "Bom", "Kol", "Mum", "Ben"]

df = pd.Series(arr, index=ind)
print(df.sort_index())
print(df.sort_values())

