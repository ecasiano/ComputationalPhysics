import numpy as np

N = 100
mu = [1.5, 3.3, 3.8]
x = np.random.random(N)

def logistic_map(x, mu):
    
    for n in range(x.size - 1):
        x[n+1] = mu*x[n]*(1-x[n])

    return x

    
print(logistic_map(x,mu))
