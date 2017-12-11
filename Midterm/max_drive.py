# Midterm
# File: max_drive.py

# Author: 
# Date: 10/21/2016

# Determine the optimal value of backspin omega to maximize a golfball's
# range.

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import g
from scipy.constants import pi as π

# --------------------------------------------------------------------
def C(v):
    '''The drag coefficient at velocity v. '''

    ##################
    # INSERT CODE HERE
    ##################

    if v < 14:
         return 0.5
    else :
        return 7.0/v

# --------------------------------------------------------------------
def ρ(y):
    '''The density of the atmosphere at height y in m above the ground. '''
    rho_0 = 1.225 # kg/m^3
    T0 = 288 # K
    a = 6.5E-3 # K/m

    ##################
    # INSERT CODE HERE
    ##################

    return rho_0*(1-(a*y)/T0)**(5/2)
# --------------------------------------------------------------------
def trajectory(omega ):
    ''' Return the x and y trajectory for a golf ball using the Euler-Cromer
        method for backspin omega. '''

    dt = 0.01 # s

    # golf ball details
    m = 45.93E-3        # kg
    D = 42.67E-3        # m
    S0 = 3.828E-5       # kg

    # initial conditions
    θ0 = np.radians(9.0)
    v0 = 72.0 # m/s
    x = np.array([0.0])     
    y = np.array([2.5E-2])

    ##################
    # INSERT CODE HERE
    ##################
    vx,vy,vz = 0,0,0 
    x = np.array([0.0])
    y = np.array([0.025])
    z = np.array([0.0])
    while y >= 0:
        v = np.sqrt(vx**2+vy**2+vz**2)
        vx -= C(v)/m*v*vx*dt
        vy -= -g*dt
        vz -= (S0/m)*omega*vx*dt
        x = np.append(x, x[-1] + vx*dt)
        y = np.append(x, x[-1] + vx*dt)
        z = np.append(x, x[-1] + vx*dt)
        
        return([x,y,z])

# --------------------------------------------------------------------
# main program
# --------------------------------------------------------------------
def main():

    omega_min= 0.0    # rad/s
    omega_max = 500.0 # rad/s
    d_omega = 0.5      # rad/s

    ##################
    # INSERT CODE HERE
    ##################

    backspinList = np.arange(omega_min,omega_max,d_omega)
    xFinalsList = []
    maxRange = 0
    for i in backspinList:
        xFinalsList.append(trajectory(i)[0][-1])

    maxRange = max(xFinalsList)
    xFinalsList = np.array(xFinalsList)

    maxIndex = np.where(xFinalsList == maxRange)

    print( trajectory(maxIndex))


    # Plot only positive y-values
    plt.plot(trajectory(maxIndex)[0], trajectory(maxIndex)[1])
    plt.title('Trajectory of golf ball')
    plt.xlabel('x(t), meters')
    plt.ylabel('y(t), meters')
    plt.axis(ymin=0.0)

    # Show the graph
    plt.show()

if __name__ == '__main__':
    main()
