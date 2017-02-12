import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

def getPeak(non_Aliasing_Points,sign,inputSamples, sizeOfFFT, windowSize):

	#print 'entering getPeak';

	re_in = inputSamples;
	im_in = np.zeros(len(inputSamples),);
	real_part = np.zeros (non_Aliasing_Points,);
	imaginary_part = np.zeros (non_Aliasing_Points,);									
	sizeOfBinInHertz = 44100.0/sizeOfFFT; 
	
	#print 'entering for loop';
	
	for i in range (0,non_Aliasing_Points):	
		
		temp_cosine = mir.Sinusoid(duration = sign.duration, freq = i*sizeOfBinInHertz , phase = np.pi/2);                                                                                   
		temp_sine = mir.Sinusoid(duration = sign.duration, freq = i*sizeOfBinInHertz , phase = 0);         
				
		for j in range (0,len(inputSamples)): 
			real_part[i] += (re_in[j] * temp_cosine.data[j]);# + (im_in[j] * temp_sine.data[j]); 
			imaginary_part[i] += (re_in[j] * temp_sine.data[j]);#(-1 * re_in[j] * temp_sine.data[j]);# + (im_in[j] * temp_cosine.data[j]);
			
	#print 'finished for loop';

				
	fft_data = real_part + 1j * imaginary_part; #making it complex to facilitate the calculation of magnitude_spectrum
												#need to make it same length as magnitude_spectrum
	
	fft_data = fft_data[:non_Aliasing_Points]/len(inputSamples); #is this valid?
																		
	magnitude_spectrum = np.abs(fft_data);
	
	#print len(magnitude_spectrum);
	#xAxis = np.linspace(0,non_Aliasing_Points,non_Aliasing_Points);
	#print len(xAxis);
	
	#plt.stem(xAxis,magnitude_spectrum);
	#plt.show();
	
	peakFrequencyBin = np.argmax(magnitude_spectrum);
	
	#print 'about to return frequencyBin';
	#print peakFrequencyBin;
	#print 'about to return frequencyBin';

	return peakFrequencyBin;
		


