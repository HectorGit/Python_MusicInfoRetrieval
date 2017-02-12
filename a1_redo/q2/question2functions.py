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
	freq = np.fft.fft(signal.data,sizeOfFFT)/len(signal.data);
	real_part = np.real(freq);
	imag_part = np.imag(freq);
	magn_spectrum = np.abs(real_part,imag_part);
	magn_spectrum = 20*np.log(magn_spectrum);
	lin_space = np.linspace(0,sizeOfFFT/2,sizeOfFFT/2);
	plt.ylabel('Amplitude in dB');
	plt.xlabel('Frequency BIN (x Freq resolution = 21.53Hz)')
	plt.title('MagnitudeSpectrum');
	plt.stem(lin_space, magn_spectrum[:sizeOfFFT/2],'r'); 
	
def plotWindowedAndNonWindowed(signal,sizeOfFFT,hanningWindow):
	plt.title("Bin NotWindowed");
	plotMagnitudeSpectrum(signal,sizeOfFFT);
	plt.show();
		
	plt.title("Bin Windowed")
	windowSignal(signal,hanningWindow);
	plotMagnitudeSpectrum(signal,sizeOfFFT);
	plt.show();