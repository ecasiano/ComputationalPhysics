#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.constants import pi
from scipy import integrate

def init(N):
    'Initialize the potential with boundary conditions'

    # the potential
    V = np.zeros([N,N,N]) 			#Factor of 10 to have more values in z-axis
    
    # set the bottom layer
    r = 1                                       #radius of disk
    dr = 1/(N-2)                                #unit cell side length
    
    y = 1
    for i in range(1,N):
        x = -1
        for j in range(1,N):
            if x**2 + y**2 <= r**2:
                V[-1,i,j] = 1
            else:
                V[-1,i,j] = 0
            x += dr
        y -= dr
    
    #Quadrants
    VII = V[-1,:,:]
    VIII = np.flipud(VII)
    VIV = np.fliplr(VIII)
    VI = np.flipud(VIV)
    
    upperHalfPlane = np.append(VII,VI[:,1:],axis=-1)
    lowerHalfPlane = np.append(VIII,VIV[:,1:],axis=-1)

    fullPlane = np.append(upperHalfPlane, lowerHalfPlane[1:,], axis=0)

    planeN = np.size(fullPlane[0])             #New dimensions(N) of plane

    #Rescale V grid
    V = np.zeros([planeN, planeN, planeN])
    V[0] = fullPlane

    # create the copy
    Vp = np.copy(V)

    return V,Vp

'--------------------------------------------------------------'
def SOR_update(V,alpha,mask):
    '''Update the potential according to the Simultaneous-Over-Relaxation method.'''
    
    N = V.shape[0]
    # here we use a mask which tells us which elements should be updated
    dV = 0.0
    for i in range(mask.shape[0]-1):
        for j in range(mask.shape[0]-1):
            for k in range(mask.shape[0]-1):
                if (i!=0 and i!= -1 and j!=0 and j!=-1 and k!=0):

                        V_old = V[k,i,j]
                        V[k,i,j] = (alpha/6)*(V[k,i+1,j] + V[k,i-1,j] + V[k,i,j+1] \
                            + V[k,i,j-1] + V[k+1,i,j] + V[k-1,i,j]) + (1-alpha)*V_old
                        dV += abs(V_old-V[k,i,j])

    return dV

'--------------------------------------------------------------'

def analyticPotential(zList):
    '''Compute the analytical solution of the potential above center'''

    #Parameters
    Vd = 1
    a = 1
    
    VList = np.array([])
    for z in zList:
            V = Vd*(1 - z/np.sqrt(a**2 + z**2))
            VList = np.append(VList, V)
            
    return(VList)
'--------------------------------------------------------------'


def analyticEdge(zList):
    '''Compute the analytical solution of the potential at disk edges'''

    #Parameters
    Vd = 1
    a = 1
    zList[0] = zList[0] + 1E-06      #Value added to avoid getting inf or nan at z=0
 
    VList = np.array([])
    for z in zList:
        
            k = 2*a/np.sqrt(z**2+4*a**2)

            def f(phi):
                return 1/np.sqrt(1-k**2 * np.sin(phi)**2)

            I = integrate.quad(f,0,pi/2)
            I = I[0] #Only assign value of integration, not the error

            V = (Vd)*(1 - I*(k*z/pi*a))
            VList = np.append(VList, V)
    return(VList)
'--------------------------------------------------------------'

def main():

    'SOR Method'

    # the number of lattice points in the x and y direction
    N = 350

    # the tolerance for convergence
    epsilon = 1.0E-12

    # the over-relaxation parameter
    alpha = 2/(1+(pi/N))

    # initialize 
    V,mask = init(N)
    VBottom = V[0,:,:]
    VHalfWayUp = V[V.shape[0]//2,:,:]

    # Plot the initial configuration
    fig = plt.figure(figsize=(8,5))
    plt.title('Initial Configuration, N=%d' % (N))
    im = plt.imshow(VBottom, extent=[-1,1,-1,1], cmap='bwr')
    plt.xlabel('x')
    plt.ylabel('y')
    cb = plt.colorbar(label='Electric Potential(SOR)', pad=0.1)
    plt.savefig('niceDisk.png')
    #plt.savefig('initialPotentialSOR_disk.png')
    plt.show()

    # Iterate until convergence
    nSOR = 0
    dV = 1.0

    while dV/(N*N) > epsilon:
            dV = SOR_update(V,alpha,mask)
            nSOR+= 1

    # plot the final converged potential
    fig = plt.figure(figsize=(8,5))
    plt.title('Converged Potential(SOR) N=%d' % (N))
    im = plt.imshow(VHalfWayUp, extent=[-1,1,-1,1], cmap='bwr')
    plt.xlabel('x')
    plt.ylabel('y')
    cb = plt.colorbar(label='Electric Potential', pad=0.1)
    plt.savefig('finalpotentialsor_disk.png')
    plt.show()

    #Get values on top of disk center
    Vz = V[:,V.shape[0]//2, V.shape[0]//2]
    zMax = 10

    zList = np.array([])

    for i in np.linspace(0,zMax,V.shape[0]):
        zList = np.append(zList,i)

    plt.plot(zList,Vz, label='SOR')

    # plot analytical and SOR solutions of potential above center
    VzAna = analyticPotential(zList)

    plt.plot(zList,VzAna,label='Analytical')
    plt.xlabel('z')
    plt.ylabel('electric potential V')
    plt.title('Disk at potential V=1 in a grounded conducting plane (AboveCenter)')
    plt.legend(loc='best')
    plt.savefig('analyticalVSOR_diskCenter.png')
    plt.show()

    # plot analytical and SOR solutions of potential above edge
    VzEdge = V[:,V.shape[0]//2, 1]
    VzEdgeAna = analyticEdge(zList)
    plt.plot(zList, VzEdge,'ko', label='SOR')
    plt.plot(zList, VzEdgeAna, label='Analytical')
    plt.xlabel('z')
    plt.ylabel('electric potential V')
    plt.title('Disk at potential V=1 in a grounded conducting plane (AboveEdge)')
    plt.legend(loc='best')
    plt.savefig('analyticalVSOR_diskEdge.png')
    plt.show()
    
    print("dV = %8.5E in %d steps" % ((dV/N**2),nSOR))
if __name__ == '__main__':
    main()
