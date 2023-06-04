import numpy as np
import matplotlib.pyplot as plt


def f(x):
    y = x**5/(np.exp(x)-1)
    return y

def d2f(x):
    y = x**3*((x**2-10*x+20)*np.exp(2*x)+(x**2+10*x-40)*np.exp(x)+20)/(np.exp(x)-1)**3
    return y

gamma = -0.1
x0 = 1
x1 = 2
x = [x0,x1]
for i in range(2,31):
    x_tmp = x[i-1] - gamma*(f(x[i-1])-f(x[i-2]))/(x[i-1]-x[i-2])
    x.append(x_tmp)
   
    
plt.plot(range(31),x)
plt.show()

plt.plot(np.linspace(0.1,20,101), d2f(np.linspace(0.1,20,101)))
plt.show()
    
