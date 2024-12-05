import numpy as np 

arr1 = np.random.random(10)
arr2 = np.random.random(10)
print(arr1[:10//2]+arr2[:10//2])
print(arr1[10//2:]*arr2[10//2:])