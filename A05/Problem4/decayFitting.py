#Emanuel Casiano-Diaz

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def N_theory(t, N0, tau):
   #From data
    return N0 * np.exp(-t/tau)

#Perform the fit
data = np.loadtxt('decay.dat')

times = data[:,0] 
N = data[:,1]
uncertainties = data[:,2]

a, acov = curve_fit(N_theory, times, N, sigma=uncertainties, p0=(1,1))

#Plot
plt.figure()
plt.errorbar(times, N, yerr=uncertainties, marker='o', color='k', linestyle='none', label='OriginalData')
plt.plot(times, N_theory(times, *a), 'r-',  label=r'$N_{0}e^{-t/\tau}$')
plt.legend(loc='best')
plt.title('Decay Rate vs Time')
plt.xlabel('Time (s)')
plt.ylabel('DecayRate(Bq)')
plt.plot()
plt.savefig('decayFitting.png')
plt.show()

#Fit values
a_err = np.sqrt(np.diag(acov))
print('N0 (Initial Decay Rate) = %8.2E +- %7.1E Bq' % (a[0], a_err[0]))
print('Tau (Half-Life) = %8.2E +- %7.1E seconds' % (a[1], a_err[1]))

#Guess of nucleus
print('960 seconds --> 16 min. The nucleus may be Iridium-182 which has a half-life of 15 minutes.')

