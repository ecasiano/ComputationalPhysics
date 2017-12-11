#Check out the forward, center and second derivatives

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.log(x)

def df(f,x):
    '''Compute the forward, centered and 2nd derivative of f = ln(x)'''
    dx = x[1]-x[0]

    dff = (f(x+dx) - f(x)) / dx
    dcf = (f(x) - f(x-dx)) / dx
    d2f = (f(x+dx) - f(x-dx)) / 2*dx

    return dff,dcf,d2f

def main():

    N = 10
    x = np.linspace(2,3,N)
    dff,dcf,d2f = df(f,x)

    fig, axes = plt.subplots(2,1,sharex=True, sharey=False, squeeze=True, figsize=(5,7))


    axes[0].plot(x,1/x, lw=1, label=r'$1/x$')
    axes[0].plot(x,dff,'s', mfc='None', ms=5, label='Forward Derivative')
    axes[0].plot(x,dcf,'o', mfc='None', ms=5, label='Centered Derivative')

    axes[0].set_ylabel("f'(x)")
    axes[0].legend()
    axes[0].set_xlim(2,3)

    axes[1].plot(x,-1/(x*x), lw=1, label=r'$-1/x^2$')
    axes[1].plot(x,d2f,'o', mfc='None', ms=5, label='2nd Centered Derivative')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel("f''(x)")
    axes[1].legend(loc='lower right')

    plt.show()
if __name__ == '__main__':
    main()
