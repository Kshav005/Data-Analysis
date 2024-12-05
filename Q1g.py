import numpy as np 

def swap_row(arr, row_num1:int, row_num2:int) :
    arr[[row_num1, row_num2]] = arr[[row_num2, row_num1]]
    return arr

def rev_column(arr, column_num:int) :
    arr[:, column_num] = np.array(list(reversed(arr[:,column_num])))
    return arr

m = 9
n = 10
arr = np.array([x for x in range(10, 100)]).reshape(m, n)
print(swap_row(arr, 1, 7))
print(rev_column(arr, 5))
