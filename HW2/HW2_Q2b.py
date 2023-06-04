#Q2 Cross section of atomic orbitals

import numpy as np
import matplotlib.pyplot as plt

#find out the wavefunciton of 2px
def wavefunction_2px(x,y,z):
    r = x**2 + y**2 +z**2
    if r == 0:
        return 0
    a0 = 0.5
    R21 = (r/a0)*np.exp(-r/(2*a0))
    px = x/r
    return px*R21

#find out the wavefunciton of 3dxy
def wavefunction_3dxy(x,y,z):
    r = x**2 + y**2 + z**2
    if r == 0:
        return 0
    a0 = 0.5
    R32 = ((r/a0)**2)*np.exp(-r/(3*a0))
    dxy = x*y/r
    return dxy*R32

#plot the two graph
i=0
while i<2:
    min_ = -4; max_ = 4
    a = 100 # number of x/y for each y/x
    step = (max_ - min_)/(a-1)
    #create 100x100 array with all zero
    x_2d = np.zeros([a,a],float); y_2d = np.zeros([a,a],float); color = np.zeros([a,a],float)
    #inputing the x and y and corresponding wavefunction
    for x in range(a):
        for y in range(a):
            x_2d[x,y] = min_ + x*step
            y_2d[x,y] = min_ + y*step
            if i == 0: 
                color[x,y] = wavefunction_2px(x_2d[x,y],y_2d[x,y],0)
            else:
                color[x,y] = wavefunction_3dxy(x_2d[x,y],y_2d[x,y],0)
    #plot the x_2d,y_2d with pseudocolor plot with colormap 'bwr'
    plt.subplot(1,2,i+1)
    plt.pcolor(x_2d,y_2d,color, cmap ='bwr')
    print(color[0][0])
    
    #set the appearence and label
    plt.axis('square')
    plt.xlabel('x'); plt.ylabel('y')
    if i == 0: plt.title('2px(a0=0.5)') 
    else: plt.title('3dxy(a0=0.5)')
    plt.axis([-4,4,-4,4])
    i+=1

plt.show()
        