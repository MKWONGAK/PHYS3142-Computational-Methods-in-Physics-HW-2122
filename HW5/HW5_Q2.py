import matplotlib.pyplot as plt
import numpy as np


def Monte_Carlo(points,R):
    x = 2*np.random.random(size= points) -R
    y = 2*np.random.random(size= points) -R
    return x,y

points = 10000
times = 4000
R=1
pi = []

#ran monte carlo 4000 times
for i in range(times):
    x,y = Monte_Carlo(points,R)
    pi.append(4*R**2*np.count_nonzero((x**2 + y**2)<R**2)/points)

pi = np.array(pi)
#plot the graph
fig, axes= plt.subplots(dpi=100)
axes.set_xlabel("mean values")
axes.set_ylabel("density")
plt.title("Distribution of Sample Mean Values")
plt.xticks(np.linspace(3.1,3.2,11))
hist_bins, bins, patches = plt.hist(pi, 
                                    bins = (np.linspace(3.1,3.2,11)-0.01/2),
                                    density = True, label = 'mean value distribution')


#calculate the required value
mean = np.sum(pi)/times
SD = np.sqrt(np.sum((pi-mean)**2/(times-1)))
P = 1 - (np.count_nonzero((pi < (np.pi - SD))) + np.count_nonzero((pi > (np.pi + SD))))/4000

print("The mean is", mean)
print("The SD is", SD)
print("The probability to obtain pi within the +- SD is", P)
    


