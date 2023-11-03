import numpy as np
#plotting a 2d plot
#x=y
x=np.linspace(-10,10,100)
y=x
x
y

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

#y=x^2
y=x**2
plt.plot(x,y)
plt.show()

#y=sin(x)
y=np.sin(x)
plt.plot(x,y)
plt.show()


#y=xlog(x)
y=x*np.log(x)
plt.plot(x,y)
plt.show()


#Sigmoid(x)
#y=1/(1+e^(-x))
y=1/(1+np.exp(-x))
plt.plot(x,y)
plt.show()