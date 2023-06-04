import numpy as np


# sampling the volume
def sample(N):
    x = 2*R1*np.random.random(size=N) -R1
    y = 2*R1*np.random.random(size=N) -R1
    z = 2*R1*np.random.random(size=N) -R1
    
    sphere = x**2 + y**2 + z**2
    cylinder = (x-1/2)**2 + y**2
    
    tmp = 0
    for i in range(N):
        if (sphere[i] <= R1**2) and (cylinder[i] <= R2**2):
            tmp += 1
    
    return V*tmp/N

R1 = 1
R2 = 1/2
V = (2*R1)**3
N = 5000
Run_time = 1000

#repeat the sampling 
volume = []
for i in range(Run_time):
    volume.append(sample(N))

volume = np.array(volume)

#calculate the value
mean = np.sum(volume)/Run_time
SD = np.sqrt(np.sum((volume-mean)**2/(Run_time-1)))
SD_error = SD/np.sqrt(Run_time)

print("The mean is", mean)
print("The SD is", SD)
print("The SD error is", SD_error)




