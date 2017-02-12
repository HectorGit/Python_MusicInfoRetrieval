import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class ClosestBins():

	def main():
		
		SizeOfBin = 100.27;
		NumBin1 = 19;
		NumBin2 = 20;
		BasisFreq1  = float(NumBin1*SizeOfBin); #~500
		BasisFreq2 = float(NumBin1*SizeOfBin);
		TestFreq = 2000.0; #fundamentalOfMixtureSignal
		
		testSine = mir.Sinusoid(freq = TestFreq);
		sine1 = mir.Sinusoid(freq = BasisFreq1);#sign); #this calls __init__ automatically
		cosine1 = mir.Sinusoid(freq = BasisFreq1, phase = np.pi/2);#sign); #this calls __init__ automatically
		sine2 = mir.Sinusoid(freq = BasisFreq2);#sign); #this calls __init__ automatically
		cosine2 = mir.Sinusoid(freq = BasisFreq2, phase = np.pi/2);#sign); #this calls __init__ automatically

		lengthOfCycle1 = float(1/BasisFreq1); #seconds 0.002
		lengthOfCycle2 = float(1/BasisFreq2);
		
		Fs = 44100.0;
		
		numSamplesPerCycle1 = (Fs*lengthOfCycle1); 
		numSamplesPerCycle2 = (Fs*lengthOfCycle2);
							
		arr1 = np.linspace(0.0,lengthOfCycle1,numSamplesPerCycle1);	#start,stop,n
		print 'size'
		print arr1.shape;
		arr2 = sine1.data[:np.int(numSamplesPerCycle1)]; 
		arr2 = np.multiply(arr2,cosine1.data[:np.int(numSamplesPerCycle1)]);
		arr2 = np.multiply(arr2,testSine.data[:np.int(numSamplesPerCycle1)]);
		plt.title('Multiplication of 2000HZ sin with Sine and Cos For Bin 5');
		plt.ylabel('Amplitude');
		plt.xlabel('Time');
		plt.plot(arr1,arr2);
		plt.show();
		
		arr3 = np.linspace(0.0,lengthOfCycle2,numSamplesPerCycle2);	#start,stop,n
		print 'size'
		print arr1.shape;
		arr4 = sine2.data[:np.int(numSamplesPerCycle2)]; 
		arr4 = np.multiply(arr2,cosine2.data[:np.int(numSamplesPerCycle2)]);
		arr4 = np.multiply(arr2,testSine.data[:np.int(numSamplesPerCycle2)]);
		plt.title('Multiplication of 2000Hz sin with Sin and Cos for Bin 21');
		plt.ylabel('Amplitude');
		plt.xlabel('Time');
		plt.plot(arr3,arr4);
		plt.show();
		
		return 0;

	if __name__ == "__main__": main()