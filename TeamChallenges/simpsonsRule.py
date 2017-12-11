import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi as  π
from scipy.special import erf

def simpsons_rule(f,x,*params):
	'The trapezoidal rule for numerical integration of f(x) over x'
	a, b = x[0],x[-1]
	dx = x[1] - x[0]
	N = x.size

	I = f(a,*params) + f(b, *params)
	I += 

def erf_kernel(t):
    '''The error function kernel.'''
    return  ### INSERT CODE HERE ###

dx = 0.001
x = np.linspace(0,1,20)
erf_approx = np.zeros_like(x)

for j,cx in enumerate(x[1:]):
    N = int(cx/dx)
    if N % 2: N += 1
    x_int = np.linspace(0,cx,N)
    erf_approx[j] = simpsons_rule(erf_)

# plot the results and compare with the 'exact' value
plt.plot(x,erf_approx,'o', mec=colors[0], mfc=colors[0], mew=1, ms=8, label="Simpson's Rule")
plt.plot(x,erf(x), color=colors[1],zorder=0, label='scipy.special.erf')
plt.legend(loc='lower right')
plt.xlabel('x')
plt.ylabel('erf(x)')