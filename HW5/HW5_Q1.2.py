from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np


#calculate the gaussian distribution
def Gaussian(mean, SD):
    x = np.linspace(0.6,1.2,50)
    dist = np.exp(-(x-mean)**2/(2*SD**2))/np.sqrt(2*np.pi*SD**2)
    return dist, x


g, size = 0.9, 400
student = 5000
array = []
#creating the array contain all student result of mean value
for i in range(student):
    array.append(np.sum(poisson.rvs(mu = g, size = size ))/size)

mean = np.sum(array)/5000
SD = np.sqrt(np.sum((np.array(array)-mean)**2/(student-1)))
SD_error = SD/np.sqrt(student)

dist, x = Gaussian(mean, SD)

#plot the graph
fig, axes= plt.subplots(dpi=100)
axes.set_xlabel("mean value of g")
axes.set_ylabel("density")
plt.title("Distribution of Sample Mean Values")
plt.xticks(np.arange(6,13)/10)
hist_bins, bins, patches = plt.hist(array, 
                                    bins = (np.linspace(0.58,1.22,33)+0.01),
                                    density = True, label = 'mean value distribution')
plt.plot(x, dist, "--", color="red",label = "Gaussian formula")
axes.legend(loc = 0)

print("The mean, standard deviation, and standard error are", mean,"," ,SD,",and", SD_error)