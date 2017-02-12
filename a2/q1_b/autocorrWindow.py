import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

#my implementation of autocorrelation calculation - acc wikipedia
#frequency calculated based on zero lag and next peak.
def computeAutoCorrelationFrequency(fs,currWindow,windowSize):
	numberOfIterations = windowSize;
	sizeOfWindowCorrelation = 2*windowSize-1;
	autocorrelation = np.zeros(sizeOfWindowCorrelation,);
	autocorrelationIndex = 0;
	aux = 0;
	indexOfLastElement = len(currWindow)-1;
	for i in range (0,numberOfIterations): 
		for k in range(0,numberOfIterations):
			if aux > windowSize-1: #like 'mod'
				aux = 0;
			multiplier = currWindow[indexOfLastElement]; #take last element
			result = multiplier * currWindow[k]; 
			autocorrelation[autocorrelationIndex+aux] += result;
			aux += 1;
		indexOfLastElement -= 1;	
		autocorrelationIndex +=1;
	zero_lag = np.argmax(autocorrelation);
	new_autocorr = autocorrelation[zero_lag+150:];
	next_peak = np.argmax(new_autocorr)+zero_lag+150;
	sampling_T = float(1.0/fs);
	period_T_in_Signal = float(next_peak - zero_lag + 1); 
	period_inSeconds = period_T_in_Signal*sampling_T;
	fs_in_signal = float(1.0/period_inSeconds);	
	return fs_in_signal;

def computeAutoCorrelationFrequencyLibrary(fs,currWindow,windowSize):
	autocorrelation = np.correlate(currWindow,currWindow,mode = 'full');
	zero_lag = np.argmax(autocorrelation);
	new_autocorr = autocorrelation[zero_lag+150:]; 
	next_peak = np.argmax(new_autocorr)+zero_lag; 
	sampling_T = float(1.0/fs);
	period_T_in_Signal = float(next_peak - zero_lag + 1); 
	period_inSeconds = period_T_in_Signal*sampling_T;
	fs_in_signal = float(1.0/period_inSeconds);
	return fs_in_signal;