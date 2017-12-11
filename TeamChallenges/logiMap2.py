import numpy as np
import matplotlib.pyplot as plt

x = [np.random.random()]
c_mu = 1.25

# the first iteration
x.append(c_mu*x[0]*(1-x[0]))

# continue until we find a fixed point

### INSERT CODE HERE



plt.plot(x,label='x* = %5.3f' % x[-1])
plt.axhline(y=(1.0-1.0/c_mu), linestyle='--', label='1-1/μ')
plt.ylim(0,1)
plt.xlabel('n')
plt.ylabel('x')
plt.legend(frameon=True)
