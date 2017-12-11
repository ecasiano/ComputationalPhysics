#Emanuel Casiano-Diaz

'''
Create an 8 × 8 matrix and fill it with a checkerboard pattern (red = 1, black = 0) without using any loops. Output
any loops. Output the result using the matshow plotting function in Matplotlib.
'''

import numpy as np
import matplotlib.pyplot as plt

#Creates the checker board as an 8x8  array of 1's and 0's
#If argument plot is set to 'y', displays the checkerboard

def checkerBoard(plot):

    zeroOne = np.tile((0,1), 4)
    oneZero = np.tile((1,0), 4)
    board = np.tile ((zeroOne, oneZero), (4,1))

    if plot == 'y':

        plt.matshow(board, cmap='RdGy_r')
        plt.savefig('checkerBoard.png')
        plt.show()
    
    return board

#Main function

def main():

    checkerBoard('y')

    return 0

main()


