import numpy as np
a=np.arange(10)
np.sin(a)
b=np.arange(100).reshape(10,10)

#sigmoid S(x)= 1/(1-e^(-x))
def sigmoid(array):
    return(1/(1+np.exp(-array)))
sigmoid(a)
sigmoid(b)

#mean Squared error
def mse(actual,predicted):
    return np.mean((actual-predicted)**2)


actual=np.random.randint(1,50,25)
predicted=np.random.randint(1,50,25)
actual
predicted

mse(actual,predicted)
# binary cross error

