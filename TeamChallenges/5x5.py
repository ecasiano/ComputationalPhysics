import numpy as numpy

M = []
ctr = 0
for i in range(5):
    N = []
    for j in range(5):
        N.append(j+ctr)
    ctr += 10
    M.append(N)

print(M)


