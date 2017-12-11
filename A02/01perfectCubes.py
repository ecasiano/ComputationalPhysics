#Emanuel Casiano-Diaz

#Determines if integer number entered by user is a perfect cube

def perfectCube(N):                 #Function returns a boolean value

    if N < 0:                       #Takes care of negative input
        
        N = abs(N)

    isPerfectCube = False

    for i in range(N+1):           #N+1 makes sure input of -1,0 or 1 includes them on list

        if i**3 == N:

            isPerfectCube = True
            break

    return isPerfectCube

def main():

    N = int(input('Enter an integer number. I will let you know if it is a perfect cube: ' ))

    if perfectCube(N) == True:

        print('%d is a perfect cube.' % N)

    else:

        print('%d is NOT a perfect cube.' % N)

    return 0

main()






