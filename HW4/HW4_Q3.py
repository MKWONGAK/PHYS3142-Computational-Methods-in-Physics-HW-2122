import numpy as np

# The trapezoidal formula
def trapezoidal(N):
    step = (b-a)/N
    x = np.linspace(a,b,N+1, endpoint= True)
    return step*(np.sum(f(x)[1:N]) + (f(x[0])+f(x[-1]))/2)
# The adaptive terms formula
def adaptive_second(N):
    step = (b-a)/N
    x = np.linspace(a,b,N+1, endpoint= True)[1:N+1:2]
    return step*np.sum(f(x)) 
# The function
def f(z):
    function = 1/(2*z**2-2*z+1)
    return function

# Calculate the error
def error(R):
    T = (np.pi) / 2
    return abs(T-R)

def Adative_trapezoidal(N):
    R = []
    R.append(trapezoidal(N))
    i = 0
    # find the N when error < 10**-8
    while error(R[i]) >= pow(10,-8):
        i+=1
        N*=2
        R.append(R[i-1]/2 + adaptive_second(N))
    return N

a = 0.
b = 1.

print(Adative_trapezoidal(1))
