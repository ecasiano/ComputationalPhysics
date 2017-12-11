#Emanuel Casiano-Diaz
#G & N Problem 3.13

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g, pi

def drivenPendulum(q, theta0, fD):
    
    dt = 0.04 #s
    
    #initial conditions
    omega0 = 0.0        #iniital angular velocity
    l = g               #string length
    m = 1.0             #pendulum mass
    omegaD = 2/3        #angular frequency

    #arrays that will store pertinent values
    timesList = np.arange(0,50+dt,dt)           #Times
    omegasList = np.zeros_like(timesList)       #Angular velocities
    thetasList = np.zeros_like(timesList)       #Angles

    omegasList[0] = omega0
    thetasList[0] = theta0
    
    for n,t in enumerate(timesList[1:]):
        
        omegasList[n+1] = omegasList[n] - (g/l)*np.sin(thetasList[n])*dt - q*omegasList[n]*dt + fD * np.sin(omegaD*timesList[n])*dt
        thetasList[n+1] = thetasList[n] + omegasList[n+1] * dt

        if(thetasList[n+1] < -1.0*pi):
            thetasList[n+1] = thetasList[n+1] + 2*pi

        if(thetasList[n+1] > 1.0*pi):
            thetasList[n+1] = thetasList[n+1] - 2*pi

    return(timesList, thetasList)

def main():
    
    q = 0.5
    fD = 0.5
    
    times = drivenPendulum(q, 0.000, fD)[0]

    thetas1 = drivenPendulum(q, 0.001, fD)[1]
    thetas2 = drivenPendulum(q, 0.000, fD)[1]

    test = drivenPendulum(q,0.2,fD)[1]
    divergence = (abs(thetas1-thetas2))

    #Plot
    plt.plot(times,divergence, label=r'$F_{D}$ = %.1f' % fD)
    plt.title(r'$\Delta \theta vs. Time$')
    plt.legend(loc='best')
    plt.xlabel('time(s)')
    plt.ylabel(r'$\Delta \theta$ (radians)')
    plt.yscale('log')
    plt.savefig('dthetaVtimeLowDrive.png')
    plt.show()

    #Find Lyapunov exponent
    lyapunovList = np.zeros_like(times)
    for n, t in enumerate(times[1:]):
        lyapunovList[n] = np.log(divergence[n])/(t)

    lyapunov =np.log(-1*(np.mean(lyapunovList))) * (-1)

    print('Lyapunov exponent is: %.2f' % lyapunov)

if __name__ == '__main__':
    main()

