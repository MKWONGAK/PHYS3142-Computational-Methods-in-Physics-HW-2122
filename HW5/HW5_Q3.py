import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,0.5,200)
#from lecture note
VE = ((162+1816*a)/21728 -(8+1594*a)/21720)*21728/(162+1816*a)

#plot the graph
plt.title("The Plot of VE vesus alpha")
plt.xlabel("alpha")
plt.ylabel("VE")
plt.plot(a,VE)
plt.show()