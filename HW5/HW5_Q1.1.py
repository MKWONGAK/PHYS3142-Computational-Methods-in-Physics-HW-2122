from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
import scipy.special

#The poisson formula
def poisson_dist(g,size):
    l = np.array(range(size))
    P = np.exp(-g)*g**l/scipy.special.factorial(l)
    return P

g = 0.9
size = 30000
array = poisson.rvs(mu = g, size = size )
y = poisson_dist(g,8)

#plot the graphs
#simple
fig, axes= plt.subplots(dpi=100)
axes.set_xlabel("energy level")
axes.set_ylabel("probability")
plt.title("Poisson Distribution")
hist_bins, bins, patches = plt.hist(array, 
                                    bins = (np.arange(-1,8) +0.5),
                                    density = True, label = 'sample points')
#formula
plt.plot(range(0,8), y, "o", color="red",label = "Poisson formula")
axes.legend(loc = 0)

mean = np.sum(array)/size
print("The mean is", mean)
print("The difference is", mean - g)


