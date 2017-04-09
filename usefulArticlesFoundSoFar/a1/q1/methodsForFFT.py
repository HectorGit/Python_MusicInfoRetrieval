import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt
#import matplotlib.axes as ax


def dftByHector(factor,numberOfBins,sign,inputSamples):
	
	re_in = inputSamples;
	im_in = np.zeros(len(inputSamples),);

	real_part = np.zeros (numberOfBins,);
	imaginary_part = np.zeros (numberOfBins,);		
											
	sizeOfBinInHertz = (44100/2)/float(numberOfBins); 
	print 'sizeOfBinInHertz'
	print sizeOfBinInHertz;
					
	for i in range (0,numberOfBins):	
		
		temp_cosine = mir.Sinusoid(duration = sign.duration, freq = i*sizeOfBinInHertz , phase = np.pi/2); 
		                                                                                                   
		temp_sine = mir.Sinusoid(duration = sign.duration, freq = i*sizeOfBinInHertz , phase = 0);         
		
		#found reference at https://www.nayuki.io/page/how-to-implement-the-discrete-fourier-transform
		
		for j in range (0,len(inputSamples)): 
			real_part[i] += (re_in[j] * temp_cosine.data[j]) + (im_in[j] * temp_sine.data[j]); #calculates the sum per bin k
			imaginary_part[i] += (-1 * re_in[j] * temp_sine.data[j]) + (im_in[j] * temp_cosine.data[j]);
		
	plotDFT(factor,numberOfBins, sign,real_part,imaginary_part);
	
	#--------------
	return 0;
		
def plotMagnitudeSpectrum(factor,numberOfBins, sign,real_part,imaginary_part):
			
	magnitude_spectrum = np.zeros (numberOfBins,);														

	for i in range(0,numberOfBins):
		magnitude_spectrum[i] = np.sqrt(imaginary_part[i]**2+real_part[i]**2);		
		magnitude_spectrum[i] = magnitude_spectrum[i]/(len(sign.data));
	
	arr2 = magnitude_spectrum;
	
	#arr1 = np.linspace(0,(44100)/2,numberOfBins);
	arr1 = np.linspace(0,numberOfBins,numberOfBins); 

	plt.ylabel('Amplitude in dB');
	plt.xlabel('Frequency Bin(mult by 100Hz)')
	plt.title('MagnitudeSpectrum');
	plt.stem(arr1,arr2);
	return 0;

def plotPhaseSpectrum(factor,numberOfBins, sign,real_part,imaginary_part):
	phase_spectrum = np.zeros (numberOfBins,);														
	
	for i in range (0,numberOfBins):
		phase_spectrum[i] = np.arctan2(imaginary_part[i],real_part[i]);	
			
	arr4 = phase_spectrum;
	#arr3 = np.linspace(0,(44100)/2,numberOfBins); 
	arr3 = np.linspace(0,numberOfBins,numberOfBins); 


	plt.title('PhaseSpectrum');
	plt.ylabel('Phase in Radians');
	plt.xlabel('Frequency Bin (mult by 100 Hz)');
	plt.stem(arr3,arr4);
	return 0;
	
	
def plotDFT(factor,numberOfBins,sign,real_part, imaginary_part):
	#plotMagnitudeSpectrum(factor,numberOfBins,sign,real_part, imaginary_part);
	print 'Yo printing stuff'
	plotPhaseSpectrum(factor,numberOfBins,sign,real_part,imaginary_part);
	plt.show();
	return 0;	
