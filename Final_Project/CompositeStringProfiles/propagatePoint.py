#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

#Parameters
c = 300         #m/s
dx = 0.01       #m  
dt = dx/c       #s

r = c*(dt/dx)

#Set initial string profile
L = 1                      #String Length (meters)
M = 1000                    #Number of spatial subdivisions
x = np.linspace(0,L,M)      #Positions across string length
x0 = 0.5                   #Pluck Center (fraction from one end)
k = 1000					#Parameter that opens or contracts Gaussian Pluck
y0 = np.exp(-k*(x-x0)**2)	#Initial Profile of String (A Gaussian) 
pluckIdx = 50               #50 -> 5% of our string

#Create 2D Array to fill in with string profiles
y = np.zeros([3,np.size(x)])     #Three rows of spatial values

y[0,] = y0
y[1,] = y0

#Set endpoints specifically to zero
y[0,0] = y0[0]
y[0,-1] = y0[-1]
y[1,0] = y0[0]
y[1,-1] = y0[-1]
y[2,0] = y0[0]
y[2,-1] = y0[-1]

#TESTING (IGNORE FOLLOWING 4 LINES)
#print(y0[0])
#print(y0[1])
#plt.plot(x,y0)
#plt.show()


N = 10100                     #Total time steps
point = np.array([])
time = np.array([])

point = np.zeros(N-2)
time = np.zeros(N-2)
for n in range(2,N):

    for i in range(1,M-1): #Stops at i =  M - 2 (998), y = 0 at i = 0 and i = M - 1

        y[2,i] = 2*(1-r**2)*y[1,i] - y[0,i] + r**2*(y[1,i+1] + y[1,i-1])
    
    
    point[n-2] =y[2,pluckIdx]
    time[n-2] = n*dt*0.1

    y[0,] = y[1,]
    y[1,] = y[2,]

plt.plot(time,point)
plt.title('String signal versus time')
plt.xlabel('Time (s)')
plt.ylabel('Signal (arbs)')
plt.show()

sd.play(point)

#Compute Power Spectrum

powerSpectrum = np.abs(np.fft.fft(point))**2
freqs = np.fft.fftfreq(time.size,time[1]-time[0])
idx = np.argsort(freqs)

plt.plot(freqs[idx],powerSpectrum[idx])
plt.title('Power Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power (arbs)')
plt.xlim(0,3000)
#plt.ylim(0,2)

plt.show()
