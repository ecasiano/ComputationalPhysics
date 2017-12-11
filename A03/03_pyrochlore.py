#Emanuel Casiano-Diaz

'''
Assume the edge of the cubic unit cell is a = 10 ˚A and write a program that generates an array
of the (x, y, z) positions of at least 500 atoms and stores them to disk in scientific notation
as a text file named pyrochlore.dat with appropriate column headings.
'''

import numpy as np
import matplotlib.pyplot as plt
from itertools import product

#Given the edge a of the cubic unit cell (in Amstrongs), returns an array  with the
#coordinates x, y, z of the atoms constituting 125 pyroclore molecules (500 atoms)

def pyroAtoms(a):
    
    #Components(ni,nj,nk)
    #NOTE: For this assignment,I have these components have been chosen from the 
    #125 permutations of three elements in the set {0,1,2,3,4} using itertools.product

    components = np.array(list(product((0,1,2,3,4), repeat=3)))
    ni = components[:,0]
    nj = components[:,1]
    nk = components[:,2]

    #x,y,z components of R (pyrochlore position vector)
    Rx1 = ni*0 + nj*a/2 + nk*a/2
    Ry1 = ni*a/2 + nj*0   + nk*a/2
    Rz1 = ni*a/ 2+ nj*a/2 + nk*0

    Rx2 = ni*0   + nj*a/2 + nk*a/2 + a/4
    Ry2 = ni*a/2 + nj*0   + nk*a/2 + a/4
    Rz2 = ni*a/ 2+ nj*a/2 + nk*0

    Rx3 = ni*0   + nj*a/2 + nk*a/2 + a/4
    Ry3 = ni*a/2 + nj*0   + nk*a/2
    Rz3 = ni*a/ 2+ nj*a/2 + nk*0   + a/4

    Rx4 = ni*0   + nj*a/2 + nk*a/2
    Ry4 = ni*a/2 + nj*0   + nk*a/2 + a/4
    Rz4 = ni*a/ 2+ nj*a/2 + nk*0   + a/4

    Rx1 = np.reshape(Rx1,(125,1))
    Ry1 = np.reshape(Ry1,(125,1))
    Rz1 = np.reshape(Rz1,(125,1))
    R1 = np.column_stack((Rx1,Ry1,Rz1))

    Rx2 = np.reshape(Rx2,(125,1))
    Ry2 = np.reshape(Ry2,(125,1))
    Rz2 = np.reshape(Rz2,(125,1))
    R2 = np.column_stack((Rx2,Ry2,Rz2))   

    Rx3 = np.reshape(Rx3,(125,1))
    Ry3 = np.reshape(Ry3,(125,1))
    Rz3 = np.reshape(Rz3,(125,1))
    R3 = np.column_stack((Rx3,Ry3,Rz3))

    Rx4 = np.reshape(Rx4,(125,1))
    Ry4 = np.reshape(Ry4,(125,1))
    Rz4 = np.reshape(Rz4,(125,1))
    R4 = np.column_stack((Rx4,Ry4,Rz4)) 
    
    Rx = np.concatenate((Rx1, Rx2, Rx3, Rx4))
    Ry = np.concatenate((Ry1, Ry2, Ry3, Ry4))
    Rz = np.concatenate((Rz1, Rz2, Rz3, Rz4))
    R = np.column_stack((Rx,Ry,Rz)) #xyz positions of each pyrochlore molecule

    return((R1,R2,R3,R4,R))

'''
Use the Matplotlib plot or scatter functions to generate three plots of the location of the
atoms projected into the xy, xz and yz plane. Differentiate the tetrahedral basis positions
using different colors.
'''

#Takes the array of x,y,z positions of pyrochlore atoms and plots projections
#into the xy, xz and yz planes

def pyroAtomsPlot(R1,R2,R3,R4):

    xAxis1 = R1[:,0]
    yAxis1 = R1[:,1]
    zAxis1 = R1[:,2]

    xAxis2 = R2[:,0]
    yAxis2 = R2[:,1]
    zAxis2 = R2[:,2]

    xAxis3 = R3[:,0]
    yAxis3 = R3[:,1]
    zAxis3 = R3[:,2]

    xAxis4 = R4[:,0]
    yAxis4 = R4[:,1]
    zAxis4 = R4[:,2]

    #xy-plane

    plt.plot(xAxis1,yAxis1,'bo' )
    plt.plot(xAxis2,yAxis2,'ro' )
    plt.plot(xAxis3,yAxis3,'yo' )
    plt.plot(xAxis4,yAxis4,'go' )
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-1,45)
    plt.ylim(-1,45)
    plt.title('xy-plane')
    plt.savefig('xy.png')

    #xz-plane

    plt.plot(xAxis1,zAxis1,'bo' )
    plt.plot(xAxis2,zAxis2,'ro' )
    plt.plot(xAxis3,zAxis3,'yo' )
    plt.plot(xAxis4,zAxis4,'go' )
    plt.xlabel('x')
    plt.ylabel('z')
    plt.xlim(-1,45)
    plt.ylim(-1,45)
    plt.title('xz-plane')
    plt.savefig('xz.png')

    #yz-plane

    plt.plot(yAxis1,zAxis1,'bo' )
    plt.plot(yAxis2,zAxis2,'ro' )
    plt.plot(yAxis3,zAxis3,'yo' )
    plt.plot(yAxis4,zAxis4,'go' )
    plt.xlabel('y')
    plt.ylabel('z')
    plt.xlim(-1,45)
    plt.ylim(-1,45)
    plt.title('yz-plane')
    plt.savefig('yz.png')

def main():

    R1,R2,R3,R4,R = pyroAtoms(10)
    
    pyroAtomsPlot(R1,R2,R3,R4)

    #Create .dat file and save to disk
    
    np.savetxt('pyrochlore.dat', R)

    print(R)

    return 0

main()
