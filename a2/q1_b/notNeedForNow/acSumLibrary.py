import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

class acSumLibrary():
	
	def main():
		#read in a signal
		#signal1 = mir.Signal();
		#signal1.wav_read("../q1audioSignals/melodyHectorHigh.wav");
		signal1 = [2,3,-1];
		
		autocorrelation = np.correlate(signal1,signal1, mode = 'full');
		sizeOfAutoCorrelation = len(autocorrelation);
																			
		xAxis = np.linspace(0,sizeOfAutoCorrelation,sizeOfAutoCorrelation); #linspace(start stop numpoints)
																			#arange(Start stop step) 
		print len(xAxis);
		print len(autocorrelation);
		plt.stem(xAxis,autocorrelation);
		plt.xlabel('Time');
		plt.ylabel('Autocorrelation');
		plt.show();
	
		return 0;
		

	if __name__ == "__main__": main()