import numpy as np
import matplotlib.pyplot as plt
import xraydb


plt.close('all')

Material='Fe'
Energy=20000  # in eV
Density = 7.874 # denisty in g/cm3
# show mu value
mu=xraydb.material_mu(Material,Energy)
print('mu (cm-1)', mu)
print('mu/rho (cm2/g)', mu/Density)

# compute transmission for a specific thickness using Beer Lambert Law
t=0.1 # in cm
transmission=np.exp(-mu*t)
print(transmission)


# compute transmission for a specific thickness using Beer Lambert Law for various energies
Material='Fe'
Emin=10000.0
Emax=100000.0
Estep = 1000.0
Energy_range=np.arange (Emin,Emax,Estep)
mu=np.zeros(len(Energy_range))
trans=np.zeros(len(Energy_range))
cpt=0
for Energy_val in Energy_range:
    val=xraydb.material_mu(Material,Energy_val)
    mu[cpt]=val
    cpt=cpt+1

# plot absorption coefficient vs energy
plt.figure(1)
plt.loglog(Energy_range,mu,'r-')
plt.xlabel('Energy in eV')
plt.ylabel('Absorption coefficient in cm-1')
title='Material = %s' %(Material)
plt.title(title)

# plot transmission coefficient vs energy
plt.figure(2)
thickness=0.1 # in cm
trans=np.exp(-mu*thickness)
plt.plot(Energy_range/1000,trans,'b-')   
plt.xlabel('Energy in keV')
plt.ylabel('transmission')
title='Material = %s / thickness = %0.4f cm' %(Material,t)
plt.title(title)
