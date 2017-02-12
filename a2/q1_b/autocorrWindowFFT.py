import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

def computeAutoCorrelationFrequencyFFT(fs,currWindow,windowSize):
	re_in = currWindow;
	im_in = np.zeros(len(re_in),);														
	spectrum = np.fft.rfft(re_in);
	mult_freq_domain = spectrum * np.conj(spectrum);
	autocorrelation = np.fft.irfft(mult_freq_domain);
	#autocorrelation = autocorrelation[:int(len(autocorrelation/2))];
	zero_lag = 0;
	next_peak = np.argmax(autocorrelation[zero_lag+50:])+zero_lag+50;
	sampling_T = float(1.0/fs);
	period_T_in_Signal = float(next_peak - zero_lag + 1); 
	period_inSeconds = period_T_in_Signal*sampling_T;
	fs_in_signal = float(1.0/period_inSeconds);		
	return fs_in_signal;
	