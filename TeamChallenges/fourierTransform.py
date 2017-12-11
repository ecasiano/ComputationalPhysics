#Emanuel Casiano-Diaz

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi

def fourierTransform(y):

    'Return discrete Fourier transform of y'

    N = np.size(y)
    yHat = np.zeros([N], dtype=complex)
   # yHat1 = np.zeros([N], dtype=complex)

#    for k in range(N):
 #       for j in range(N):
  #          yHat[k] += y[j]*np.exp(-complex(0,1)*2*pi*j*k/N)

#OR

    for k in range(N):
        yHat[k] = np.sum(y*np.exp(-complex(0,1)*2*pi*np.arange(N)*k/N))

    return yHat

def main():
    
    dt = 0.01
    t = np.arange(0.0, 50.0, dt)
    N = np.size(t)
    omega0 = 2.0*pi*(0.2)
    phi = 0
    y = np.sin(omega0*t + phi)
    
    yHats = fourierTransform(y)

    print(yHats)


if __name__ == '__main__':
    main()


