import time
import numpy as np
from numba import jit
import random
def f(x):
    return 3*x**2
def w(x):
    return 2*x # here the integration of w(x) from 0 to 1 is 1
def g(x):
    return f(x)/w(x)
N=100
M=10000
a=0
b=1
time1=time.time()
all_g=[]
for m in range(M):
    g_avg=0
    x_i = a + (b-a)*np.random.random()
    for n in range(N):
        x_next = a + (b-a)*np.random.random()
        if min(w(x_next)/w(x_i),1)>np.random.random():
            x_i = x_next
        g_avg += g(x_i)/N
    all_g.append(g_avg)
mean=(np.sum(all_g)/M) # the mean of M many mean values
time2=time.time()   
print("Original: mean =",mean,"runtime:",round(time2-time1,3),"seconds") 
time3=time.time() 
# broadcasting, use broadcasting to replace the for loop over M
all_gx_MN=np.zeros((M,N))
x_i=a+(b-a)*np.random.random(size=(M))
for n in range(N):
    all_gx_MN[:,n]=g(x_i)
    x_next = a + (b-a)*np.random.random(size=(M))
    T=w(x_next)/w(x_i)
    indices_larger_than_1 = np.where(T>1)[0] # find where T_ij>1
    T[indices_larger_than_1]=np.ones(len(indices_larger_than_1))
    conditions=T>np.random.random(size=(M)) # an array of True or False
    x_i = x_next*conditions+x_i*(1-conditions) # with length M
    
all_gx_M=all_gx_MN.sum(axis=1)/N
mean=all_gx_M.sum()/M
time4=time.time()   
print("Broadcasting: mean =",mean,"runtime:",round(time4-time3,3),"second")