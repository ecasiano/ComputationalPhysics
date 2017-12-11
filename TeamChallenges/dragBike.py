#

import matplotlib.pyplot as plt
import numpy as np

#Parameters

def main():
    
    #Parameters
    dt = 0.25
    m = 70
    A = 0.33
    rho = 1.2
    P = 400

    #the time array
    t = np.arange(0,100.0,dt)
    numSteps = t.size

    #the velocity array
    v = np.zeros_like(t)

    #initial velocity
    v[0] = 4.0

    #numerical integration ; C=0.5 (airDrag), C=0.0 (no airDrag)

    for C in [0.0,0.5]:
        for n in range(1,numSteps):
            v[n] = v[n-1] + P/(m*v[n-1])*dt - C*rho*A*v[n-1]**2*dt/(2.0*m)

        #plot the result
        plt.plot(t,v,'-',label=r'$C = %3.1f$' % C)

    #set the plot labels
    plt.xlabel('Time [s]')
    plt.ylabel('Velocity [m/s]')

    #draw the legend
    plt.legend(loc='lower right')

    #draw the graph to the screen
    plt.show()

if __name__== '__main__':
    main()






