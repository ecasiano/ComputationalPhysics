#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def init(N):
    'Initialize the potential with boundary conditions'

    #the potential
    V = np.zeros([N,N])
    
    #boundary conditions
    V[:,N//2] = 10000      #The Rod
    V[1,N//2] = 0.0         #some space in between
    V[2,N//2] = 0.0         #some space in between
    V[0,:] = -10000         #The Clouds

    #create the copy
    Vp = np.copy(V)

    return V,Vp

def jacobi_update(V,Vp):
    'Update the potential using Jacobi Method'
    
    dV = 0
    for i in range(0,V.shape[0]-1):
        for j in range(0,V.shape[0]-1):
            if not(j == V.shape[0]//2 and i>=3):
                Vp[i,j] = 0.25*(V[i-1,j] + V[i+1,j] + V[i,j+1] + V[i,j-1])
                dV += abs(Vp[i,j] - V[i,j])

    return dV

def getE(V):
        'Compute the electric field using a centered derivative for an isotropic discretization equal to 1.'

        # initialize the E-Field arrays    
        Ex = np.zeros(V.shape)
        Ey = np.zeros_like(Ex)

        #Compute the electric field as the gradient of the potential
        for i in range(1,V.shape[0]-1):
            for j in range(0,V.shape[1]-1):
                Ex[i,j] = -0.5*(V[i,j+1]-V[i,j-1])
                Ey[i,j] = -0.5*(V[i+1,j]-V[i-1,j])

        # Return the electric field
        return Ex,Ey

def main():

    N = 51

    tolerance = 1.0E-5

    V,Vp = init(N)

    # Plot the initial configuration
    fig = plt.figure(figsize=(8,5))
    plt.title('Lightning Rod Initial Configuration')
    im = plt.imshow(1.0*V, extent=[-1,1,-1,1], cmap='bwr')
    plt.xlabel('x')
    plt.ylabel('y')
    cb = plt.colorbar(label='Electric Potential', pad=0.1)
    plt.savefig('LRinitial.png')
    plt.show()

    # Iterate until convergence
    n = 0
    dV = 1.0

    while dV/(N*N) > tolerance:
        dV = jacobi_update(V,Vp)
        dV += jacobi_update(Vp,V)
        n+= 1

    # plot the final converged potential
    fig = plt.figure(figsize=(8,5))
    plt.title('Lightning Rod Converged Potential')
    im = plt.imshow(1.0*V, extent=[-1,1,-1,1], cmap='bwr')
    plt.xlabel('x')
    plt.ylabel('y')
    cb = plt.colorbar(label='Electric Potential', pad=0.1)
    plt.savefig('LRfinal.png')
    plt.show()

    # plot final equipotential lines
    fig = plt.figure(figsize=(5,5))
    X,Y = np.meshgrid(np.linspace(1.0,-1.0,N),np.linspace(1.0,-1.0,N))
    cs = plt.contour(X,Y,V,20, cmap='bwr')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.clabel(cs, inline=1, fontsize=12)
    plt.title('Lightnin Rod Equipotential Lines')
    plt.savefig('LRequipotential.png')
    plt.show()

    print("ΔV = %8.5E in %d steps" % ((dV/N**2),n))

    #Get and plot final electric field
    Ex,Ey = getE(V)
    X,Y = np.meshgrid(np.linspace(-1.0,1.0,N),np.linspace(-1.0,1.0,N))
    plt.contourf(-X,-Y,V,50, cmap='bwr')
    plt.quiver(-X,-Y,-Ex,-Ey)
    plt.axis([-1.0,1.0,-1.0,1.0])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Lightning Electric Field')
    plt.savefig('LRfield.png')
    plt.show()

    return 0

if __name__ == '__main__':
    main()

