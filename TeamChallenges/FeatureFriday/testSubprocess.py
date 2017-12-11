#Runs the testArgParse.py with different command-line arguments
#NOTE: Both files should be in the same directory

import subprocess

for N in range(2000000):
    N = str(N)   #Changes N to a string so we can "write it" in the command-line
    
    subprocess.run(['python', 'testArgParse.py', N])
