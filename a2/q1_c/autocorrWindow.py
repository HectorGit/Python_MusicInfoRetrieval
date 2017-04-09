import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

def computeAutoCorrelationFrequencyLibrary(fs,currWindow,windowSize):
	autocorrelation = np.correlate(currWindow,currWindow,mode = 'full');
	zero_lag = np.argmax(autocorrelation);
	new_autocorr = autocorrelation[zero_lag+150:]; 
	next_peak = np.argmax(new_autocorr)+zero_lag+150; 
	sampling_T = float(1.0/fs);
	period_T_in_Signal = float(next_peak - zero_lag + 1); 
	period_inSeconds = period_T_in_Signal*sampling_T;
	fs_in_signal = float(1.0/period_inSeconds);
	return fs_in_signal;