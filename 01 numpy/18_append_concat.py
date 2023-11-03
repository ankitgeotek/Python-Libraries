import numpy as np

a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)

np.append(a,200)

b_app=np.append(b,np.random.random((b.shape[0],1)),axis=1)
b_app.shape

'''
concat
'''
c=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)
c
d
#by row
np.concatenate((c,d),axis=0)
#by column
np.concatenate((c,d),axis=1)
#concate 3 array
np.concatenate((c,c,d))

