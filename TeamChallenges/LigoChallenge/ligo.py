# Comparing LIGO data with NumericalRelativity prediction

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('ligo_data.dat')
prediction =np.loadtxt('nr_prediction.dat')

plt.figure()
#H1 Strain
plt.subplot(2,1,1)
plt.plot(data[:,0], data[:,1], label = 'H1 Strain')
plt.plot(prediction[:,0], prediction[:,1], label = 'NR Prediction')
plt.title('Hanford, Washington')
plt.ylabel('Strain Waveform')
plt.legend(loc = 'upper left')
plt.ylim(-4,4)
plt.xlim(-0.05,0.02)

#H2 Strain
plt.subplot(2,1,2)
plt.plot(data[:,0], data[:,2], label = 'H2 Strain')
plt.plot(prediction[:,0], prediction[:,1], label = 'NR Prediction')
plt.xlabel('time (s)')
plt.ylabel('Strain Waveform')
plt.legend(loc = 'upper left')
plt.ylim(-4,4)
plt.xlim(-0.05,0.02)
plt.show()

