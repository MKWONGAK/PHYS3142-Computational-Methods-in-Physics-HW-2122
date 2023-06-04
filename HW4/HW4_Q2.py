import numpy as np
import matplotlib.pyplot as plt
import gaussxw

# The Si of the adaptive simpson
def Si(N):
    step = (b-a)/N
    k = np.array(range(2,N-1,2))
    return (2*np.sum(f(step*k)) + f(a) + f(b))/3
# The Ti of the adaptive simpson
def Ti(N):
    step = (b-a)/N
    k = np.array(range(1,N,2))
    return (2/3)*np.sum(f(step*k))

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
def f(x):
    function = (4)*(x**3)*np.exp(x**4)
    return function

#Adaptive simpson
def Adaptive_Simpson(N):
    I = np.zeros(m)
    S = np.zeros(m)
    T = np.zeros(m)
    for i in range(m):
        step = (b-a)/N
        T[i] = Ti(N)
        if i == 0:
            S[i] = Si(N)
        else:
            S[i] = S[i-1] + T[i-1]
        I[i] = step*(S[i]+2*T[i])
        N*=2
    return I

# Do the Romberg calculation and store in R
def Romberg(m,Ni):
    R = np.zeros([m,m])
    x = []
    for i in range(m):
        if i == 0:
            R[0][0] = trapezoidal(Ni)
        else:
            Ni*=2
            R[i][0] = R[i-1][0]/2 + adaptive_second(Ni)
            for j in range(i):
                R[i][j+1] = R[i][j] + (R[i][j]-R[i-1][j])/(4**(j+1)-1)
                if i>=2 and j==i-1:
                    x.append(R[i][j+1])
    return np.array(x)

#Do the Gaussian quadrature
def Gaussian(N):
    G = np.zeros(m)
    for i in range(m):
        x,w = gaussxw.gaussxwab(N,a,b)
        G[i] = np.sum(w*f(x))
        N*=2
    return G

m = 6
a = 0.
b = 1.
N = 4
#the true value
T = np.exp(1) - 1
Simpson, Rom, Gauss = Adaptive_Simpson(N), Romberg(m+2,1), Gaussian(N)
Error_s, Error_r, Error_g = abs(Simpson-T), abs(Rom-T), abs(Gauss-T)

Ni = np.array([4,8,16,32,64,128])

#plot graph
fig, axes= plt.subplots(dpi=900)
axes.set_xlabel("N")
axes.set_ylabel("Error")
axes.plot(Ni, Error_s, label = "Adaptive Simpson's rule")
axes.plot(Ni, Error_r, label = "Romberg integral")
axes.plot(Ni, Error_g, label = "Gaussian quadrature")
axes.set_xscale("log", base=10)
axes.set_yscale("log", base=10)
axes.legend(loc = 0)
plt.show()




    
        
    



