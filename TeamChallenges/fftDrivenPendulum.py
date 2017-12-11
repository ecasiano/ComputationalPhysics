
from scipy.constants import g
from scipy.constants import pi

def fast_fourier_transform(t,y):
    '''Return the fast Fourier transform of y.'''
    yHat = np.fft.fft(y)
    fftOmega = 2*pi*np.fft.fftfreq(t.size,t[1]-t[0])
    return fftOmega,yHat

def euler(t,FD,l,theta0,omega0,gamma,omegaD):
    ''' Semi-implicit Euler Method for the non-linear, dissipative, driven pendulum.'''
    
    dt = t[1]-t[0]
    omegasList,thetasList = np.zeros_like(t),np.zeros_like(t)
    thetasList[0],omegasList[0] = theta0,omega0
    
    # perform the numerical integration
    for n in range(t.size-1):
        omegasList[n+1] = omegasList[n] + (-(g/l)*np.sin(thetasList[n]) - gamma*omegasList[n] + FD*np.sin(omegaD*t[n]))*dt
        thetasList[n+1] = thetasList[n] + omegasList[n+1]*dt
        
        # keep theta in [-pi,pi)
        if thetasList[n+1] < -pi: thetasList[n+1] += 2.0*pi
        if thetasList[n+1] >= pi: thetasList[n+1] -= 2.0*pi

return thetasList,omegasList

params = l,theta0,omega0,gamma,omegaD = g, 0.2, 0.0, 0.5, 2.0/3.0
FD = [0.5,1.2]
dt = 0.01

# We determine the maximum time such that N = 2*n
N = int(2**(np.ceil(np.log2(int(200.0/dt)))))
t = np.arange(0.0,N*dt,dt)
