import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

def getPeakFFT(inputSamples, windowSize):
	fft_data = np.fft.fft(inputSamples); 
	magnitude_spectrum = np.absolute(fft_data);
	magnitude_spectrum = magnitude_spectrum[:len(inputSamples)/2];	
	peakFrequencyBin = np.argmax(magnitude_spectrum[:len(magnitude_spectrum)/4]); 
	return peakFrequencyBin;
