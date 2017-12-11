#Emanuel Casiano-Diaz

#Find square up to an accuracy of 4 decimal places and displays output at each
#level of precision

def customSqrt(N):

    if N < 0:

        print('Warning: Input was negative. Will use the absolute value instead.')
        
        N = abs(N)

    intN = int(N)

    #Determines the integer part of sqrt approximation   
    for i in range(intN+1):                

        if i**2 <= N and N < (i+1)**2:
            
            intPart = i

            if N == (i+1)**2:

                intPart = i+1

            break

    decPart = 0.00

    sqrt = intPart + decPart
    
    #At the end of the loop, the corresponding decimals of the approximation are added
    #to the integer part

    while (sqrt**2 <= N-0.0001):
         
         sqrt = intPart + decPart
         decPart += 0.0001

    if(abs(N-(sqrt**2+0.0001)) <= abs(N-(sqrt**2))):

        sqrt = sqrt + 0.0001

    return sqrt


def main():

    N = float(input('Enter a non-negative number and I will calculate the square root: '))

    sqrt = customSqrt(N)

    print('Square root of %f is: ' % N)
   
    print('4 decimal places: %.4f' % (sqrt))
    print('3 decimal places: %.3f' % (sqrt))
    print('2 decimal places: %.2f' % (sqrt))
    print('1 decimal places: %.1f' % (sqrt))
    print('0 decimal places: %d' % (sqrt))

    return 0

main()





        
        
