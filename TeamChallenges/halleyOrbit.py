#Emanuel Casiano-Diaz

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi

def celestialOrbits(T):
   
    theta = 0

    a = T**(2/3) #SemiMajor Axis From Kepler's Third Law 
    
    xList = np.array([])
    yList = np.array([])

    x = a
    y = 0

    thetasList = np.arange(0,91,0.01)
    xStep = x/np.size(thetasList)

    for theta in np.arange(0,90,0.1):
        y = 0
        angle = np.degrees(np.arctan(y/x))
        while np.round(angle,2) != 0:
            y += 0.001
        xList = np.append(xList,x)
        yList = np.append(yList,y)
        x -= xStep
    
    return(xList, yList)

def main():

    print(celestialOrbits(76))

if __name__ == '__main__':
    main()

        
        


