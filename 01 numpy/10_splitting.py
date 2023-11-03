'''Just opposite of stacking'''
import numpy as np

a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
a4
a5

np.hsplit(a4,2) #(array, cut into n parts)
np.vsplit(a5,3)