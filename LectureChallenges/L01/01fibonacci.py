# Asks the user for the Nth fibonacci number and displays all fibonacci numbers up to that one

# Parameters

N = int(input('Enter the amount of Fibonacci numbers that you want to see: '))

fibNumbers = [0, 1]

for i in range(N-2):
	nextFib = fibNumbers[i] + fibNumbers[i+1]
	fibNumbers.append(nextFib)

print(('The first %g Fibonacci numbers are: ' % N), fibNumbers) 


