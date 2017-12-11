#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt

#Parameters
c = 300
dx = 0.01
dt = dx/c

r = c*(dt/dx)

#Set initial string profile
L = 3*np.pi                     #String Length (meters)
M = 1500                    #Number of spatial subdivisions
x = np.linspace(0,L,M)      #Positions across string length
x0 = 0.5                  #Pluck Center
#k = 1000					#Parameter that opens or contracts Gaussian Pluck
#y0 = np.exp(-k*(x-x0)**2)	#Initial Profile of String (A Gaussian) 

y0_1 = np.zeros_like(x)
y0_1 = np.sin(x) 

y0_2 = np.zeros_like(x)
y0_2 = np.sin(2*x) 

y0_3 = np.zeros_like(x)
y0_3 = np.sin(3*x) 

y0_4 = np.zeros_like(x)
y0_4 = np.sin(4*x) 


plt.plot(x,y0_1)
plt.plot(x,y0_2)
plt.plot(x,y0_3)
plt.plot(x,y0_4)
plt.show()

#Create 2D Array to fill in with string profiles
y1 = np.zeros([3,np.size(x)])     #Three rows of spatial values

y1[0,] = y0_1
y1[1,] = y0_1

y2 = np.zeros([3,np.size(x)])     #Three rows of spatial values

y2[0,] = y0_2
y2[1,] = y0_2

y3 = np.zeros([3,np.size(x)])     #Three rows of spatial values

y3[0,] = y0_3
y3[1,] = y0_3

y4 = np.zeros([3,np.size(x)])     #Three rows of spatial values

y4[0,] = y0_4
y4[1,] = y0_4

#Set endpoints specifically to zero
y1[0,0] = y0_1[0]
y1[0,-1] = y0_1[-1]
y1[1,0] = y0_1[0]
y1[1,-1] = y0_1[-1]
y1[2,0] = y0_1[0]
y1[2,-1] = y0_1[-1]

y2[0,0] = y0_1[0]
y2[0,-1] = y0_1[-1]
y2[1,0] = y0_1[0]
y2[1,-1] = y0_1[-1]
y2[2,0] = y0_1[0]
y2[2,-1] = y0_1[-1]

y3[0,0] = y0_1[0]
y3[0,-1] = y0_1[-1]
y3[1,0] = y0_1[0]
y3[1,-1] = y0_1[-1]
y3[2,0] = y0_1[0]
y3[2,-1] = y0_1[-1]

y4[0,0] = y0_1[0]
y4[0,-1] = y0_1[-1]
y4[1,0] = y0_1[0]
y4[1,-1] = y0_1[-1]
y4[2,0] = y0_1[0]
y4[2,-1] = y0_1[-1]

N = 10100                     #Total time steps
for n in range(2,N) :
    for i in range(1,M-1): #Stops at i =  M - 2 (998), y = 0 at i = 0 and i = M - 1

        y1[2,i] = 2*(1-r**2)*y1[1,i] - y1[0,i] + r**2*(y1[1,i+1] + y1[1,i-1])
        y2[2,i] = 2*(1-r**2)*y2[1,i] - y2[0,i] + r**2*(y2[1,i+1] + y2[1,i-1])
        y3[2,i] = 2*(1-r**2)*y3[1,i] - y3[0,i] + r**2*(y3[1,i+1] + y3[1,i-1])
        y4[2,i] = 2*(1-r**2)*y4[1,i] - y4[0,i] + r**2*(y4[1,i+1] + y4[1,i-1])
    
    if n % 5 == 0:
        #save pictures at different times
        plt.plot(x,y1[2,])
        plt.plot(x,y2[2,])
        plt.plot(x,y3[2,])
        plt.plot(x,y4[2,])
        secs = '%.6f'%(n*dt)
        plt.title('Plucked String    t='+secs+' s')
        plt.ylim(-1.1,1.1)
        plt.draw()
        plt.pause(1E-10)
        plt.clf()

    #Delete n=0; shift n=1->n=0 and n=2->n=1
    y1[0,] = y1[1,]
    y1[1,] = y1[2,]

    y2[0,] = y2[1,]
    y2[1,] = y2[2,]

    y3[0,] = y3[1,]
    y3[1,] = y3[2,]
    
    y4[0,] = y4[1,]
    y4[1,] = y4[2,]
