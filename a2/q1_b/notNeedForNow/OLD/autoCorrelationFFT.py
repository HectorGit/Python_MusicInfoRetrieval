import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

class autoCorrelationFFT():
	
	def main():
		#read in a signal
		
		signal1 = mir.Signal();
		signal1.wav_read("../q1audioSignals/thisPart.wav");
		
		#http://dsp.stackexchange.com/questions/386/autocorrelation-in-audio-analysis
		
		spectrum = np.fft.rfft(signal1.data);
		print 'spectrum';
		print spectrum[0];

		mult_freq_domain = spectrum * np.conj(spectrum);
		print 'mult_freq_domain';
		print mult_freq_domain[0];

		autocorrelation = np.fft.irfft(mult_freq_domain);
		print 'autocorrelation';
		print autocorrelation[0];
		autocorrelation = np.absolute(autocorrelation);
		print 'autocorrelation Magnitude';
		print autocorrelation[0];
		
		#need to find zeroeth peak - which is where the input 
		#matches the shifted copy exactly. ->GLOBAL MAXIMUM
		#find argmax
		
		maxValue = np.max(autocorrelation);
		print 'maxValue'
		print maxValue;
		
		zero_lag = np.argmax(autocorrelation);
		print 'zero_lag'
		print zero_lag;
		
		#then find the next peak from that - calculate the period
		#then lastly f = 1/T. -> TA DA.
		#find argmax after previous argmax
		next_peak = np.argmax(autocorrelation[zero_lag:])+zero_lag; #haahha cheater
		print 'next_peak'
		print next_peak;
		
		
		fs = 44100; 
		sampling_T = float(1/44100.0);#???
		period_T_in_Signal = next_peak - zero_lag + 1; # +1?
		fs_in_signal = 1/period_T_in_Signal;
		
		print 'fs is (Hz)';
		print fs_in_signal;
		
		plt.plot(autocorrelation);
		plt.show();
	
		return 0;
		

	if __name__ == "__main__": main()