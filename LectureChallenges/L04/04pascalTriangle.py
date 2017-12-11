#Emanuel Casiano-Diaz

#Lecture Challenge 04: Build and display Pascal's triangle in the terminal

import numpy as np

def pascal(N):
    
    layoutSpace =  np.zeros([2*N+1, N])             #2D array filled with zeros
    rowLength = range(2*N+1)                        #Amount of elements in each row
    midPoint = rowLength.index(rowLength[-1])//2    #Gives the index of the midPoint of the rows       

    layoutSpace[0][midPoint] = 1                    #1 assigned to the middle of the first row
    total = 1
    for i in range(1, N-1):
        layoutSpace[i][midPoint + i] = 1
        layoutSpace[i][midPoint - i] = 1

    return layoutSpace

def main():
    print(pascal(5))

    return 0

main()

        
        

    
        
        




