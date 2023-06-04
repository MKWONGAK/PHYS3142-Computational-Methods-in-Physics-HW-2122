import numpy as np
import matplotlib.pyplot as plt

# The trapezoidal formula
def trapezoidal(N,a):
    step = (b-a)/N
    x = np.linspace(a,b,N+1, endpoint= True)
    return step*(np.sum(f(x)[1:N]) + (f(x[0]) + f(x[-1]))/2)

# The function
def f(x):
    function = (np.cos(x) + np.sin(np.sqrt(x))**2)/np.sqrt(x)
    return function

b=1
a = np.array([0.1,0.01,0.001,0.0001,0.00001])
N = np.array(range(1,3500))

fig, axes= plt.subplots(dpi=100)
axes.set_xlabel("N")
axes.set_ylabel("I")
axes.set_xscale("log", base=10)
axes.set_yscale("log", base=10)
for i in a:
    I = []
    #store the I for each N
    for j in N:
        I.append(trapezoidal(j,i))
    axes.plot(N, I, label = ("I" + str(i)))
    #compare the I for two nearby Ni and Ni-1, is their difference is smaller than 10^-5
    #then I said it is converged
    for k in range(1,len(I)):
        if abs(I[k] - I[k-1]) < 10**-5:
            print("convergence values is", I[k], "for a = " +str(i))
            print("the corresponding N is ", k)
            break
axes.legend(loc = 0)
plt.show()

