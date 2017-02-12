import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

class autoCorrelationSum():
	
	def main():
		#read in a signal
		
		signal1 = mir.Signal();
		signal1.wav_read("../q1audioSignals/thisPart.wav");
		
		sizeOfAutoCorrelation = 2*len(signal1.data)-1;
		numberOfIterations = len(signal1.data);

		autocorrelation = np.zeros(sizeOfAutoCorrelation,);
		autocorrelationIndex = 0;
		aux = 0;
		indexOfLastElement = len(signal1.data)-1;
		
		for i in range (0,numberOfIterations): 
			for k in range(0,numberOfIterations):
				
				if aux > 2:
					aux = 0;
				
				multiplier = signal1.data[indexOfLastElement]; #take last element
				result = multiplier * signal1.data[k]; #multiply that by the whole input in order
												 #element by element
				#for this element, we need to correctly place it at an offset from the start
				#of autocorrelation
				
				
				autocorrelation[autocorrelationIndex+aux] += result;
				aux += 1;
				
			indexOfLastElement -= 1;	
			autocorrelationIndex +=1;
			
																			
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