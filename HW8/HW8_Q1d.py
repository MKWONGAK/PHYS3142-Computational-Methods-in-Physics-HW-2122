import numpy as np
import time
import banded

def A(N,V,Nup,Ndown):
    a = np.zeros([N,N])
    w = np.zeros([N,1])
    k = Nup +Ndown
    b = np.zeros([k+1,N])
    if N>3:
        for i in range(N):
            if i == 0:
                a[i,i],a[i,i+1],a[i,i+2] = 3,-1,-1
                w[i,0] = V
                b[k-2,i],b[k-1,i],b[k,i] = 3,-1,-1
                
            elif i == 1:
                a[i,i-1],a[i,i],a[i,i+1],a[i,i+2] = -1,4,-1,-1
                w[i,0] = V
                b[k-3,i],b[k-2,i],b[k-1,i],b[k,i] = -1,4,-1,-1
            elif i == N-2:
                a[i,i+1],a[i,i],a[i,i-1],a[i,i-2] = -1,4,-1,-1
                b[k-4,i],b[k-3,i],b[k-2,i],b[k-1,i] = -1,-1,4,-1
            elif i == N-1:
                a[i,i],a[i,i-1],a[i,i-2] = 3,-1,-1
                b[k-4,i],b[k-3,i],b[k-2,i] = -1,-1,3
            else:
                a[i,i-2],a[i,i-1],a[i,i],a[i,i+1],a[i,i+2] = -1,-1,4,-1,-1
                b[k-4,i],b[k-3,i],b[k-2,i],b[k-1,i],b[k,i] = -1,-1,4,-1,-1

    if N == 1:
        a = np.array([[2]])
        w = np.array([[V]])
        b = a
    if N == 2:
        a = np.array([[3,-1],
                      [-1,3]])
        w = np.array([[V],
                      [V]])
        b = a
    if N == 3:
        a = np.array([[3,-1,-1],
                      [-1,4,-1],
                      [-1,-1,3]])
        w = np.array([[V],
                      [V],
                      [0]])
        b = a
    return a,w,b



a10000, w10000, b10000 = A(10000,5,2,2)

# using numpy.linalg
t1 = time.time()
sol1 = np.linalg.solve(a10000,w10000)
print(sol1)
print("the time used for using np.linalg is", time.time() - t1)

#using banded
t2 = time.time()
sol2 = banded.banded(b10000, w10000, 2, 2)
print(sol2)
#sol2 = banded.banded(a,w10000,Nup,Ndown)
print("the time used for using banded is", time.time() - t2)













