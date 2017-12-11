#Emanuel Casiano-Diaz

'''
Construct a 100 ×2 numpy array containing 100 random sets of points
inside the unit square x ∈ [−1, 1], y ∈ [−1, 1]. You may find it useful
to lookup the instructions on the numpy.random methods. Using array
operations, convert these cartesian coordinates to polar coordinates
and make two plots, highlighting both cartesian and polar axes.
'''

import numpy as np
import matplotlib.pyplot as plt

#Generates n random cartesian coordinates in -1<=x<=1 , -1<=y<=1

def generateCartesian(n):

    cartCoords = np.random.uniform(-1,1,(n,2))

    return cartCoords

#Takes the nx2 array of Cartesian coords and returns the nx2 array of Polar coords

def cartesian2Polar(xy):

    numberOfPoints = xy[:,0].size

    xList = np.reshape(xy[:,0], (numberOfPoints,1))
    yList = np.reshape(xy[:,1], (numberOfPoints,1))

    r = np.sqrt(xList**2 + yList**2)
   
    thetas = np.degrees(np.arctan2(yList,xList))
    polarCoords = np.column_stack((r,thetas))

    return polarCoords

def cart2PolarPlot(cartesian, polar):

    numberOfPoints = cartesian[:,0].size

    xList = np.reshape(cartesian[:,0], (numberOfPoints,1))
    yList = np.reshape(cartesian[:,1], (numberOfPoints,1))
   
    rList = np.reshape(polar[:,0], (numberOfPoints,1))
    thetaList = np.reshape(polar[:,1], (numberOfPoints,1))
   
    plt.figure()

    #Cartesian Plot
    plt.plot(xList, yList, 'bo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cartesian')
    plt.savefig('cartesian.png')
    plt.show() 

    #Polar Plot
    plt.axes(polar=True)
    plt.plot(thetaList,rList, 'bo')
    plt.title('Polar')
    plt.savefig('polar.png')
    plt.show()

    plt.axes()
def main():
    
    cartesian = generateCartesian(100)
    polar = cartesian2Polar(cartesian)

    print('Cartesian (x, y)')
    print(cartesian) #100X2 np.array of random cartesian coordinates

    print('\n')

    print('Polar (r, theta (deg))')
    print(polar)     #100x2 np.array of corresping polar coordinates)

    cart2PolarPlot(cartesian,polar)

    return 0

main()


