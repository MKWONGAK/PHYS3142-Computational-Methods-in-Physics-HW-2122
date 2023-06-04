import numpy as np


def f(r,b): #r[0]:x r[1]:y r[2]:vx r[3]:vy
    g = 10
    fx = r[2]
    fy = r[3]
    fvx = -b*r[2]*np.sqrt(r[2]**2+r[3]**2)
    fvy = -g -b*r[3]*np.sqrt(r[2]**2+r[3]**2)
    return np.array([fx,fy,fvx,fvy])

def RK(theta0):
    b = 0.0003
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
    return max(x) - min(x)

#my program for golden ratio from HW9
x1 = 0
x4 = np.pi/2
z = (1+np.sqrt(5))/2
i = 0
x2 = x4-(x4-x1)/z
x3 = x1+(x4-x1)/z
e = x4 - x1
while e> 10**(-6):
    y1 = RK(x1)
    y2 = RK(x2)
    y3 = RK(x3)
    y4 = RK(x4)
    if (y2>y1 and y2>y4) or (y3>y1 and y3>y4):
        if y2 >= y3:
            x4 = x3
            x3 = x2
            x2 = x4 -(x4-x1)/z 
        else:
            x1 = x2
            x2 = x3
            x3 = x1+(x4-x1)/z
        e = x4 - x1
        i+=1
print(i)
print("the launch angle is")
print((x4+x1)/2)

