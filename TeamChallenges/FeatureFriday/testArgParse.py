
#Squares an integer N and prints it to the screen. If --cube flag is selected, returns the cube of N also.

import argparse

#Enables the input of command-line arguments

parser = argparse.ArgumentParser()

#Positional Argument

parser.add_argument('N', type=int, help='The number that you want to square')

#Optional Argument

parser.add_argument('--cube', action='store_true', help='If selected, also returns the cube')

#After adding all your arguments, we use parse_args()

args = parser.parse_args()

#The program output

print(args.N**2)

#The following will be printed if the --cube optional argument is selected

if args.cube:

    print(args.N**3)




