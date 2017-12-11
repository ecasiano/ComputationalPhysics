import numpy as np
import matplotlib.pyplot as plt

def init_poisson(N,delta):
    '''Initialize the potential with boundary conditions.'''
    
    # midpoint
    mid = int(N/2)
    
    # potential, charge density and mask
    V  = np.zeros([N,N,N],dtype=float)
    rho = np.zeros_like(V)
    mask = np.ones([N,N,N],dtype=int)
    
    ###
    # INITIALIZE MASK
    ###
    
    ###
    # INITIALIZE ρ \rho
    ###
    
    return V,rho,mask

def SOR_update_3D(V,rho,alpha,delta,mask):
    '''Update the potential according to the Simultaneous-Over-Relaxation method.'''
    
    # here we use a mask which tells us which elements should be updated
    dV = 0.0
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            for k in range(mask.shape[2]):
                if mask[i,j,k]:
                    V_old = V[i,j,k]
                    ###
                    # INSERT CODE HERE
                    ###
                    
                    dV += abs(V_old-V[i,j,k])
return dV

def main():

    # the number of lattice points in each direction
    N = 11

    # box and grid size
    L = 1.0
    delta = L/N

    # the tolerance for convergence
    epsilon = 1.0E-5

    # the over-relaxation parameter
    alpha = 1.5

    # initialize
    V,rho,mask = init_poisson(N,delta)

    # Iterate until convergence
    dV = 100.0
    while dV/(N**3) > epsilon:
    ###
    # INSERT CODE HERE
    ###

    print("dV = %8.5E in %d steps" % ((dV/N**3),n))

    # plot the final result as a contour plot
    X,Y = np.meshgrid(np.linspace(-L/2,L/2,N), np.linspace(-L/2,L/2,N))
    cs = plt.contourf(X,Y,np.transpose(V[:,:,int(N/2)]),10,cmap=plt.get_cmap('bwr'))
    cb = plt.colorbar(label='Electric Potential', pad=0.1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axes().set_aspect('equal')

if __name__ == '__main__':
    main()
