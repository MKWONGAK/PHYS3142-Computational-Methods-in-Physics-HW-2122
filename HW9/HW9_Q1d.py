import numpy as np
import matplotlib.pyplot as plt

def function(x,C,T):
    y = np.tanh(C*x/T)
    return y

T = 0.9
C = 1
x0 = 1
w = 1
sol = []
error_rel = []
error_ove = []

x_true = x0
for i in range(50):
    x_true = (1+w)*function(x_true,C,T) - w*x_true
    
x1 = x0
x2 = x0
sol.append(x0)
for i in range(1,31):
    x1 = function(x1,C,T)
    x2 = (1+w)*function(x2,C,T) - w*x2
    if i >= 5: 
        error_rel.append(abs(x1-x_true))
        error_ove.append(abs(x2-x_true))

plt.subplot()
plt.semilogy(range(5,31),error_rel,label = "relaxation")
plt.semilogy(range(5,31),error_ove,label = "over_relaxation")
plt.legend(loc = 0)
plt.xlabel("T")
plt.ylabel("error")
plt.show()




