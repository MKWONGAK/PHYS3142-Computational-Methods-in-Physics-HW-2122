import numpy as np

#sort the matrix such that below the last 1 of each column is 0
def sort(A,m):
    A1 = np.copy(A)
    k1 = 0
    for i in range(m):
        pos = np.where(A1[:,i] != 0)[0]
        k2 = 0
        for j in pos:
            if j>= k1:
                x = np.copy(A1[k2+k1,:])
                y = np.copy(A1[j,:])
                A1[j,:], A1[k2+k1,:] = x,y
                k2+=1
        k1 += k2
    return(A1)


def gaussian(A):
    m = len(A[0,:])
    n = len(A[:,0])
    A1 = sort(A,m)
    for i in range(n-1):
        pos1 = np.where(A1[i,:] != 0)[0]
        if len(pos1) == 0:
            return A1
        pos2 = np.where(A1[:,i] != 0)[0]
        for j in range(len(pos2)-1):
            print(i,j)
            dev = A1[i,pos1[0]]
            A1[i,:] = A1[i,:]/dev
            print()
            mult = A1[j+1,i]
            print(mult)
            x = A1[j+1,:] - mult*A1[i,:]
            print(A1[j+1,:])
            print(mult*A1[i,:])
            A1[j+1,:] = x
            
            print(A1)
            
        A1 = sort(A1,m)
        print(A1)
    return A1
        
        

#create a random binary matrix with n by m, max. of n,m is 5
#A = np.random.randint(2,size = (np.random.randint(1,6),np.random.randint(1,6)))

A = np.array([[1,1,1,0],
              [1,1,1,0],
              [1,0,1,1],
              [0,1,1,0]])

print("The original matrix is")
print(A)
print()
print("The final matrix is")
print(gaussian(A))


