import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

def windowSignal(signal,windowingFunction):
		sizeOfSignal = len(signal.data);
		for i in range (0, sizeOfSignal):
			signal.data[i] = signal.data[i]*windowingFunction[np.mod(i, len(windowingFunction))];
			
def plotMagnitudeSpectrum(signal,sizeOfFFT):		
	freq = np.fft.fft(signal.data,sizeOfFFT)/len(signal.data)*1.0; #normalized by N
	real_part = np.real(freq);
	imag_part = np.imag(freq);
	magn_spectrum = np.abs(real_part,imag_part);
	lin_space = np.linspace(0,(44100)/2,sizeOfFFT/2);#sizeOfFFT/2); #same linspace to possibly obtain same plot.
	plt.ylabel('Amplitude in dB');
	plt.xlabel('Frequency in Hz')
	plt.title('MagnitudeSpectrum');
	plt.stem(lin_space, magn_spectrum[:sizeOfFFT/2],'r'); #magn_spectrum[:sizeOfFFT/2],'r');