# filename: radioactive-decay.py
# author: Adrian Del Maestro
# date: 09.13.2011

# Use the Euler method to iteratively solve a first order differential equation
# describing the decay of 235-Uranium and compare with the exact solution

import matplotlib.pyplot as plt
import numpy as np

# main program
def main():
 
    initialTimeStep = 0.0001                                                     #Smallest time step we want to evaluate
    finalTimeStep = 0.1                                                          #Largest time step we want to evaluate
    stepSize = 0.0001                                            
    errorTime = 5                                                              #Time at which we want to evaluate the error as a function of step size
    
    dtList = np.arange(initialTimeStep, finalTimeStep + stepSize, stepSize)      #Generates an array dt = {dt_0, 2*dt_0, 3*dt_0, ... , finalTimeStep}
    errorList = np.zeros_like(dtList)
    ctr = 0
    
    #Iterates the code for every time step in dtList
    for dt in dtList:


        # define and initialize 
        dt  = 0.05  # in units of tau
        t = np.arange(0.0,errorTime,dt)
        num_steps = t.size
        N_euler = np.zeros_like(t) # in units of N_0)
        N_euler[0] = 1
        N_RK = np.zeros_like(t)
        N_RK[0] = 1

        # get the iterative Euler solution
        for n in range(1,len(t)):
            N_euler[n] = (1.0-dt)*N_euler[n-1]

        #Runge-Kutta Solution
        
            N_RK[n] = N_euler[n]*(1 - dt + 0.5*dt**2)
        
        #Analytic solution
        N_analytic = N_euler[0]*np.exp(-t)
        
        #Error
        errorList[ctr] = abs((N_analytic[-1] - N_RK[-1])/N_analytic[-1])*100     #[-1] index to evaluate error at end of array (a.k.a at errorTime)
        ctr += 1

   
    # plot the Runge-Kutta solution
    plt.plot(t,N_RK, marker='*', label='RungeKutta')

    # plot the analytical solution
    anLab = r'$N_0\mathrm{e}^{-t/\tau}$'
    plt.plot(t,N_euler[0]*np.exp(-t),linestyle='-',marker='None', color='black',
           linewidth=1.5, label=anLab)
    plt.xlabel(r'$t/\tau$')
    plt.ylabel(r'$N(t)/N_0$')
    plt.legend()
    plt.title('Runge-Kutta solution for radioactive decay')
    plt.show()
    
    #plot Runge-Kutta error vs time step
    plt.plot(dtList, errorList)
    plt.xscale('log')
    plt.xlabel(r'TimeStep[$\frac{\Delta t}{\tau}$]')
    plt.ylabel('Error (%)')
    plt.title('Runge-Kutta Error vs TimeStep @ t = %.d' % (errorTime))
    plt.xlim(initialTimeStep/10 , finalTimeStep*10)
    plt.savefig('rkDecayError_t_%.d.png' % (errorTime))
    plt.show()

if __name__ == '__main__':
    main()
