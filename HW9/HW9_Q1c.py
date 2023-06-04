import numpy as np
import matplotlib.pyplot as plt

def function(x,C,T):
    y = np.tanh(C*x/T)
    return y

T = 0.9
C = 1
x0 = 1
sol = []
error_act = []
error_app = []
x_true = x0
for i in range(50):
    x_true = function(x_true,C,T)

x = x0
sol.append(x0)
for i in range(1,31):
    x = function(x,C,T)
    sol.append(x)
    if i >= 5: 
        error_act.append(abs(x-x_true))
        error_app.append(abs((sol[i-1]-sol[i])**2/(2*sol[i-1]-sol[i-2]-sol[i])))




plt.subplot()
plt.semilogy(range(5,31),error_act,label = "Actual error")
plt.semilogy(range(5,31),error_app,label = "Estimate error")
plt.legend(loc = 0)
plt.xlabel("T")
plt.ylabel("error")
plt.show()
