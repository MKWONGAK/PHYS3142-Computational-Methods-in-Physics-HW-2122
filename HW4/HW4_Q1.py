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
def f(x):
    function = np.exp(-x**2)
    return function

# Do the Romberg calculation and store in R
def Romberg(m,Ni):
    R = np.zeros([m,m])
    for i in range(m):
        if i == 0:
            R[0][0] = trapezoidal(Ni)
        else:
            Ni*=2
            R[i][0] = R[i-1][0]/2 + adaptive_second(Ni)
            for j in range(i):
                R[i][j+1] = R[i][j] + (R[i][j]-R[i-1][j])/(4**(j+1)-1)
    return R

b = 1.0
a = 0.0    
m = 5
Ni = 1
result = Romberg(m,Ni)
#print out the Ri,m and round them to 6 decimal place and make the output
#looks like the fig.1
for i in range(m):
    print('I'+ str(i+1), '=', end = ' ')
    for j in range(i+1):
        if j != i:
            print('{:.6f}'.format(result[i,j]), end =  ' \u2192 ')
        else:
            print('{:.6f}'.format(result[i,j]))
    if i != m-1:
        for j in range(i+1):
            if j == 0:
                print(" "*(5+8), end = '\u2798')
            else:
                print(" "*(9), end = '\u2798')
            if j == i:
                print()
