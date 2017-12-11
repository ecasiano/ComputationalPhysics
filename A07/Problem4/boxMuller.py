#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi

def boxMuller(N):

    # our uniform random numbers
    x1 = np.random.random(N)
    x2 = np.random.random(N)

    # generate the Box-Muller values
    x = np.sqrt(-2.0*np.log(1-x1))*np.cos(2.0*pi*x2)
    y = np.sqrt(-2.0*np.log(1-x1))*np.sin(2.0*pi*x2)
   
    # combine them into 1 array
    r = np.hstack([x,y])
    
    return r

def main():
    
    N = 1000
    y = boxMuller(N)
   
    # plot white noise
    plt.plot(y,'b-')
    plt.title('White Noise using Box-Muller Random Numbers')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.savefig('whiteNoise.png')
    plt.show()

    # get FFT of y
    yhat = np.fft.fft(y)
    n = np.size(y)
    freq = np.fft.fftfreq(n)


    # plot Fourier Transform of r vs r
    plt.plot(abs(freq),yhat,'b-')
    plt.title('Power Spectrum of Box-Muller White Noise')
    plt.xlabel('frequency')
    plt.ylabel('$|\^{y(t)}|$')
    plt.savefig('whiteNoisePowerSpectrum.png')
    plt.show()
    
    

if __name__ == '__main__':
    main()



