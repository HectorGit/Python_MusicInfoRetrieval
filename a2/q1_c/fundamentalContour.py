import mir
import getPeak
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class fundamentalContour():
	
	def main():
	
		#read in a signal
		signal1 = mir.Signal();
		signal1.wav_read("../q1audioSignals/qbhexamplesB.wav");
			 
		sizeOfFFT = 2048;
		windowSize = 2048;
		non_Aliasing_Points = sizeOfFFT/2;
		sizeOfBin = 44100.0/sizeOfFFT;

		#compute the FFT for N windows that fit the audio input.
		#for each FFT, take the peak in the magnitude spectrum, and put it in the list.
		
		numberOfWindows = int(np.floor(len(signal1.data)/windowSize));
		#print numberOfWindows;
		
		t = windowSize/44100.0;
		
		fundamentals = np.zeros(numberOfWindows,);
		
		for i in range (0,numberOfWindows): #for each window, calculate the peak freq.
			hanning = np.hanning(2048);
			inputSamples = signal1.data[int(i*windowSize):int((i+1)*windowSize)];
			inputSamples = np.multiply(hanning,inputSamples);
			#peakBin = getPeak.getPeak(non_Aliasing_Points,signal1,inputSamples,sizeOfFFT,windowSize);
			peakBin = getPeak.getPeakFFT(inputSamples, windowSize);
			peakFrequency = peakBin*sizeOfBin;
			fundamentals[i] = peakFrequency;
			if fundamentals[i] >= 1000: fundamentals[i] = 0;
			#print '------------------------------------------------------------------------';

		
		xAxis = np.linspace(0,numberOfWindows*t,numberOfWindows); #advancing 0.05 for every FFT window  (Start stop step) linspace(start stop numpoints)
		#print len(xAxis);
		#print len(fundamentals);
		plt.stem(xAxis,fundamentals);
		plt.xlabel('Time in seconds - 0.05s per FFT window');
		plt.ylabel('Frequency of the Fundamental in Hz.');
		plt.show();
	
		return 0;
		

	if __name__ == "__main__": main()