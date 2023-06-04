import matplotlib.pyplot as plt
import numpy as np
from numba import jit

column = 10
row = 10
N = row*column
Jx = 2
Jy = -1
beta = 1
T = np.linspace(1,10,46)
repeat = 5000

@jit(nopython=True)
def delta_energy(i,j,S):
    #periodic conditions
    left = np.mod(j-1,column)
    right = np.mod(j+1,column)
    up = np.mod(i-1,row)
    down = np.mod(i+1,row)
    
    E = 2*S[i,j]*(Jx*(S[i,left]+S[i,right]) + Jy*(S[up,j]+S[down,j]))
    return E

@jit(nopython=True)
def accept(S,T):
    i = np.random.randint(row)
    j = np.random.randint(column)
    alpha = np.exp(-beta*delta_energy(i,j,S)/T)
    if alpha > np.random.rand():
        S[i,j] = -S[i,j]
    return S

@jit(nopython=True)
def Hamiltonian(S):
    H = 0
    #sum each pair
    for i in range(row):
        for j in range(column-1):
            H += Jx*S[i,j]*S[i,j+1]
    for i in range(row-1):
        for j in range(column):
            H += Jy*S[i,j]*S[i+1,j]
    return -1*H

@jit(nopython=True)          
def energy(S):
    E = Hamiltonian(S)/N
    return E

@jit(nopython=True)
def var(x):
    size = len(x)
    x_bar = np.sum(x)/size 
    x2_bar = np.sum(x**2)/size
    return x2_bar - x_bar**2

E = []
M = []
Cv = []
X = []

for t in T:
    E_tmp = []
    M_tmp = []
    state = np.sign(np.random.rand(row,column)-0.5)
    for r in range(repeat):
        for s in range(N):
            state = accept(state,t)
        E_tmp.append(energy(state))
        M_tmp.append(abs(np.sum(state))/N)
    E_tmp = np.array(E_tmp)
    M_tmp = np.array(M_tmp)
    E.append(np.sum(E_tmp)/repeat)
    M.append(np.sum(M_tmp)/repeat)
    Cv.append(var(E_tmp)/t**2)
    X.append(var(M_tmp)/t)

plt.subplot(221)
plt.title("Eenergy vs. Temperature")
plt.xlabel("T")
plt.ylabel("E")
plt.plot(T,E)

plt.subplot(222)
plt.title("Magnetization vs. Temperature")
plt.xlabel("T")
plt.ylabel("M")
plt.plot(T,M)

plt.subplot(223)
plt.title("Capacity vs. Temperature")
plt.xlabel("T")
plt.ylabel("C")
plt.plot(T,Cv)

plt.subplot(224)
plt.title("Susceptibility vs. Temperature")
plt.xlabel("T")
plt.ylabel("X")
plt.plot(T,X)

plt.show() 