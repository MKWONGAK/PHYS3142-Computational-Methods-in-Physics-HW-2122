#Monte Carlo simulations for 2D Ising model with grid N*N

import numpy as np
from pylab import plot,figure,errorbar,hist,subplot,title,xlabel,ylabel,legend
import time as time

# start time of calculation

#Hamiltonian
J=1
Latt_N = 4
Latt_M = 4
low_T=1
high_T=4
delta_T=0.2

#Monte Carlo setup
Nbins = 1000
Nsweep = 5

#prepare the initial state
latt=np.zeros([Latt_M,Latt_N])
for nx in range(Latt_M):
    for ny in range(Latt_N):
        latt[nx,ny]=np.sign(np.random.random()-0.5)

#get the energy difference after flipping the spin at (nx,ny)
def get_delta_E(nx,ny):
    nx1=np.mod(nx-1,Latt_M)
    nx2=np.mod(nx+1,Latt_M)
    ny1=np.mod(ny-1,Latt_N)
    ny2=np.mod(ny+1,Latt_N)
    delta_E=2*J*latt[nx,ny]*(latt[nx1,ny]+latt[nx2,ny]+latt[nx,ny1]+latt[nx,ny2])
    return delta_E

#calculate the auto-correlation
def auto_corr(data):
    data_tmp=np.array(data)
    N=data_tmp.size;
    Num_auto=int(0.1*N)
    
    if Num_auto>500:
        Num_auto=500
    
    data_tmp=data_tmp-sum(data_tmp)/N
    
    auto_corr = np.zeros(Num_auto)
    for ni in range(Num_auto):
        auto_corr[ni]=sum((data_tmp[0:N-ni])*(data_tmp[ni:N]))

    return auto_corr/auto_corr[0]


num_T=np.arange(low_T,high_T,delta_T).size
all_M=np.zeros([num_T,Nbins*Nsweep])
all_M_abs=np.zeros([num_T,Nbins*Nsweep])
aver_M=np.zeros(num_T)
aver_M_abs=np.zeros(num_T)
nT=0
for T in np.arange(low_T,high_T,delta_T):

    nt2=0
    start_time = time.time()
    for nb in range(Nbins):        
        for ns in range(Nsweep):
            
            for nl in range(Latt_N*Latt_M):
                nx=np.random.randint(Latt_M)
                ny=np.random.randint(Latt_N)
                delta_E=get_delta_E(nx,ny)
                if np.exp(-delta_E/T)>np.random.random():
                    latt[nx,ny] = - latt[nx,ny]
                    
            all_M[nT,nt2]=sum(sum(latt))/Latt_M/Latt_N
            all_M_abs[nT,nt2]=abs(all_M[nT,nt2])
            nt2 +=1
            
    aver_M[nT]=sum(all_M[nT,:])/Nbins/Nsweep
    aver_M_abs[nT]=sum(all_M_abs[nT,:])/Nbins/Nsweep
    nT+=1
    print("--- %s seconds ---" % (time.time() - start_time))

figure()
subplot(221)
title('Magnetization vs temperature')
plot(aver_M,np.arange(low_T,high_T,delta_T))
#plot(np.arange(low_T,high_T,delta_T),abs(aver_M),'bo',label='absolute value')
xlabel('Magnetization')
ylabel('temperature')
#legend()

subplot(223)
title('Absolute Magnetization vs temperature')
plot(aver_M_abs,np.arange(low_T,high_T,delta_T))
xlabel('Absolute Magnetization')
ylabel('temperature')

