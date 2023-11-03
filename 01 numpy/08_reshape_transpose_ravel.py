import numpy as np
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)

print(a1)
print(a2)
print(a3)

'''
transpose interchange row to column and column to row
'''
np.transpose(a2)
a2.T

'''
ravel convert any multi dimension array to 1d array
it is doing same thing as nditer
'''
a2.ravel()

