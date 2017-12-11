import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,100)

y1 = x

a = 5

y2 = np.tanh(x/a)

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlim(0,5)
plt.ylim(0,5)
plt.show()
