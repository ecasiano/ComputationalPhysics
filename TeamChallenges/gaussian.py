import numpy as np
import matplotlib.pyplot as plt


x_axis = np.linspace(0,100)

gaussian = [(1/np.sqrt(2*np.pi))*np.exp((-1.0*x**2)/2) for x in x_axis]

plt.plot(x_axis, gaussian)
plt.show()
