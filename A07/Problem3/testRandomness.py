#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt

def lcg_rand(a,c,m,seed,N=1):
    '''A linear congruential pseudrandom number generator'''
    x = np.zeros([N])
    X = seed
    x[0] = X/m
    for n in range(N-1):
            X = (a*X + c) % m
            x[n+1] = X/m
    return x

def main():

    #LCG Results
    N = 1000
    a = 6
    c = 7
    m = 2**31-1
    seed = 3
    x = lcg_rand(a,c,m,seed,N) 
    print(x)

    #Plot LCG Results
    xvals = np.array([])
    yvals = np.array([])
    for i in range(np.size(x)-1):
        xvals = np.append(xvals,x[i])
        yvals = np.append(yvals,x[i+1])

    plt.plot(xvals,yvals,'ko',label='LCG')

    #Plot np.random.random results
    npxvals = np.array([])
    npyvals = np.array([])
    npList = np.random.random(N)

    for i in range(np.size(npList)-1):
        npxvals = np.append(npxvals,npList[i])
        npyvals = np.append(npyvals,npList[i+1])
    plt.plot(npxvals,npyvals,'ro',label='np.random.random()')

    plt.title('LCG vs. np.random.random comparison, LCG multiplier = 6')
    plt.legend(loc = 'upper right')
    plt.xlabel('$r_{i}$')
    plt.ylabel('$r_{i+1}$')
    plt.savefig('LCG_vs_nprand.png')
    plt.show()

    #Modify LCG parameters to get more randomized values
    a = 100
    c = 7
    m = 2**31-1
    seed = 3
    x = lcg_rand(a,c,m,seed,N) 

    #Plot modified LCG results

    xvals = np.array([])
    yvals = np.array([])
    for i in range(np.size(x)-1):
        xvals = np.append(xvals,x[i])
        yvals = np.append(yvals,x[i+1])

    plt.plot(xvals,yvals,'ko',label='LCG')
    plt.plot(npxvals,npyvals,'ro',label='np.random.random()')

    plt.title('LCG vs. np.random.random comparison, LCG multiplier = 100')
    plt.legend(loc = 'upper right')
    plt.xlabel('$r_{i}$')
    plt.ylabel('$r_{i+1}$')
    plt.savefig('LCGmod_vs_nprand.png')
    plt.show()

if __name__ == '__main__':
    main()
