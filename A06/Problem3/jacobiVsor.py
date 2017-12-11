#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi

'--------------------------------------------------------------'
def init(N):
    '''Initialize the potential with boundary conditions.'''

    # the potential
    V  = np.zeros([N,N])

    # set the boundary conditions 
    V[:,(N//2)-N//8] = 1.0
    V[:,(N//2)+N//8] = -1.0
    V[0,:] = 0
    V[-1,:] = 0
    V[1,:] = 0
    V[-2,:] = 0
    # create the copy
    Vp = np.copy(V)

    return V,Vp

'--------------------------------------------------------------'
def jacobi_update(V,Vp):
    '''Update the potential according to the Jacobi method.'''
    N = V.shape[0]
    ΔV = 0.0
    for i in range(1,V.shape[0]-1):
        for j in range(1,V.shape[1]-1):
        	if (j!=(N//2)-N//8 and j!=(N//2)+N//8):
	            Vp[i,j] = 0.25*(V[i-1,j] + V[i+1,j] + V[i,j+1] + V[i,j-1])
	            ΔV += abs(Vp[i,j]-V[i,j])

    return ΔV

'--------------------------------------------------------------'
def SOR_update(V,α,mask):
    '''Update the potential according to the Simultaneous-Over-Relaxation method.'''
    
    N = V.shape[0]
    # here we use a mask which tells us which elements should be updated
    ΔV = 0.0
    for i in range(mask.shape[0]-1):
        for j in range(mask.shape[1]-1):
        	if (j!=(N//2)-N//8 and j!=(N//2)+N//8):

        		V_old = V[i,j]
        		V[i,j] = (α/4)*(V[i-1,j] + V[i+1,j] + V[i,j+1] + V[i,j-1]) + (1-α)*V_old
        		ΔV += abs(V_old-V[i,j])
    return ΔV

'--------------------------------------------------------------'
def getE(V):
    '''Compute the electric field using a centered derivative for an isotropic discretization
       equal to 1.'''

    # initialize the E-Field arrays    
    Ex = np.zeros(V.shape)
    Ey = np.zeros_like(Ex)

    #Compute the electric field as the gradient of the potential
    for i in range(1,V.shape[0]-1):
        for j in range(1,V.shape[1]-1):
            Ex[i,j] = -0.5*(V[i,j+1]-V[i,j-1])
            Ey[i,j] = -0.5*(V[i+1,j]-V[i-1,j])

    # Return the electric field
    return Ex,Ey

def main():

	'---------------------------------------------------------------------'
	'Jacobi Method'
	# the number of lattice points in the x and y direction
	N = 20

	# the tolerance for convergence
	ϵ = 1.0E-5

	# initialize 
	V,Vp = init(N)

	# Plot the initial configuration
	fig = plt.figure(figsize=(8,5))
	plt.title('Initial Configuration(Jacobi)')
	im = plt.imshow(1.0*V, extent=[-1,1,-1,1], cmap='bwr')
	plt.xlabel('x')
	plt.ylabel('y')
	cb = plt.colorbar(label='Electric Potential', pad=0.1)
	plt.savefig('initialPotentialJacobi.png')
	plt.show()

	# Iterate until convergence
	nJacobi = 0
	ΔV = 1.0

	while ΔV/(N*N) > ϵ:
		ΔV = jacobi_update(V,Vp)
		ΔV += jacobi_update(Vp,V)
		nJacobi+= 1

	# plot the final converged potential
	fig = plt.figure(figsize=(8,5))
	plt.title('Converged Potential(Jacobi)')
	im = plt.imshow(1.0*V, extent=[-1,1,-1,1], cmap='bwr')
	plt.xlabel('x')
	plt.ylabel('y')
	cb = plt.colorbar(label='Electric Potential(Jacobi)', pad=0.1)
	plt.savefig('finalPotentialJacobi.png')
	plt.show()

	# plot the electric field

	Ex,Ey = getE(V)
	X,Y = np.meshgrid(np.linspace(-1.0,1.0,N),np.linspace(-1.0,1.0,N))
	plt.contourf(X,Y,V,50, cmap='bwr')
	plt.quiver(X,Y,Ex,Ey)
	plt.axis([-1.0,1.0,-1.0,1.0])
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Electric Field')
	plt.savefig('electricField.png')
	plt.show()

	print("ΔV = %8.5E in %d steps" % ((ΔV/N**2),nJacobi))

	'---------------------------------------------------------------------'
	'SOR Method'

	# the number of lattice points in the x and y direction
	N = 20

	# the tolerance for convergence
	ϵ = 1.0E-5

	# the over-relaxation parameter
	α = 2/(1+(pi/N))
	#α = 2.5

	# initialize 
	V,mask = init(N)

	# Plot the initial configuration
	fig = plt.figure(figsize=(8,5))
	plt.title('Initial Configuration')
	im = plt.imshow(1.0*V, extent=[-1,1,-1,1], cmap='bwr')
	plt.xlabel('x')
	plt.ylabel('y')
	cb = plt.colorbar(label='Electric Potential(SOR)', pad=0.1)
	plt.savefig('initialPotentialSOR.png')
	plt.show()

	# Iterate until convergence
	nSOR = 0
	ΔV = 1.0

	while ΔV/(N*N) > ϵ:
		ΔV = SOR_update(V,α,mask)
		nSOR+= 1

	# plot the final converged potential
	fig = plt.figure(figsize=(8,5))
	plt.title('Converged Potential(SOR)')
	im = plt.imshow(1.0*V, extent=[-1,1,-1,1], cmap='bwr')
	plt.xlabel('x')
	plt.ylabel('y')
	cb = plt.colorbar(label='Electric Potential', pad=0.1)
	plt.savefig('finalPotentialSOR.png')
	plt.show()
	
	print("ΔV = %8.5E in %d steps" % ((ΔV/N**2),nSOR))
if __name__ == '__main__':
	main()
