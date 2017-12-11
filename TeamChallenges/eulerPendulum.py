import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi as π
from scipy.constants import g

# constants and intitial conditions
ℓ = 0.25 # m
Δt = 0.01 # s

t = np.arange(0.0,4.0,Δt)
θ,ω = np.zeros_like(t),np.zeros_like(t)
θ[0] = π/12.0 # rad

#for n in range(t.size-1):


# the small angle solution
plt.plot(t, θ[0]*np.cos(np.sqrt(g/ℓ)*t), label='Small angle solution')

# the Euler method
plt.plot(t,θ, label='Euler method')
plt.legend(loc='lower left')

plt.xlabel('Time [s]')
plt.ylabel('θ(t) [rad]')

plt.show()
