import numpy as np


def df(x):
    y = (x**4*(np.exp(x)*(5-x)-5))/(np.exp(x)-1)**2
    return y

def d2f(x):
    y = x**3*((x**2-10*x+20)*np.exp(2*x)+(x**2+10*x-40)*np.exp(x)+20)/(np.exp(x)-1)**3
    return y

x0 = 5
sol = [x0]
i = 0
x = x0
e = 100
while e > 10**(-6):
    x = x-df(x)/d2f(x)
    sol.append(x)
    e = abs(sol[i+1]-sol[i])
    i+=1

print(i-1)
print(sol[i-1])
print(sol)