import numpy as np

arr = np.empty((0, 6), np.float64)
arr = np.append(arr,[2,3,2,4,5,8])
arr = np.append(arr,[2,3.4,2,4,5.7,8])
print(arr)