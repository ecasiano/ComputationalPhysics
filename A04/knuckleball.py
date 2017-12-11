#Emanuel Casiano-Diaz (Last modified on 10/15/16.)

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants
from scipy.constants import g,pi

def convert(value,unit1,unit2):
        '''Convert value in unit1 to unit2'''
                
        # the converter
        conv = {'ft->m':constants.foot,'in->m':constants.inch,'mph->m/s':constants.mph}

        # make a copy and perform reverse conversions
        cpy_conv = dict(conv)
        for key, val in cpy_conv.items():
            units = key.split('->')
            conv[units[-1]+'->'+units[0]] = 1.0/val
                                                                
        # perform the conversion
        key = '%s->%s'%(unit1,unit2)
        if key in conv:
            return value*conv[key]
        else:
            print('Unit conversion %s not possible.' %key)

def main():
    # GridBox Features
    gridSides = 36                        #side length of grid box (in inches)-->3ft
    gridArea = gridSides**2
    unitCellArea = 13.6                   #cross-sectional area of baseball (inches)
    unitCellSides = np.sqrt(unitCellArea)
    insideBox = 0                         #pitches inside the box
    
    # Generate GridBox
    N = 1                                 #number of unit cells in a each row or columni
    unitCellRanges = [0,unitCellSides]
    while(N*unitCellSides <= gridSides):
        N += 1
        unitCellRanges.append(unitCellSides*N)
    gridBox = np.zeros((N,N))             #2D-Array of dimension = (N*unitCellSide)^2

    #Parameters
    pitches = 2000
    pitchesList = np.arange(0,pitches,1)

    for i in pitchesList:

        # the time step
        dt = 0.001 # s

        # the dimensionless angular drag factor
        S0om = 4.1E-4

        # drag force
        B2om = 0.0005
        
        #Initial Positions
        x0 = 0
        y0 = convert(np.random.uniform(6.3,6.7), 'ft', 'm')       #Observed release heights: 6.5+-0.2ft
        z0 = convert(np.random.uniform(2.9,3.1), 'ft', 'm')       #Horizontal inital pos of pitch: 1.5+-0.1ft from home
        theta = convert(np.random.uniform(0,2*np.pi),'ft','m')    #Initial angle of the baseball respect to y-axis 

        #Initial Velocities
        vx = convert(np.random.uniform(64.0,71.0),'mph','m/s')      #Observed initial pitch speeds: 67.5+-3.5mph
        vy = convert(np.random.uniform(0.8,1.6),'mph','m/s')        #Observed initial vertical speeds: 1.2+-0.4mph
        vz = convert(np.random.uniform(1.5,1.9),'mph','m/s')        #Observed initial transverse speed: 1.7+-0.2mph
        omega = np.random.uniform(0.35,0.45)                        #Observed initial rotations: 0.4 +- 0.05 rev/s
        
        # lateral force
        lateralForce = 0.5*g*(np.sin(4*theta) - 0.25*np.sin(8*theta) + 0.08*np.sin(12*theta) - 0.025*np.sin(16*theta))
        # Magnus force
        magnusForce = S0om*vx*omega

        # initial conditions (convert everything to SI)
        r = np.array([[x0,y0,z0]])
        while r[-1,0] <= convert(60.5,'ft','m'):
                v = np.sqrt(vx**2 + vy**2 + vz**2)
                vx -= B2om*v*vx*dt
                vy -= g*dt
                vz -= (S0om*vx*omega + lateralForce)*dt
                cr = np.array([[vx,vy,-vz]])*dt
                r = np.append(r,r[-1]+cr,axis=0)            

        # convert the result to feet
        r = convert(r,'m','ft')

        #convert result to inches to fill gridBox
        r_inches = convert(convert(r,'ft','m'),'m','in')
        
        #determine the corresponding coordinates (y,z) to fill the gridbox
        for j,l in enumerate(unitCellRanges):
            if r_inches[-1][1] >= l and r_inches[-2][1] < l + unitCellSides:
                y = j
                break
        
        for k,m in enumerate(unitCellRanges):
            if (gridSides - (r_inches[-1][2] - r_inches[0][2])) >= m and (gridSides - (r_inches[-1][2] - r_inches[0][2])) < m + unitCellSides:
                z = k
                gridBox[y][z] += 1
                insideBox += 1
                break
            #out of the box
            if (gridSides - (r_inches[-1][2] - r_inches[0][2])) <= unitCellRanges[0] or (gridSides - (r_inches[-1][2] - r_inches[0][2])) > unitCellRanges[-1]:
                break
    
    outsideBox = pitches - insideBox      #pitches outside box
    #Probability gridBox
    print(gridBox)
    print('Pitches inside box: ', insideBox)
    print('Pitches outside box: ', outsideBox)

    #Fills each unit cell with the amount of pitches going through there
    for y in range(gridBox.shape[0]):
        for x in range(gridBox.shape[1]):
            plt.text(x + 0.5, y + 0.5, '%.d' % gridBox[y, x],horizontalalignment='center',verticalalignment='center')
    
    #Density Plot
    gridSides = convert(gridSides,'in','m')
    gridSides = convert(gridSides,'m','ft')
    plt.pcolor(gridBox)
    plt.xticks(np.arange(0,np.size(unitCellRanges)), np.linspace(-gridSides/2,gridSides/2, np.size(unitCellRanges)))  #Label axis subdivisions such that homeplate is at z=0
    plt.yticks(np.arange(0,np.size(unitCellRanges)), np.linspace(0,gridSides,np.size(unitCellRanges)))
    plt.xlabel('z(t) (horizontal), (ft)')
    plt.ylabel('y(t) (vertical), (ft)')
    plt.title('Knuckleball Positions at Home Plate (%.d pitches)'%pitches)
    plt.colorbar()
    plt.savefig('knuckleball_colormap.png')
    plt.show()
    
if __name__ == '__main__':
    main()
