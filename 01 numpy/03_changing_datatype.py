'Changing type'
'1st astype'



import numpy as np
a1=np.array(10,dtype=np.int32)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8,dtype=np.int64).reshape(2,2,2)

print(a1)
print(a2)
print(a3)

print(a1.dtype)
print(a2.dtype)
print(a3.dtype)


'1st astype'
a3=a3.astype(np.int32)
print(a3.dtype)



 