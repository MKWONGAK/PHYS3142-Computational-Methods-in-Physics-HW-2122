import numpy as np
import time

#only one bullet in the gun

num_test = 20000000
num_pos = 20
pos_take = tuple(range(10))

start_time = time.time()
np.random.seed(10)
num_lose = 0
for nt in range(num_test):
    A = np.zeros(num_pos)
    A[np.random.randint(0,num_pos)] = 1
    
    for n in range(num_pos):
        if A[n] == 1:
            if n in pos_take:
                num_lose += 1
            break


print('The probability of losing is:', num_lose/num_test)
print('Time:', time.time() - start_time)
print('Number of tests:', num_test)