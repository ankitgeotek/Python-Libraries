import numpy as np

a=np.array([1,2,3,4,np.nan,6])
#remove missing values
np.isnan(a)
a[~(np.isnan(a))]

