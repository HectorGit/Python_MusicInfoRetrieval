import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

def dftByHector(sizeOfFFT,sign,sizeOfBin):	

	re_in = sign.data;
	n = len(re_in);	
	re_out = np.zeros(sizeOfFFT,);
	im_out = np.zeros(sizeOfFFT,);	
	
	for k in range(0,sizeOfFFT):
		sumReal = 0;
		sumImag = 0;
		for t in range(0,n):
			angle = float(2.0*np.pi*(t*k)/sizeOfFFT);
			sumReal += re_in[t] * np.cos(angle);
			sumImag += re_in[t] * np.sin(angle);
		re_out[k] = sumReal;
		im_out[k] = sumImag;
	
	non_Aliasing_Points = sizeOfFFT/2;	
	plotDFT(non_Aliasing_Points, sign,re_out,im_out);
	return 0;
		
def plotMagnitudeSpectrum(non_Aliasing_Points, sign,re_out,im_out):	
	magnitude_spectrum = np.zeros(non_Aliasing_Points,);														
	print len(magnitude_spectrum);
	for i in range(0,non_Aliasing_Points):
		magnitude_spectrum[i] = np.sqrt(im_out[i]**2+re_out[i]**2);		
	arr2 = magnitude_spectrum;
	arr1 = np.linspace(0,non_Aliasing_Points,non_Aliasing_Points); 
	plt.ylabel('Amplitude');
	plt.xlabel('Frequency Bin')
	plt.title('MagnitudeSpectrum');
	plt.plot(arr1,arr2);
	return 0;

def plotPhaseSpectrum(non_Aliasing_Points, sign,re_out,im_out):
	phase_spectrum = np.zeros(non_Aliasing_Points,);	
	for i in range (0,non_Aliasing_Points):
		phase_spectrum[i] = np.arctan2(im_out[i],re_out[i]);				
	arr4 = phase_spectrum;
	arr3 = np.linspace(0,non_Aliasing_Points,non_Aliasing_Points); 
	plt.title('PhaseSpectrum');
	plt.ylabel('Phase');
	plt.xlabel('Frequency Bin');
	plt.plot(arr3,arr4);
	return 0;
	
def plotDFT(non_Aliasing_Points,sign,real_part, imaginary_part):
	plotMagnitudeSpectrum(non_Aliasing_Points,sign,real_part, imaginary_part);
	plt.show();
	plotPhaseSpectrum(non_Aliasing_Points,sign,real_part,imaginary_part);
	plt.show();
	return 0;	

def plotWithLibraryFFT(sizeOfFFT, sign):
	non_Aliasing_Points = sizeOfFFT/2;
	freq = np.fft.fft(sign.data,sizeOfFFT)/len(sign.data);
	real_part = np.real(freq);
	imag_part = np.imag(freq);
	magn_spectrum = np.absolute(freq);
	phase_spectrum = np.zeros(non_Aliasing_Points,);
	for i in range (0,non_Aliasing_Points):
		phase_spectrum[i] = np.arctan2(imag_part[i],real_part[i]);
	lin_space = np.linspace(0,non_Aliasing_Points,non_Aliasing_Points);
	plt.title('Magnitude Response - LIBRARY');
	plt.ylabel('Magnitude');
	plt.xlabel('Frequency bin');
	plt.plot(lin_space, magn_spectrum[:non_Aliasing_Points],'r');
	plt.show();
	plt.title('Phase Response - LIBRARY');
	plt.ylabel('Phase');
	plt.xlabel('Frequency bin');
	plt.plot(lin_space, phase_spectrum[:non_Aliasing_Points],'r');
	plt.show();
	