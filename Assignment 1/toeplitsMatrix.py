import numpy as np 
from scipy import linalg

x = np.array([2,-1]).reshape(2,-1)
h = np.array([-1,2,1])
print(x.shape[0])
padding = np.zeros(x.shape[0]-1, x.dtype)
first_col = np.r_[h,padding]
first_row = np.r_[h[0], padding]

H = linalg.toeplitz(first_col, first_row)

print(H@x)

