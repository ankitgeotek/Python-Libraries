import numpy as np

'Fency Indexing'
a=np.arange(24).reshape(6,4)
'''
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23]])
'''
#get 1,3,4th row
a[[0,2,3]]

#get 1,3,4,6 row
a[[0,2,3,5]]



'Boolean Indexing' #index by logics eg- give all even no.
b=np.random.randint(0,100,24).reshape(6,4)
b
'''
array([[60, 32, 90, 48],
       [67, 89, 77,  5],
       [50, 23, 72,  1],
       [86, 94, 98, 87],
       [61, 87, 21, 16],
       [90, 14,  7, 33]])
'''
#find which element of b >50
b>50
#Get element >50
b[b>50]

#even no
b%2==0
#get even no
b[b%2==0]

#get element>50 and even
(b>50) & (b%2==0)
b[(b>50) & (b%2==0)]

#get element>50 or even
(b>50) | (b%2==0)
b[(b>50) | (b%2==0)]

#get elements not divisible by 7
b%7!=0
b[b%7!=0]

~(b%7==0)   # ~ is NOT operator 
b[~(b%7==0)]