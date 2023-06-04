import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate

def function(x):
    return np.sqrt(np.sin(x))/x

def function2(x):
    return np.sqrt(np.sin(x)/x)

def p(x):
    return 1/np.sqrt(x)

def g(x):
    return function(x)/p(x)

#uniform sampling
def I_estimate(a,b):
    sampling = 100
    x = (b-a)*np.random.rand(sampling)
    I = (b-a)*np.sum(function(x))/sampling
    return I

#non-uniform sampling
def non_uniform(a,b):
    sampling = 100
    x = (b-a)*np.random.rand(sampling)
    rand1 = (x*2)**2/4
    I = 2*np.sum(function2(rand1))/sampling
    return I

#the Metropolis algorithm
def Metropolis(a,b):
    sampling = 50000
    x = (b-a)*np.random.rand(sampling)
    I = 2*np.sum(g(x))/100
    x_next = (b-a)*np.random.rand(sampling)
    T = p(x_next)/p(x)
    indice = np.where(T>1)
    T[indice] = np.ones(len(indice))
    condition = T>=np.random.rand(sampling)
    x = x_next*condition + x*(1-condition)
    return I

def estimate(case,title):
    I = []
    repeat = 50000
    #for different questions
    if case == 1:
        for i in range(repeat):
            I.append(I_estimate(0, 1))
    if case == 2:
        for i in range(repeat):
            I.append(non_uniform(0, 1)) 
    if case == 3:
        for i in range(100):
            a= Metropolis(0,1)
            I.append(a)
            
    I = np.array(I)   
    
    #calculate the value
    mean = np.sum(I)/repeat
    SD = np.sqrt(np.sum((I-mean)**2)/(repeat - 1))
    error = SD/10
    accurate_solution = scipy.integrate.quad(function,0,1)
    print("For " + title)
    print("The mean is", mean)
    print("The standard deviation is", SD)
    print("The standard error is", error)
    print("The true value is", accurate_solution[0])
    print("The error of the true value is", accurate_solution[1])
    
    if (mean + error> accurate_solution[0]) and (mean - error< accurate_solution[0]):
        print("The estimate is good")
    else:
        print("The estimate is bad")
    print()
    
    #plot the graph
    plt.subplots(dpi=100)
    plt.title(title)
    plt.xlim(mean - 2*SD, mean + 2*SD)
    hist_bins, bins, patches = plt.hist(I, 
                                        bins = np.linspace(np.min(I),np.max(I),501),
                                        density = True, label = 'sample points')
    y = np.max(hist_bins)
    plt.vlines(mean-error,0,y,colors = "grey")
    plt.vlines(mean+error,0,y,colors = "grey")
    plt.vlines(accurate_solution[0],0,y,colors = "red")
    plt.show()
    return error

a = estimate(1,"Uniform sampling")
b = estimate(2,"Non-uniform sampling")
c = estimate(3,"Metropolis algorithm")  

print("The ratio of the standard error between Q1a and Q1b is", a/b)
print("The ratio of the standard error between Q1a and Q1c is", a/c)
    

