import matplotlib.pyplot as plt
import numpy as np

M = 10**5
N = np.array(range(1,10**4 + 1))
zeta_M = 0
zeta_N = []

#sum the first M terms and store the first 10**4 to the zeta_N
for n in range(M):
    zeta_M += 1/(n+1)**3
    if n < 10**4:
        zeta_N.append(zeta_M)
#change the data type to array 
#and calculate the error for each N in the range.
zeta_N = np.array(zeta_N)
error = zeta_M - zeta_N

#plot the graph
plt.xlabel('N')
plt.ylabel('error')
plt.semilogy(N,error,base=10)
plt.show()