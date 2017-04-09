import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class BasisFunctions():

	def main():
		
		SizeOfBin = 100.27;
		NumBin = 20;
		BasisFreq  = float(NumBin*SizeOfBin); #~500
		print 'basisFreq';
		print BasisFreq;
		#TestFreq = 2000.0;
		
		testSine = mir.Sinusoid(freq = TestFreq);
		sine1 = mir.Sinusoid(freq = BasisFreq);#sign); #this calls __init__ automatically
		cosine1 = mir.Sinusoid(freq = BasisFreq, phase = np.pi/2);#sign); #this calls __init__ automatically

		lengthOfCycle = float(1/BasisFreq); #seconds 0.002
		print 'lengthOfCycle'
		print lengthOfCycle;
		
		Fs = 44100.0;
		t = BasisFreq/Fs;
		
		numSamplesPerCycle = (Fs*lengthOfCycle); #since we sample 44100 times per 1 second, we sample x times for 0.002 seconds
		#   44100/1 = x/0.002 =>  x = (44100/1)(0.002) = 44100 * lengthOfCycle ~about 88 samples.;
		print 'numSamplesPerCycle';
		print numSamplesPerCycle;
							
		arr1 = np.linspace(0.0,lengthOfCycle,numSamplesPerCycle);	#start,stop,n
		print 'size'
		print arr1.shape;
		arr2 = sine1.data[:numSamplesPerCycle]; 
		print 'size2'
		print arr2.shape;
		arr3 = cosine1.data[:numSamplesPerCycle]; #each of these has to have len 44100 bc
		print 'size3'
		print arr3.shape;
							 #they last 1 second by default.
		
		plt.title('Basis Functions for Bin 20');
		plt.ylabel('Amplitude');
		plt.xlabel('Time');
		plt.plot(arr1,arr2);
		plt.plot(arr1,arr3);

		plt.show();
		
		return 0;

	if __name__ == "__main__": main()