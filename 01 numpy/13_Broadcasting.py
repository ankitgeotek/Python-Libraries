import numpy as np

#same size
a=np.arange(6).reshape(2,3)
b=np.arange(6,12).reshape(2,3)

print(a+b)

#different Size
a=np.arange(6).reshape(2,3)
b=np.arange(3).reshape(1,3)

a
b

print(a+b)

#more example
a=np.arange(12).reshape(4,3)
b=np.arange(3)
a
b
print(a+b)

a=np.arange(12).reshape(3,4)
b=np.arange(3)
a
b
print(a+b) #operands could not be broadcast together with shapes (3,4) (3,)

a=np.arange(3).reshape(1,3)
b=np.arange(3).reshape(3,1)
a.shape
b.shape
c=a+b
c.shape
print(a+b) 

a=np.arange(4).reshape(1,4)
b=np.arange(3).reshape(3,1)
a.shape
b.shape
c=a+b
c.shape
print(a+b)



a=np.arange(1).reshape(1)
b=np.arange(4).reshape(2,2)
a.shape
b.shape
c=a+b
c.shape
print(a+b)

a=np.arange(12).reshape(3,4)
b=np.arange(12).reshape(4,3)
a.shape
b.shape
c=a+b   #ValueError: operands could not be broadcast together with shapes (3,4) (4,3)
c.shape
print(a+b)  #ValueError: operands could not be broadcast together with shapes (3,4) (4,3)


a=np.arange(16).reshape(4,4)
b=np.arange(4).reshape(2,2)
a.shape
b.shape
c=a+b   #ValueError: operands could not be broadcast together with shapes (3,4) (4,3)
c.shape
print(a+b)  #ValueError: operands could not be broadcast together with shapes (3,4) (4,3)
