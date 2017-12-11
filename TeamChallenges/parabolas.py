import numpy as np
import matplotlib.pyplot as plt

def parabola(k):

    parabola = []
    for i in range(-10,10):
        parabola.append(i**2 + k*10)
    return np.array(parabola)

x_axis = np.array(range(-10,10))
marker_list = ['o','s','p','^','v','>','<','D','*','H']
for m, n in enumerate(marker_list):
    plt.plot(x_axis, parabola(m), n)
plt.show()
