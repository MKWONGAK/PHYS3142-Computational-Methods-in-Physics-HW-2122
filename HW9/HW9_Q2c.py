import numpy as np


def f(x):
    y = x**5/(np.exp(x)-1)
    return y

x1 = 0.1
x4 = 20
z = (1+np.sqrt(5))/2

i = 0
x2 = x4-(x4-x1)/z
x3 = x1+(x4-x1)/z

e = x4 - x1
while e> 10**(-6):
    y1 = f(x1)
    y2 = f(x2)
    y3 = f(x3)
    y4 = f(x4)
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

    else:
        print("no peak")


print("Iteration",i)
print((x4+x1)/2)
            



