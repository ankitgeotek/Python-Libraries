'''
Functions
np.arrya
np.arange
np.reshape
np.ones
np.zeros
np.random
lenearly space- np.linspace
'''


import numpy as np
'1d tensor/ vector'
a=np.array([1,2,3])
print(a)
'2d array/ Matrix/ '
b=np.array([[0,1,2],[4,5,6]])
print(b)

'3d array/tensor'
c=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,22,33],[44,55,66],[77,88,99]],[[111,222,333],[444,555,666],[777,888,999]]])
print(c)

'dtype'
# default data type of array is float
d=np.array([1,2,3],dtype=float)
print(d)

e=np.array([0,1,2],dtype=bool)
print(e)

f=np.array([0,1,2],dtype=complex)
print(f)


'np.arange' 
# printin arrray in a range a(including) to b(excluding) with interbla c np.arange(a,b,c)
a1=np.arange(1,11,1)
print(a1)

a2=np.arange(1,11,2)
print(a2)

'np.reshape'
a3=np.arange(1,13,1).reshape(4,3)
print(a3)

a4=np.arange(1,13,1).reshape(2,6)
print(a4)

a5=np.arange(1,13,1).reshape(6,2)
print(a5)

a6=np.arange(1,13,1).reshape(2,2,3)
print(a6)


'np.ones and np.zeros'
b1=np.ones(10)
print(b1)

b2=np.zeros(10).reshape(2,5)
print(b2)

'np,random'
#random number between 0-1
c1=np.random.random((3,4))
print(c1)



'np.linspace'
'linspace is very helpful in ploting graphs'
# for creating points in a linear space in the given range
# from a to b (including both a & b) with n nubers of point -->  np.linspace(a,b,n)
# distance between any two adjecent point will be same 
d1=np.linspace(-10,10,11)
print(d1)

d2=np.linspace(-10,10,10)
print(d2)

'np.identity'
e1=np.identity(3)
print(e1)

