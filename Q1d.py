import numpy as np 

arr1 = np.random.random((4))
arr2 = np.random.random((4))
arr3 = np.random.random((4))

arr4 = arr3 - arr2 
arr5 = 2*arr1

print(np.cov(arr1, arr4))
print(np.corrcoef(arr1, arr5))

