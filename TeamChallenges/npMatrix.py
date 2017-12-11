#Team Programming Challenge

import numpy as np

# 1. Find indices of non-zero elements

l = [1,2,0,0,4,0]

indices = []

for i,j in enumerate(l):

    if j != 0:
        indices.append(i)

np.array(indices)

print(indices)

# 2.Create an array of uniformly distributed numbers between 1 and 3
# and explore how the average depends on the length of the array.

a = np.linspace(1,3)

average = 0

for i in a:

    average += a[]
            
#3 Show that a 10x10 identity matrix is idenpotent.

M = np.random.rand(10,10)


