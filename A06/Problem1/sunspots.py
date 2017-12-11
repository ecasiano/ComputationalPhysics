#Emanuel Casiano-Diaz
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.constants import pi

def linRegression(xList, yList):
	#Do (least squares)linear fitting
	slope, intercept, r_value, p_value, std_err = linregress(xList,yList)

	linFitList = np.array([])
	for x in xList:
		linFitList = np.append(linFitList, slope*x + intercept)

	return(xList,linFitList,slope,intercept,std_err)

def powerSpectra(y, t):
    yHat = np.fft.fft(y)
    power = np.absolute(yHat)
    
    time_step = 1/30
    frequencies = np.fft.fftfreq(yHat.size, time_step)
    
    return(frequencies, power)



def main():

    #Import data
    data = np.loadtxt('SN_m_tot_V2.0.txt')
    timeList = data[:,2]
    sunspotList = data[:,3]

    #Plot Monthly Sunspot Number vs Time
    plt.plot(timeList, sunspotList, 'b')
    plt.title('Monthly Sunspot Number')
    plt.xlabel('Time (Months as fractions of year)')
    plt.ylabel('Mean Sunspots Observed')
    plt.savefig('sunspots.png')
    plt.show()

    #Get linear regression values
    sunspotLinFit = linRegression(timeList, sunspotList)[1]
    m = linRegression(timeList, sunspotList)[2]
    b = linRegression(timeList, sunspotList)[3]

    #Plot original plot + linear fit
    plt.plot(timeList, sunspotList, 'b')
    plt.plot(timeList, sunspotLinFit, 'k', label='y = %f*t + %f'%(m,b))
    plt.legend(loc='best')
    plt.title('Monthly Sunspot Number (LinearFit)')
    plt.xlabel('Time (Months as fractions of year)')
    plt.ylabel('Mean Sunspots Observed')
    plt.savefig('sunspotsWfit.png')
    plt.show()
    print('Standard error is = ', linRegression(timeList,sunspotList)[4])

    #Do Fast-Fourier Transform on the data
    frequencyList = powerSpectra(sunspotList,timeList)[0]
    powerList = powerSpectra(sunspotList,timeList)[1]

    #Plot Power Spectra vs Frequencies
    plt.plot(frequencyList, powerList)
    plt.title('Power Spectra')
    plt.xlabel(r'$\omega$ ($year^{-1}$)')
    plt.ylabel('Power (arb)')
    plt.xlim(-1)
    plt.savefig('powerSpectra.png')
    plt.show()

if __name__ == '__main__':
	main()

