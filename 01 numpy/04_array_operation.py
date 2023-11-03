'Array operation'
import numpy as np

a1=np.arange(12).reshape(3,4)       #12 element starting from 0 i.e 0-11
a2=np.arange(12,24).reshape(3,4)    #element from 12-24 including 12 and excluding 24
print(a1)
print(a2)


'1 Airthmatic operation'

'1.a Scalar airthmatic operation'
print(a1*2)     #a1 is like matrix and 2 as scalar
print(a1-5)
print(a1+5)
print(a1/5)

'1.b vector operation (here shape should be same)'
print(a1+a2)

'2nd relational operation'
print(a2>15)
print(a2==15)
print(a2<15)




