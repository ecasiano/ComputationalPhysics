#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt


def simpsons_rule(f,x,*params):
	'''The trapezoidal rule for numerical integration of f(x) over x.'''
	a,b = x[0],x[-1]
	dx = x[1] - x[0]
	N = x.size

	I = (f(a,*params) + f(b,*params))/3.0
	I += (4.0/3.0)*sum([f(a+i*dx,*params) for i in range(1,N,2)])
	I += (2.0/3.0)*sum([f(a+i*dx,*params) for i in range(2,N,2)])

	return dx*I

def I(x,alpha):

	return ( 1/(1-x)**alpha )

def main():
	#alpha = np.linspace(0,0.9,100000)
	alphaMax = 0.999999999
	t = np.arange(0,1,1/100000)

	alphaList = np.arange(0,1,0.01)
	IListAna = np.array([])
	IListSimpson = np.array([])
	for alpha in alphaList:
		IAna = 1/(1-alpha)
		IListAna = np.append(IListAna, IAna)
		IListSimpson = np.append(IListSimpson, simpsons_rule(I,t,alpha))

	#Plot and compare Simpsons vs Analytical Result
	plt.plot(alphaList, IListAna, 'b-', label='Analytical')
	plt.plot(alphaList, IListSimpson, 'ko', label='Simpsons Rule')
	plt.title('Comparison of Analytical result and Simpsons Rules')
	plt.xlabel(r'$\alpha$')
	plt.ylabel(r'$I(\alpha)$')
	plt.legend(loc='best')
	plt.savefig('powerLawSingularities.png')
	plt.show()

	print(simpsons_rule(I,t,alpha))

if __name__ == '__main__':
	main()
