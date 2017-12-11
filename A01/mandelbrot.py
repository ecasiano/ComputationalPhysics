# Emanuel Casiano-Diaz. Assignment 01, Due Date: 09/02/16

# Program that generates a Mandelbrot plot and saves it to disk as a pdf.

import numpy as np
import matplotlib.pyplot as plt

# Parameters

N = 501 # Step size of np.array. Make it bigger to make increments of z0 more gradual
M = 51  # Iterations of z

mbset = np.zeros([N,N]) # 2-D array filled with zeros and has  dimensions N x N.

# The following 'chunk'of code determines if a complex number z0 is part of the Mandelbrot Set.
# A number M of iterations of z are evaluated in the last "for loop". If the modulus of z is
# greater than 2, then z0 is not part of the Mandelbrot Set. If z0 is not part of the Mandelbrot
# Set, then the number of the iteration when it was discovered replaces the corresponding zero
# element of the previously defined 2-D array, mbset. NOTE that for larger 'escape numbers', the
# number that will replace a zero in mbset, will be smaller, which will affect the color. 

for j, x in enumerate(np.linspace(-2,1,N)):
	for i, y in enumerate (np.linspace(-1.0j, 1.0j, N)):
		z0 = x + y
		z = 0
		for m in range(M):
			if abs(z) > 2:
				break
			z = z*z + z0
		mbset[i, j] = 1.0/m

# Using matplotlib.pyplot , the Mandelbrot diagram is drawn, shown on screen and saved as a PDF.
# The darker the color, the more it took to find an 'escape number' in the previous chunk of code.

plt.imshow(mbset, cmap ='spectral', extent = [-2, 1, -1, 1])
plt.colorbar()
plt.xlabel(r'Re $z_0$')
plt.ylabel(r'Im $z_0$')
plt.savefig('mandelbrotPlot.pdf')
plt.show()

