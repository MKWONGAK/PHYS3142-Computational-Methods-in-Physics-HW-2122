import numpy as np
import matplotlib.pyplot as plt

def f(r):
    g = 4
    L = 1
    f_theta = r[1]
    f_theta_dot = -g/L*np.sin(r[0]) #non-linear
    return np.array([f_theta,f_theta_dot])

#2nd order RK method
def RK(theta0, theta_dot0):
    #100 steps with 101 data points
    h = 5*np.pi/100
    theta = [theta0]
    r = np.array([theta0,theta_dot0])
    for i in range(100):
        k1 = h*f(r)
        k2 = h*f(r+1/2*k1)
        r = r + k2
        theta.append(r[0])
    return theta

def sol(theta0,t):
    g = 4
    L = 1
    Tl = 2*np.pi*np.sqrt(L/g)
    theta = theta0*np.cos(2*np.pi*t/Tl)
    return theta


t = np.linspace(0,5*np.pi,101)
    
RK_sol = RK(0.7,0)
linear_sol = sol(0.7,t)

plt.plot(t,RK_sol,label = "2nd RK")
plt.plot(t,linear_sol,label = "linear")
plt.xlabel("t")
plt.ylabel("theta")
plt.legend(loc = 1)
plt.show()

