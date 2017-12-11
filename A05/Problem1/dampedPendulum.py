#Emanuel Casiano-Diaz
#G & N Computational Physics Problem 3.6

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g

def pendulum(q):

    dt = 0.04 #s

    #initial conditions
    theta0 = 0.2        #radians
    omega0 = 0.0        #rads/secs
    l = 1.0             #m
    m = 1.0             #kg

    #arrays that will store pertinent values
    timesList = np.arange(0,10+dt,dt)           #Times
    omegasList = np.zeros_like(timesList)       #Angular velocities
    thetasList = np.zeros_like(timesList)       #Angles
    energiesList = np.zeros_like(timesList)     #Energies

    omegasList[0] = omega0
    thetasList[0] = theta0
    energiesList[0] = (1/2)*m*l**2*(omega0**2 + (g/l)*theta0**2) 
    

    for n,t in enumerate(timesList[1:]):

        omegasList[n+1] = omegasList[n] - (g/l)*thetasList[n]*dt - q*omegasList[n]*dt
        thetasList[n+1] = thetasList[n] + omegasList[n+1] * dt
        energiesList[n+1] = energiesList[n] + (1/2)*m*g*l*(omegasList[n]**2 + (g/l)*thetasList[n]**2)*(dt**2)
    
    return(timesList, thetasList, energiesList)

def main():

    underDamped = pendulum(1) 
    criticallyDamped = pendulum(5)  
    overDamped = pendulum(10)

    #Oscillations vs time plots
    plt.plot(underDamped[0], underDamped[1], label =  'UnderDamping')
    plt.plot(criticallyDamped[0], criticallyDamped[1], label = 'CriticalDamping')
    plt.plot(overDamped[0], overDamped[1], label = 'OverDamping')
    plt.legend()
    plt.title('Pendulum Oscillations vs Time')
    plt.ylabel('Oscillations (radians)')
    plt.xlabel('Time (s)')
    plt.savefig('oscillationsVtime.png')
    plt.show()
    
    #Energy vs time plots
    
    plt.plot(underDamped[0], underDamped[2], label =  'UnderDamping')
    plt.plot(criticallyDamped[0], criticallyDamped[2], label = 'CriticalDamping')
    plt.plot(overDamped[0], overDamped[2], label = 'OverDamping')
    plt.legend(loc='best')
    plt.title('Pendulum Energy vs Time')
    plt.ylabel('Energy (J)')
    plt.xlabel('Time (s)')
    plt.savefig('energiesVtime.png')
    plt.show()

    #Check where Under-Over Damping Boundary occurs (Numerically)
    qNum = 0

    thetas  = pendulum(qNum)[1]
    sortedThetas = np.sort(pendulum(qNum)[1])  #Sorts angles in ascending order
    sortedThetas = sortedThetas[::-1]       #Reverses to descending order
    
    while(np.array_equal(thetas, sortedThetas) == False):
        qNum += 0.01
        thetas  = pendulum(qNum)[1]
        sortedThetas = np.sort(pendulum(qNum)[1])  
        sortedThetas = sortedThetas[::-1]

    #Analytic Value
    m = 1.0
    l = 1.0
    qAna = 2*np.sqrt(m*(g/l))

    print('Critical Damping at %f (Numerically), %f (Analytically)' % (qNum, qAna))

    #Error

    error = abs(qAna-qNum)/qAna * 100 

    print('Error: %f %%' % (error))
if __name__ == '__main__':
    main()





