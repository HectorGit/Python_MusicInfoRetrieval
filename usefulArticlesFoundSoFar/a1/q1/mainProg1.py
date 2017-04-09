import mir
import methodsForFFT
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class mainProg1():
	
	def main():
	
		#---------plotting with self implemented DFT-----------------------------------#
		#------------------------------------------------------------------------------#
		#------------------------------------------------------------------------------#
	
		#PART A - test with harmonically related sinusoids.
		sine1 = mir.Sinusoid(amp = 1,freq = 2000.0,phase = 0);
		sine2 = mir.Sinusoid(amp = 0.5,freq = 4000.0, phase = np.pi/4);
		sine3 = mir.Sinusoid(amp = 0.25,freq = 8000.0, phase = np.pi/2);
		signal = mir.Mixture(sine1,sine2,sine3);
		#PART A - test with harmonically related sinusoids.

		#PART B - test with sinusoid exactly at a Bin.
		#signal = mir.Sinusoid(freq = 50.0*100.227272727); #100.227 is the calculates size
		                                                   # of a single bin in Hz
		#PART B - test with sinusoid exactly at a Bin.
		
		#PART C - test with sinusoid between Bins.
		#signal = mir.Sinusoid(freq = 50.5*100.227272727); #100.227 is the calculates size
		                                                   # of a single bin in Hz
		#PART C - test with sinusoid between Bins.
		
		factor = 100; #this reduces the size of the DFT to a fraction of the length of 
					  #the input
		inputSamples = signal.data;		
	
		sizeOfFFT = len(inputSamples)/factor; #size of fft ( k = N , in this case)
		numberOfBins = sizeOfFFT/2;

		#PART A - test with harmonically related sinusoids.
		methodsForFFT.dftByHector(factor,numberOfBins,signal,inputSamples);
		#PART A - test with harmonically related sinusoids.

		#PART B - test with sinusoid exactly at a Bin.
		#methodsForFFT.dftByHector(factor,numberOfBins,signal,inputSamples);
		#PART B - test with sinusoid exactly at a Bin.
		
		#PART C - test with sinusoid between Bins.
		#methodsForFFT.dftByHector(factor,numberOfBins,signal,inputSamples);
		#PART C - test with sinusoid between Bins.
		
		#----------------'plotting with library function for DFT'----------------------#
		#------------------------------------------------------------------------------#
		#------------------------------------------------------------------------------#

		freq = np.fft.fft(inputSamples,sizeOfFFT)/numberOfBins;#/len(inputSamples);
		real_part = np.real(freq);
		imag_part = np.imag(freq);
		
		magn_spectrum = np.absolute(freq);

		
		phase_spectrum = np.zeros(numberOfBins,);
		for i in range (0,numberOfBins):
			phase_spectrum[i] = np.arctan2(imag_part[i],real_part[i]);
		
		lin_space = np.linspace(0,(44100)/2,numberOfBins);

		#plt.stem(lin_space, magn_spectrum[:numberOfBins],'r');
		#plt.stem(lin_space, phase_spectrum[:numberOfBins],'b');
		
		#plt.show();
		
		return 0;
		

	if __name__ == "__main__": main()