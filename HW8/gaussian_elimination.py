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

#row i - row j if below the first 1 of row i is 1
def gaussian(A):
    m = len(A[0,:])
    A1 = sort(A,m)
    row = 0
    for i in range(m):
        ypos = np.where(A1[:,i] != 0)[0]
        ypos1 = np.where(ypos>=row)[0]
        k = 0
        if len(ypos1) >0:
            div = A1[ypos[ypos1[0]],i]
            A1[ypos[ypos1[0]],:] = A1[ypos[ypos1[0]],:]/div
        if len(ypos1) >1:
            for j in ypos1:
                if k != 0:
                    mult = A1[ypos[j],i]
                    x = A1[ypos[j],:] - mult*A1[ypos[ypos1[0]],:]
                    A1[ypos[j],:] = x
                k +=1
        A1 = sort(A1,m)
        if len(ypos1) != 0:
            if len(ypos[ypos1[0]:]) != 0:
                row += 1
                
  
    return A1
           
def rank(A):
    rank_ = 0
    n = len(A[:,0])
    for i in range(n):
        pos = np.where(A[i,:]==1.)[0]
        if len(pos) == 0:
            break
        else:
            rank_ +=1
    return rank_
    
#create a random binary matrix with n by m, max. of n,m is 10
A = np.random.randint(2,size = (np.random.randint(1,10),np.random.randint(1,10)))

"""
#test matrix
A = np.array([[0,0,0],
              [0,0,0],
              [0,0,0],
              [0,0,0],
              [0,0,0]])
"""

A = A.astype(float)
A1 = gaussian(A)
rank_ = rank(A1)

print("The original matrix is")
print(A)
print()
print("The final matrix is")
print(A1)
print()
print("The rank is")
print(rank_)











