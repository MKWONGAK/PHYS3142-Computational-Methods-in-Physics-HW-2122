import numpy as np
import matplotlib.pyplot as plt

def f(r):
    g = 4
    L = 1
    f_theta = r[1]
    f_theta_dot = -g/L*np.sin(r[0]) #nonlinear 
    return np.array([f_theta,f_theta_dot])

#total energy
def energy(theta,theta_dot,theta0):
    g = 4
    L = 1
    m = 1
    KE = 1/2*m*L**2*theta_dot**2
    PE = m*g*L*(np.cos(theta0)-np.cos(theta))
    return PE + KE


def RK_2(theta0, theta_dot0):
    #100 steps with 101 data points
    h = 5*np.pi/100
    r = np.array([theta0,theta_dot0])
    E = [energy(r[0],r[1],theta0)]
    for i in range(100):
        k1 = h*f(r)
        k2 = h*f(r+1/2*k1)
        r = r + k2
        E.append(energy(r[0],r[1],theta0))
    return E

def RK_4(theta0, theta_dot0):
    h = 5*np.pi/100
    r = np.array([theta0,theta_dot0])
    E = [energy(r[0],r[1],theta0)]
    for i in range(100):
        k1 = h*f(r)
        k2 = h*f(r+1/2*k1)
        k3 = h*f(r+1/2*k2)
        k4 = h*f(r+k3)
        r = r + 1/6*(k1+2*k2+2*k3+k4)
        E.append(energy(r[0],r[1],theta0))
    return E

theta0 = 1
theta_dot0 = 0

E_RK2 = RK_2(theta0, theta_dot0)
E_RK4 = RK_4(theta0, theta_dot0)

t = np.linspace(0,5*np.pi,101)

#2nd RK
plt.xlabel("t")
plt.ylabel("energy")
plt.plot(t,E_RK2,label = "2nd RK")
plt.legend()
plt.show()

#4th RK
plt.xlabel("t")
plt.ylabel("energy")
plt.plot(t,E_RK4,label = "4th RK")
plt.legend()
plt.show()

