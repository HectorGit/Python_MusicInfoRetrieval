import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class BasisFunctions():

	def main():
		
		SizeOfBin = 43.1;
		NumBin = 200;
		TestBin = 100;
		BasisFreq  = float(NumBin*SizeOfBin); 
		print 'basisFreq';
		print BasisFreq;
		TestFreq = TestBin*SizeOfBin;
		testSine = mir.Sinusoid(freq = TestFreq);
		sine1 = mir.Sinusoid(freq = BasisFreq);
		cosine1 = mir.Sinusoid(freq = BasisFreq, phase = np.pi/2);

		lengthOfCycle = float(1/BasisFreq);
		print 'lengthOfCycle'
		print lengthOfCycle;
		
		Fs = 44100.0;
		t = BasisFreq/Fs;
		
		numSamplesPerCycle = (Fs*lengthOfCycle); 
		print 'numSamplesPerCycle';
		print numSamplesPerCycle;
							
		arr1 = np.linspace(0.0,lengthOfCycle,numSamplesPerCycle);	
		
		arr2 = sine1.data[:numSamplesPerCycle]; 
		arr3 = cosine1.data[:numSamplesPerCycle]; 
		arr4 = testSine.data[:numSamplesPerCycle];
		
		plt.title('ONE CYCLE Basis Functions for Bin 30');
		plt.ylabel('Amplitude');
		plt.xlabel('Time (Seconds) ');
		plt.stem(arr1,arr2);
		plt.show();
		plt.stem(arr1,arr3);
		plt.show();
		
		arr5 = np.multiply(arr2,arr4);
		arr6 = np.multiply(arr5,arr3);
	
		plt.title('bin 100 test TIME bin 30 basis');
		plt.ylabel('Amplitude');
		plt.xlabel('Time');
		plt.stem(arr1,arr6);
		plt.show();
		
		return 0;

	if __name__ == "__main__": main()