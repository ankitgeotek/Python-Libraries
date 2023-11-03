import numpy as np

'''union
'''
m=np.array([1,2,3,4,5])
n=np.array([3,4,5,6,7])
np.union1d(m,n)
np.intersect1d(m,n)
np.setdiff1d(n,m)
np.setdiff1d(m,n) #present in m but absent in n
np.setxor1d(m,n)
np.in1d(m,1)
m[np.in1d(m,1)]


'''
np.clip put value in a range
'''
a
np.clip(a,a_max=75,a_min=25)