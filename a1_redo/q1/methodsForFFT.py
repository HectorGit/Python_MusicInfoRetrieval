import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

def dftByHector(non_Aliasing_Points,sign,inputSamples):
	re_in = inputSamples;
	im_in = np.zeros(len(inputSamples),);
	real_part = np.zeros (non_Aliasing_Points,);
	imaginary_part = np.zeros (non_Aliasing_Points,);									
	sizeOfBinInHertz = 44100.0/1024.0; 
					
	for i in range (0,non_Aliasing_Points):	
		temp_cosine = mir.Sinusoid(duration = sign.duration, freq = i*sizeOfBinInHertz , phase = np.pi/2);                                                                                   
		temp_sine = mir.Sinusoid(duration = sign.duration, freq = i*sizeOfBinInHertz , phase = 0);         
				
		for j in range (0,len(inputSamples)): 
			real_part[i] += (re_in[j] * temp_cosine.data[j]) + (im_in[j] * temp_sine.data[j]); #calculates the sum per bin k
			imaginary_part[i] += (-1 * re_in[j] * temp_sine.data[j]) + (im_in[j] * temp_cosine.data[j]);
		
	plotDFT(non_Aliasing_Points, sign,real_part,imaginary_part);
	
	return 0;
		
def plotMagnitudeSpectrum(non_Aliasing_Points, sign,real_part,imaginary_part):
			
	magnitude_spectrum = np.zeros (non_Aliasing_Points,);														

	for i in range(0,non_Aliasing_Points):
		magnitude_spectrum[i] = np.sqrt(imaginary_part[i]**2+real_part[i]**2);		
		magnitude_spectrum[i] = magnitude_spectrum[i]/(len(sign.data));
	
	arr2 = magnitude_spectrum;
	arr1 = np.linspace(0,non_Aliasing_Points,non_Aliasing_Points); 
	print 'length(arr1)';
	print len(arr1);
	plt.ylabel('Amplitude in dB');
	plt.xlabel('Frequency Bin(mult by ~43.1 Hz)')
	plt.title('MagnitudeSpectrum');
	plt.stem(arr1,arr2);
	return 0;

def plotPhaseSpectrum(non_Aliasing_Points, sign,real_part,imaginary_part):
	phase_spectrum = np.zeros(non_Aliasing_Points,);	

	compl_array = real_part + 1j * imaginary_part; #cheating using complex numbers
	threshold = np.max(np.abs(compl_array))/10000;
	#X2(abs(X)<threshold) = 0; %maskout values that are below the threshold
	
	for i in range(0, non_Aliasing_Points):
		if compl_array[i] < threshold:
			real_part[i] = 0;
			imaginary_part[i] = 0;
	
	for i in range (0,non_Aliasing_Points):
		phase_spectrum[i] = np.arctan2(imaginary_part[i],real_part[i]);#*180/np.pi;			
		
	arr4 = phase_spectrum;
	arr3 = np.linspace(0,non_Aliasing_Points,non_Aliasing_Points); 
	plt.title('PhaseSpectrum');
	plt.ylabel('Phase in Radians');
	plt.xlabel('Frequency Bin (mult by ~43.1 Hz)');
	plt.stem(arr3,arr4);
	return 0;
	
def plotDFT(non_Aliasing_Points,sign,real_part, imaginary_part):
	#plotMagnitudeSpectrum(non_Aliasing_Points,sign,real_part, imaginary_part);
	#plt.show();
	plotPhaseSpectrum(non_Aliasing_Points,sign,real_part,imaginary_part);
	plt.show();
	return 0;	
