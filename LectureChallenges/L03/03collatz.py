#Emanuel Casiano-Diaz

#LectureChallenge 03: Explore the CollatzConjecture

import numpy as np
import matplotlib.pyplot as plt
from math import floor

def collatz(n):

    #The following list, fList, will store the result after each iteration
    fList = [n]

    f = 3*n + 1 if (n % 2 != 0 or n == 1) else n//2

    fList.append(f)

    while f != 1:

        f = 3*f + 1 if (f % 2 != 0) else f//2
        
        fList.append(f)

    return fList   

def main():

       n = 0

       while(n < 1 or type(n) != int ): 
         n = int(input('Enter starting number (must be integer and greater than 0): '))

       plot = input('Want to plot? [y/n] ')

       print(list(collatz(n)))
      
       #Plots f vs iteration number if user presses 'y'

       if plot == 'y':
            fList = np.array(collatz(n))
            iterations = np.array(range(len(collatz(n))))

            print('Iterations until 1 (stopping time): i = %d' % (iterations[-1]))

            plt.plot(iterations, collatz(n), 'b-')
            plt.axis([iterations[0], iterations[-1], np.min(fList), np.max(fList)])
            plt.xlabel('Iterations of f(n)')
            plt.ylabel('f(n)')
            plt.title('CollatzConjecture (n = %d)' % n)
            plt.show()

       return 0

main()
