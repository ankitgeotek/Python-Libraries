'Array Attributes'
'1st - np.ndim'
'2nd- np.shape'
'3rd np.size'
'4th np.itemsize'
'5th np.dtype'

import numpy as np
a1=np.array(10)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

print(a1)
print(a2)
print(a3)

'1st - np.ndim'
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

'2nd- np.shape'
print(a1.shape)
print(a2.shape)
print(a3.shape)

'3rd np.size'
#tells nos. of items in the array
print(a1.size)
print(a2.size) 
print(a3.size)


'4th np.itemsize'
#how much memory each item is occupying
print(a1.itemsize)  #int32 will occupy 4 bytes
print(a2.itemsize)  #float will occupy 8
print(a3.itemsize)  


'5th np.dtype'
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)



