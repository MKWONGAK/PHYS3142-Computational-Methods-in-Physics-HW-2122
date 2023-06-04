import numpy as np
import matplotlib.pyplot as plt


def f(r,b): #r[0]:x r[1]:y r[2]:vx r[3]:vy
    g = 10
    fx = r[2]
    fy = r[3]
    fvx = -b*r[2]*np.sqrt(r[2]**2+r[3]**2)
    fvy = -g -b*r[3]*np.sqrt(r[2]**2+r[3]**2)
    return np.array([fx,fy,fvx,fvy])

def RK(theta0,b):
    v0 = 200
    h = 0.1
    vx0 = v0*np.cos(theta0)
    vy0 = v0*np.sin(theta0)
    x = [0]
    y = [0]
    i = 1
    r = np.array([0,0,vx0,vy0])
    j = 0
    while i == 1:
        k1 = h*f(r,b)
        k2 = h*f(r+1/2*k1,b)
        k3 = h*f(r+1/2*k2,b)
        k4 = h*f(r+k3,b)
        r = r + 1/6*(k1+2*k2+2*k3+k4)
        x.append(r[0])
        y.append(r[1])
        j += 1
        if (y[j-1]>=0) and (y[j]<0):
            i = 0
    return x,y

theta = np.linspace()

theta0 = np.pi/4
x_without,y_without = RK(theta0,0)
x_with,y_with = RK(theta0,0.0003)
print(max(x_with)-min(x_with))

plt.plot(x_without,y_without, label = "no resistance")
plt.plot(x_with,y_with, label = "with air resistance")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = 1)
plt.show()
