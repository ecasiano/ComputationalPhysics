#!/usr/bin/env python

#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt

#Parameters
c = 300
dx = 0.01
dt = dx/c

r = c*(dt/dx)

#Set initial string profile
L = 1                      #String Length (meters)
M = 1500                    #Number of spatial subdivisions
x = np.linspace(0,L,M)      #Positions across string length
x0 = 0.5                   #Pluck Center
k = 1000					#Parameter that opens or contracts Gaussian Pluck
y0 = np.exp(-k*(x-x0)**2)	#Initial Profile of String (A Gaussian) 


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

N = 11000                     #Total time steps

image_num = 0
for n in range(0,N) : 
    for i in range(1,M-1): #Stops at i =  M - 2 (998), y = 0 at i = 0 and i = M - 1

        y[2,i] = 2*(1-r**2)*y[1,i] - y[0,i] + r**2*(y[1,i+1] + y[1,i-1])
    
    if n % 50 == 0:
        # create filename
        filename = './OUTPUT/image_%06i.png' % image_num
        # iterate image_num
        image_num += 1
        #save pictures at different times
        plt.plot(x,y[2,])
        secs = '%.6f'%(n*dt)
        plt.title('Gaussian Pluck    t='+secs+' s')
        plt.ylim(-1.1,1.1)
        # plt.draw()
        # plt.pause(1E-10)
        plt.savefig(filename)
        plt.clf()

    #Delete n=0; shift n=1->n=0 and n=2->n=1
    y[0,] = y[1,]
    y[1,] = y[2,]

    
