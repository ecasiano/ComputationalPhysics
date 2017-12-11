#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt

#Plot a comparison of the scaling for Jacobi and the SOR methods

L = np.array([10,20,30,40,50])
nJacobi = np.array([22,77,159,237,356])
nSOR = np.array([18,38,57,73,91])

plt.plot(L,nJacobi, label='Jacobi')
plt.plot(L,nSOR, label='SOR')
plt.title('Iterations until convergence vs. grid size')
plt.xlabel('L')
plt.ylabel('n iterations')
plt.legend(loc='best')
plt.savefig('scalingComparison.png')
plt.show()
