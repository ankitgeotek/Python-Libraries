import numpy as np

a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)
np.sort(a)

#row wise sorting
np.sort(b)

#column wise sorting
np.sort(b,axis=0)
