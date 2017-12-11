#Use Euler Method to solve the radioactive decay problem

import numpy as np
import matplotlib.pyplot as plt

def main():

    dt = 1.0/4
    t = np.arange(0.0,5,dt)
    num_steps = t.size
    N = np.zeros_like(t)
    N[0] = 1

    for n in range(1,len(t)):
        N[n] = (1.0-dt)*N[n-1]

    #Plot the numerical solution
    numLab = r' $\Delta t = %3.2f \tau$' % dt
    plt.plot(t, N, linestyle='None',marker='o', markersize=6, label=numLab)

    #Plot the analytical solution
    anLab = r' $N_0 \mathrm{e}^{-t/\tau}$'
    plt.plot(t, N[0]*np.exp(-t), linestyle='-', marker='None', color='black',
            linewidth=1.5, label=anLab)
    plt.xlabel(r'$t/\tau$')
    plt.ylabel(r'$N(t)/\N_0$')

    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()

