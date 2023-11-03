'==>1'
'Iterating'

import numpy as np
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)

print(a1)
print(a2)
print(a3)


#In 1d array each item will be printed
for i in a1:
    print(i)


#In 2d array each row will be printed
for i in a2:
    print(i)

# for printing all item in n-d array
for i in np.nditer(a3):     #np.nditer  will convert nd array in 1d array
    print(i)
