import numpy as np

# The trapezoidal formula
def trapezoidal(N):
    step = (b-a)/N
    x = np.linspace(a,b,N+1, endpoint= True)
    return step*(np.sum(f(x)[1:N]) + f(x[-1])/2)
# The adaptive terms formula
def adaptive_second(N):
    step = (b-a)/N
    x = np.linspace(a,b,N+1, endpoint= True)[1:N+1:2]
    return step*np.sum(f(x)) 
# The function
def f(x):
    function = (np.cos(x) + np.sin(np.sqrt(x))**2 -1)/np.sqrt(x)
    return function

def Adaptive_trapezoidal(N):
    R = []
    R.append(trapezoidal(N))
    N*=2
    R.append(R[0]/2 + adaptive_second(N))
    i = 1
    # find the N when error <= 10**-5
    while (1/3)*(R[i]-R[i-1]) > pow(10,-5):
        i+=1
        N*=2
        R.append(R[i-1]/2 + adaptive_second(N))
    return R[i]

a = 0
b = 1

print("I =", Adaptive_trapezoidal(1)+2)