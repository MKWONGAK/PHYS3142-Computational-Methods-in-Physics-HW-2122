import numpy as np
import matplotlib.pyplot as plt

def function(x,C,T):
    y = np.tanh(C*x/T)
    return y

x0 = 1
C = 1
Ti = 0.1
Tf = 2
iterations = 50

T = np.linspace(Ti, Tf,101)

x = x0

for i in range(iterations):
    x = function(x,C,T)

plt.plot(T,x)
plt.xlabel("T")
plt.ylabel("x")
plt.show()