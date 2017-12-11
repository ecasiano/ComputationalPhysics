#Emanuel Casiano-Diaz (Last modified on 10/14/16.)
#Based on code written in PHYS256 by A. Del Maestro

# Plots the error between Euler Method and exact solution of
# the ODE for radioactive decay as a function of the time step

#NOTE: The error will be evaluated at a single time, defined as errorTime

import numpy as np
import matplotlib.pyplot as plt

# main program
def main():
    
    initialTimeStep = 0.0001                                                     #Smallest time step we want to evaluate
    finalTimeStep = 0.1                                                          #Largest time step we want to evaluate
    stepSize = 0.0001     
    errorTime = 5                                                                #Time at which we want to evaluate the error as a function of step size

    dtList = np.arange(initialTimeStep, finalTimeStep + stepSize, stepSize)      #Generates an array dt = {dt_0, 2*dt_0, 3*dt_0, ... , finalTimeStep}
    errorList = np.zeros_like(dtList)                                             
    ctr = 0
   
    #Iterates the code written in class for every time step in dtList
    for dt in dtList:

        # define and initialize 
        t = np.arange(0.0, errorTime ,dt)
        num_steps = t.size
        N_euler = np.zeros_like(t) # in units of N_0)
        N_euler[0] = 1

        # get the iterative Euler solution
        for n in range(1,len(t)):
            N_euler[n] = (1.0-dt)*N_euler[n-1]
        
        # Analytical Solution 
        N_analytic = N_euler[0]*np.exp(-t)

        #Error
        errorList[ctr] = abs((N_analytic[-1] - N_euler[-1])/N_analytic[-1])*100     #[-1] index to evaluate error at end of array (a.k.a at errorTime)
        ctr += 1
    
    #plot error vs timeStep

    plt.plot(dtList, errorList)
    plt.xscale('log')
    plt.xlabel(r'TimeStep[$\frac{\Delta t}{\tau}$]')
    plt.ylabel('Error (%)')
    plt.title('Euler Error vs TimeStep @ t = %.d' % (errorTime))
    plt.xlim(initialTimeStep/10 , finalTimeStep*10)
    plt.savefig('eulerDecayError_t_%.d.png' % (errorTime))
    plt.show()

if __name__ == '__main__':
    main()
