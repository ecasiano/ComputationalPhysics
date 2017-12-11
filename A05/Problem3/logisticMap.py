#Emanuel Casiano-Diaz

import numpy as np
import matplotlib.pyplot as plt

def logisticMap(mu,x):
    return (mu * x * (1.0 - x))


def main():
 
    muLow = 1.0           #Smallest mu value
    muHigh = 4.0          #Largest mu value

    transients = 200      #Number of transients
    iterates = 250        #Number of iterates
    dn = 0.005            #Step size

    for mu in np.arange(muLow,muHigh,dn):
        x0 = 0.5          #Initial x

        for n in range(transients):
            x0 = logisticMap(mu,x0)

        muList = np.array([])       #List where we will store mu values
        xList = np.array([])        #Same as above but for x values

        for n in range(iterates):
            x0 = logisticMap(mu, x0)
            muList = np.append(muList,mu)
            xList = np.append(xList, x0)

        plt.plot(muList,xList,'k,') #'k,' plots black pixels
    
    plt.title('Bifurcation Diagram of Logistic Map')
    plt.xlabel(r'$\mu $')
    plt.ylabel('x')
    plt.annotate('Period Doubling', xy=(3.00,0.67), xytext=(2.0,0.7), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('Chaos', xy=(3.57,0.33), xytext=(3.10,0.22), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.savefig('bifurcationDiagram.png')
    plt.show()

if __name__ == '__main__':
    main()
