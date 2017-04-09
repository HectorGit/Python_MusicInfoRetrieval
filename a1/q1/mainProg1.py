import mir
import methodsForFFT
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class mainProg1():
	
	def main():
		#-----IMPLEMENTED----#
		
		Fs = 44100;
		sizeOfFFT = 1024; #size of fft ( k = N , in this case)
		sizeOfBin = Fs/sizeOfFFT;
		fundamental1 = 128*sizeOfBin;
		fundamental2 = 130.5*sizeOfBin;

		#PART A - fundamental at freq bin
		sine1 = mir.Sinusoid(amp = 1,freq = fundamental1,phase = 0, duration = 0.001);
		sine2 = mir.Sinusoid(amp = 0.5,freq = 2*fundamental1, phase = np.pi/4, duration = 0.001);
		sine3 = mir.Sinusoid(amp = 0.25,freq = 3*fundamental1, phase = np.pi/8, duration = 0.001);
		signal1 = mir.Mixture(sine1,sine2,sine3);
		methodsForFFT.dftByHector(sizeOfFFT,signal1,sizeOfBin);
		#PART A - fundamental at freq bin
		
		#PART B - fundamental between freq bin
		sine4 = mir.Sinusoid(amp = 1,freq = fundamental2,phase = 0, duration = 0.001);
		sine5 = mir.Sinusoid(amp = 0.5,freq = fundamental2*2, phase = np.pi/4, duration = 0.001);
		sine6 = mir.Sinusoid(amp = 0.25,freq = fundamental2*3, phase = np.pi/8, duration = 0.001);
		signal2 = mir.Mixture(sine4,sine5,sine6);
		methodsForFFT.dftByHector(sizeOfFFT,signal2,sizeOfBin);
		#PART B - fundamental between freq bin
		
		#-----LIBRARY----#
		methodsForFFT.plotWithLibraryFFT(sizeOfFFT, signal1);
		methodsForFFT.plotWithLibraryFFT(sizeOfFFT, signal2);
		return 0;
		

	if __name__ == "__main__": main()