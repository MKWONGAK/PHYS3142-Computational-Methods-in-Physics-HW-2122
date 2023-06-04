import matplotlib.pyplot as plt
import numpy as np

rand1 = np.random.rand(10**6)
rand2 = (rand1*2)**2/4

# Plot the uniform histogram of 10**6 sampling points

plt.title("Unifrom random number")
hist_bins, bins, patches = plt.hist(rand1, 
                                    bins = np.linspace(np.min(rand1),np.max(rand1),501),
                                    density = True, label = 'sample points')
plt.show()
plt.title("Non-unifrom")
hist_bins, bins, patches = plt.hist(rand2, 
                                    bins = np.linspace(np.min(rand2),np.max(rand2),501),
                                    density = True, label = 'sample points')
plt.show()

