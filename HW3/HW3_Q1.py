import numpy as np
import time

#only one bullet in the gun

num_test = 2000000
num_pos = 20
pos_take = 10

start_time = time.time()
np.random.seed(10)
num_lose = 0

#create a array of size num_test and element are random int from 0 to 19
x = np.random.randint(0,num_pos, size = num_test)
#use the np.count_nonzero to count the number of element of x<pos_take
num_lose = np.count_nonzero(x < pos_take)        


print('The probability of losing is:', num_lose/num_test)
print('Time:', time.time() - start_time)
print('Number of tests:', num_test)