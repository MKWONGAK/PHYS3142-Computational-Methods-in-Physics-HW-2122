import numpy as np
import matplotlib.pyplot as plt


def f(x):
    y = x**5/(np.exp(x)-1)
    return y

def df(x):
    y = (x**4*(np.exp(x)*(5-x)-5))/(np.exp(x)-1)**2
    return y

x = np.linspace(0.1,20,101)

plt.subplot()
plt.plot(x,f(x), label = "f(x)")
plt.plot(x,df(x), label = "df(x)/dx")
plt.axhline(y=0, color='r', linestyle='--')
plt.legend(loc = 0)
plt.xlabel("x")
plt.show()