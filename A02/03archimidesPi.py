#Emanuel Casiano-Diaz

#Use Archimides method to approximate the value of pi to at least 4 decimals.
#Outputs a table showing the number of sides, lower and upper bound on pi.
# % Operator is used to print a maximum of 10 rows

from math import sqrt, tan, radians

def archPi(doubling):

    #Start with hexagon, just as Archimides did

    n = 6
    diameter = 2
    radius = diameter/2
    sideLengthIn = 1                  #Outer polygon side length
    sideLengthOut = (2*sqrt(3))/3     #Inner polygon side length

    for i in range(doubling+1):
 
        pi_In = n*sideLengthIn/diameter
        pi_Out = n*sideLengthOut/diameter
        n = n*2
        bisection = sqrt(radius**2-(sideLengthIn/2)**2) #Length of bisecting line resulting when doubling n
        sideLengthIn = sqrt((radius-bisection)**2+(sideLengthIn/2)**2)
        sideLengthOut = diameter*tan(radians(180)/n) #NOTE:Outer side length determined using radians
        averagePi = (pi_In + pi_Out)/2 #Average of up/lower bounds
    return [averagePi,n/2, pi_In, pi_Out]
        
def main():

    doubling = int(input('Double the original 6 sides how many times?: '))
    
    print('Last 10 iterations... \n')

    #Formatting for table output

    print('{:<25} {:<25} {:25} '.format('Sides', 'LowerBound', 'UpperBound'))

    for i in range(doubling):

        n = int(archPi(i)[1])
        lower = archPi(i)[2]
        upper = archPi(i)[3]

    #Following if statement prints out only last 10 iterations

        if i >= (doubling - 10) and i < doubling:
            print('{:<25} {:<25} {:<25}'.format(n, lower, upper))

    print('\nApproximate Pi = %.8f' % archPi(doubling)[0])

main()  
