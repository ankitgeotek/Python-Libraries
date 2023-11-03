import numpy as np
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)

print(a1)
print(a2)
print(a3)

'''
stacking means adding
horizontal stacking (2x2) & (2x2) = (2x4)
vertical stacking (2x2) & (2x2) = (4x2)
'''
a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
a4
a5
#horizontal stack
np.hstack((a4,a5))

#vertical stack
np.vstack((a4,a5))