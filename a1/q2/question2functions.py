import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

def windowSignal(signal,windowingFunction):
		numberOfWindows = int(len(signal.data)/len(windowingFunction));
		windowSize = len(windowingFunction);
		for i in range (0, numberOfWindows):
			currentSamples = signal.data[:windowSize];
			signal.data[:windowSize] = np.multiply(currentSamples,windowingFunction);
			
def plotMagnitudeSpectrum(signal,sizeOfFFT):		
	freq = np.fft.fft(signal.data,sizeOfFFT)/len(signal.data);
	magn_spectrum = np.abs(freq);
	#loudest = np.amax(magn_spectrum);
	magn_spectrum = 20*np.log10(magn_spectrum);
	lin_space = np.linspace(0,sizeOfFFT/2,sizeOfFFT/2);
	plt.ylabel('Amplitude in dB');
	plt.xlabel('Frequency bin')
	#plt.title('MagnitudeSpectrum');
	plt.plot(lin_space, magn_spectrum[:sizeOfFFT/2],'r'); 
	plt.show();
	
def plotMagnitudeSpectrumReduced(signal,sizeOfFFT):		
	freq = np.fft.fft(signal.data[:2048],sizeOfFFT)/2048;
	magn_spectrum = np.abs(freq);
	#loudest = np.amax(magn_spectrum);
	magn_spectrum = 20*np.log10(magn_spectrum);
	lin_space = np.linspace(0,sizeOfFFT/2,sizeOfFFT/2);
	plt.ylabel('Amplitude in dB');
	plt.xlabel('Frequency bin')
	#plt.title('MagnitudeSpectrum');
	plt.plot(lin_space, magn_spectrum[:sizeOfFFT/2],'r'); 
	plt.show();	
	
def plotWindowedAndNonWindowed(signal,sizeOfFFT,hanningWindow):
	plotMagnitudeSpectrum(signal,sizeOfFFT);
		
	windowSignal(signal,hanningWindow);
	plotMagnitudeSpectrum(signal,sizeOfFFT);
