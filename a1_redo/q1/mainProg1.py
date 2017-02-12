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
	
		#FS = 44100 and DFT size = 1024. Size of Freq Bin is ~43.1 HZ. 
		#Can represent correctly frequencies of up to 22050 Hz. 
		#Bin 50 is 2155Hz.
		sizeOfFFT = 1024; #size of fft ( k = N , in this case)
		non_Aliasing_Points = sizeOfFFT/2;
		sizeOfBin = 44100.0/sizeOfFFT;
		fundamental1 = 100*sizeOfBin;
		fundamental2 = 100.5*sizeOfBin;

		#PART A - fundamental at freq bin
		sine1 = mir.Sinusoid(amp = 1,freq = fundamental1,phase = 0, duration = 0.01);
		sine2 = mir.Sinusoid(amp = 0.5,freq = 2*fundamental1, phase = np.pi/4, duration = 0.01);
		sine3 = mir.Sinusoid(amp = 0.25,freq = 3*fundamental1, phase = np.pi/2, duration = 0.01);
		signal1 = mir.Mixture(sine1,sine2,sine3);
		inputSamples1 = signal1.data;	
		methodsForFFT.dftByHector(non_Aliasing_Points,signal1,inputSamples1);
		#PART A - fundamental at freq bin
		
		#PART B - fundamental between freq bin
		#sine1 = mir.Sinusoid(amp = 1,freq = fundamental2,phase = 0, duration = 0.01);
		#sine2 = mir.Sinusoid(amp = 0.5,freq = fundamental2*2, phase = np.pi/4, duration = 0.01);
		#sine3 = mir.Sinusoid(amp = 0.25,freq = fundamental2*3, phase = np.pi/2, duration = 0.01);
		#signal2 = mir.Mixture(sine1,sine2,sine3);
		#inputSamples2 = signal2.data;		
		#methodsForFFT.dftByHector(non_Aliasing_Points,signal2,inputSamples2);
		#PART B - fundamental between freq bin
		
		#----------------'plotting with library function for DFT'----------------------#
		#------------------------------------------------------------------------------#
		#------------------------------------------------------------------------------#

		freq = np.fft.fft(inputSamples,sizeOfFFT)/len(inputSamples);
		real_part = np.real(freq);
		imag_part = np.imag(freq);
		
		magn_spectrum = np.absolute(freq);

		phase_spectrum = np.zeros(non_Aliasing_Points,);
		for i in range (0,non_Aliasing_Points):
			phase_spectrum[i] = np.arctan2(imag_part[i],real_part[i]);
		
		lin_space = np.linspace(0,non_Aliasing_Points,non_Aliasing_Points);

		plt.title('Magnitude Response - LIBRARY');
		plt.ylabel('Magnitude in dB');
		plt.xlabel('Frequency bin (x ~43 Hz)');
		plt.stem(lin_space, magn_spectrum[:non_Aliasing_Points],'r');
		plt.show();
		
		plt.title('Phase Response - LIBRARY');
		plt.ylabel('Phase in Radians');
		plt.xlabel('Frequency bin (x ~43 Hz)');
		plt.stem(lin_space, phase_spectrum[:non_Aliasing_Points],'r');
		plt.show();
		
		return 0;
		

	if __name__ == "__main__": main()