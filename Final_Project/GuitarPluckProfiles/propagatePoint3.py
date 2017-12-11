#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt

#Parameters
c = 300
dx = 0.0065
dt = dx/c

r = c*(dt/dx)

#Set initial string profile
L = 0.65                       #String Length (meters)
M = 1500                    #Number of spatial subdivisions
x = np.linspace(0,L,M)      #Positions across string length
x0 = L/20                    #Pluck Center
h = 0.005                   #Initial Pluck Position

y0 = np.zeros_like(x)
pluckIdx = 75               #75 -> 5% of our string

#Creates a Triangular Profile
for j,t in enumerate(x):
    if(t<=x0): y0[j] = (h/x0)*t
    else: y0[j] = h*(L-t)/(L-x0)

#Plot initial profile
plt.plot(x,y0)
plt.title('Guitar Pluck')
plt.xlabel('x(m)')
plt.ylabel('y(mm)')
plt.show()

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

N = 10100                     #Total time steps
point = np.array([])
time = np.array([])

#Calculates the displacements at a single point
point = np.zeros(N-2)
time = np.zeros(N-2)
for n in range(2,N):

    for i in range(1,M-1): #Stops at i =  M - 2 (998), y = 0 at i = 0 and i = M - 1

        y[2,i] = 2*(1-r**2)*y[1,i] - y[0,i] + r**2*(y[1,i+1] + y[1,i-1])
    
    
    point[n-2] =y[2,pluckIdx]
    time[n-2] = n*dt*100

    y[0,] = y[1,]
    y[1,] = y[2,]

#Plots the motion of the chosen point
plt.plot(time,point)
plt.title('String signal versus time')
plt.xlabel('Time (ms)')
plt.ylabel('Signal (arbs)')
plt.savefig('guitarSignal (Close to bridge).png')
plt.show()

#Compute Power Spectrum

yHat = np.fft.fft(point)
freqs = np.fft.fftfreq(time.size,time[1]-time[0])
powerSpectrum = np.abs(yHat)**2
idx = np.argsort(freqs)


plt.plot(freqs,powerSpectrum)
plt.title('Power Spectrum')
plt.xlabel('Frequency (KHz)')
plt.ylabel('Power (arbs)')
plt.xlim(0,3)
#plt.savefig('guitarPower_0.2.png')
#plt.ylim(0,2)
plt.show()
