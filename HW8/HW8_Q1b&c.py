import numpy as np

def A(N,V):
    a = np.zeros([N,N])
    w = np.zeros([N,1])
    if N>3:
        for i in range(N):
            if i == 0:
                a[i,i],a[i,i+1],a[i,i+2] = 3,-1,-1
                w[i,0] = V     
            elif i == 1:
                a[i,i-1],a[i,i],a[i,i+1],a[i,i+2] = -1,4,-1,-1
                w[i,0] = V
            elif i == N-2:
                a[i,i+1],a[i,i],a[i,i-1],a[i,i-2] = -1,4,-1,-1
            elif i == N-1:
                a[i,i],a[i,i-1],a[i,i-2] = 3,-1,-1
            else:
                a[i,i-2],a[i,i-1],a[i,i],a[i,i+1],a[i,i+2] = -1,-1,4,-1,-1
            
    
    if N == 1:
        a = np.array([[2]])
        w = np.array([[V]])
    if N == 2:
        a = np.array([[3,-1],
                      [-1,3]])
        w = np.array([[V],
                      [V]])
    if N == 3:
        a = np.array([[3,-1,-1],
                      [-1,4,-1],
                      [-1,-1,3]])
        w = np.array([[V],
                      [V],
                      [0]])
    return a,w


a5,w5 = A(5,5)
a6,w6 = A(6,5)

# Q1b
print("The A and w for N = 5 is")
print(a5)
print("and")
print(w5)
print("The A and w for N = 6 is")
print(a6)
print("and")
print(w6)
print()
#Q1c
print("The solution for N = 5 is")
print(np.linalg.solve(a5,w5))
print("The solution for N = 6 is")
print(np.linalg.solve(a6,w6))
