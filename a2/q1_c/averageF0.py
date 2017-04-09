import mir
import getPeak
import autocorrWindow
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

class averageF0():
	def main():
		signal1 = mir.Signal();
		signal1.wav_read("../q1audioSignals/qbhexamplesB.wav");
		sizeOfFFT = 2048;
		windowSize = 2048;
		non_Aliasing_Points = sizeOfFFT/2;
		sizeOfBin = 44100.0/sizeOfFFT;
		numberOfWindows = int(np.floor(len(signal1.data)/windowSize));
		fs = 44100.0;
		t = windowSize/fs;
		fundamentals = np.zeros(numberOfWindows,);
		for i in range (0,numberOfWindows): 
			hanning = np.hanning(2048);
			inputSamples = signal1.data[int(i*windowSize):int((i+1)*windowSize)];
			inputSamples = np.multiply(hanning,inputSamples);
			peakBin = getPeak.getPeakFFT(inputSamples, windowSize);
			peakFrequencyFFT = peakBin*sizeOfBin;
			peakFrequencyAutoCorr = autocorrWindow.computeAutoCorrelationFrequencyLibrary(fs,inputSamples,windowSize);
			fundamentals[i] = (peakFrequencyFFT+peakFrequencyAutoCorr)/2.0;
			if fundamentals[i] >= (fs/2): fundamentals[i] = 0;
		xAxis = np.linspace(0,numberOfWindows*t,numberOfWindows); 
		plt.stem(xAxis,fundamentals);
		plt.xlabel('Time in seconds - 0.05s per FFT window');
		plt.ylabel('Frequency of the Fundamental in Hz.');
		plt.show();
		return 0;
	if __name__ == "__main__": main()