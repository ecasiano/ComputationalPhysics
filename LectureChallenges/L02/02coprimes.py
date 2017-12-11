#Lecture Challenge 2: Determine if two integers are coprime

#The following function takes two numbers as arguments
#and returns True if they're coprime and False if not.

#NOTE: Used syntax resembling  C++ (i.e, defining a main() function) for practice

def isCoprime(A, B):

    A = int(abs(A)) #Absolute value used in case the input is a negative integer
    B = int(abs(B))  
        
    factorsA = []
    factorsB = []
    
    if A < B:      #Variable swap if 1st entry < 2nd entry so the % operator will not yield a zero always
        A, B = B, A
        
    if A == 1 or B == 1 or A == 0 or B == 0: #Trivial cases
            coprime = False

    else:
        for i in range(2, A+1, 1):
            if A % i == 0:
                factorsA.append(i)

        for j in range(2, B+1, 1):
            if B % j == 0:
                factorsB.append(j)

        for k in factorsA:
            if k in factorsB: #If k is found inside factorsB, returns a True
                coprime = False
                break

            else:
                coprime = True
    
    return coprime

def main():

    #User input

    A,B = map(int, input('Enter two integers separated by a space: ').split())

    if isCoprime(A,B) == True:
        print('The integers %d and %d are COPRIME.' % (A,B))

    else:
        print('The integers %d and %d are NOT COPRIME.' % (A, B))

    return 0

main()
