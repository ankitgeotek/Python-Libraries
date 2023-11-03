'Math Function'
import numpy as np

a1=np.arange(12).reshape(3,4)       #12 element starting from 0 i.e 0-11
a2=np.arange(12,24).reshape(3,4)    #element from 12-24 including 12 and excluding 24
print(a1)
print(a2)

'max/min/sum/prod'
print(np.max(a1))
print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))

#finding maximum of each row 
print(np.max(a1,axis=1)) #axis=1 mean row, axis=0 means column
#finding sum of each row 
print(np.sum(a1,axis=1))


'mean/median/std/var'
print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))

'trignomatric function'
print(np.sin(a1))
print(np.cos(a1))
print(np.tan(a1))

'==>dot product'
'''
dot product is possible only when shape of matrix are in
certain especific format i.e A(x,y) B(y,z) 
result of dot product will have shape of A.B(x,z)
'''
a3=np.linspace(-10,10,15).reshape(3,5)
a4=np.linspace(15,30,15).reshape(5,3)
print(a3)
print(a4)

a3_a4_dot=np.dot(a3,a4)
print(a3_a4_dot)
print(a3_a4_dot.shape)

'log and exponent'
np.log(a1)
np.exp(a1)

'round/floor/ceil'
a5=np.random.random((2,3))*100
print(a5)
print(np.round(a5))     #round-nearest integer round off
print(np.floor(a5))     #floor- back integer round off
print(np.ceil(a5))     #ceil- next integer round off

