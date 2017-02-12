import mir
import autocorrWindow
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

class acSumSignalWindowed():
	def main():
		signal1 = mir.Signal();
		signal1.wav_read("../q1audioSignals/outMelody.wav");
		fs = 44100;
		windowSize = 2048; #at a 44100 Hz Fs.
		numberOfWindows = int(np.floor(len(signal1.data)/windowSize));
		frequencies = np.zeros(numberOfWindows,);
		for  i in range (0,numberOfWindows): #-1?
			currWindow = signal1.data[i*windowSize:(i+1)*windowSize];
			frequencies[i] = autocorrWindow.computeAutoCorrelationFrequency(fs,currWindow,windowSize);															
		xAxis = np.linspace(0,numberOfWindows,numberOfWindows);
		plt.stem(xAxis,frequencies);
		plt.xlabel('Time ~0.05 s per result');
		plt.ylabel('Frequency in Hz');
		plt.show();
		return 0;
	if __name__ == "__main__": main()