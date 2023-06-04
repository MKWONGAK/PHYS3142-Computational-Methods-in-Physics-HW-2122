# Hw1 Q1 arc length of a cycloid
import numpy as np
import matplotlib.pyplot as plt

#the given parameter and initial position
r = 1
w = 1
v_cm = r*w
theta = 0
x_cm = 0
y_cm = 1
#uniform sampling of time
delta_t = 2*np.pi/99
x = []
y = []

for i in range(100):
    #The positon of the point I tracing
    x.append(x_cm + r*np.sin(theta))
    y.append(y_cm - r*np.cos(theta))
    x_cm += v_cm*delta_t
    theta += -w*delta_t

arc_length = 0
#approximation the arc_length
for i in range(1,100):
    arc_length += np.sqrt((x[i]-x[i-1])**2 + (y[i]-y[i-1])**2)

print('The arc length of a cycloid approximately equal to',arc_length)

#adjust the plot appearance
plt.figure(figsize=(7,2), dpi =800)
plt.xticks(np.linspace(0,7,8, endpoint = True))
plt.yticks(np.linspace(0,2,5, endpoint = True))
plt.xlim(-0.1,6.4)
plt.ylim(0,2.1)
plt.xlabel('x(r)')
plt.ylabel('y(r)')

#plot the x,y
plt.scatter(x,y,1)
plt.show()


