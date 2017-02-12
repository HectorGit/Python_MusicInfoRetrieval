import mir
import methodsForFFT
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class AdditiveSynthesis():

	def main():
		
		#improve - read this list from a file. or receive as system argument. (from console.)
		list_of_frequencies_and_amplitudes = [[50,1],[100,0.75],[200,0.5],[400,0.25],[800,0.5],[1600,0.75]];
		
		instrumentData = np.zeros(44100,);

		for sublist in list_of_frequencies_and_amplitudes:
			sinTemp = mir.Sinusoid(freq = sublist[0], amp = sublist[1]);
			instrumentData = np.add(instrumentData,sinTemp.data);
			
		outputSignal =	mir.Signal(data = instrumentData);
				
		outputSignal.wav_write('outInstrument.wav');
				
		arr1 = np.linspace(0,len(outputSignal.data)/440,len(outputSignal.data)/440);#len(sign.data),len(sign.data)); #x's
		print arr1.shape;
		
		arr2 = outputSignal.data[:len(outputSignal.data)/440]; #y's
		print arr2.shape;
		
		plt.title('Instrument Waveform Graphed');
		plt.ylabel('Amplitude');
		plt.xlabel('Time');
		plt.stem(arr1,arr2);
		plt.show();
		
		#improve - take the DFT of said signal of instrument.
		
		factor = 100; #this reduces the size of the DFT to a fraction of the length of 
					  #the input
		inputSamples = outputSignal.data;		
	
		sizeOfFFT = len(inputSamples)/factor; #size of fft ( k = N , in this case)
		numberOfBins = sizeOfFFT/2;

		#methodsForFFT.dftByHector(factor,numberOfBins,outputSignal,inputSamples);
		
		freq = np.fft.fft(inputSamples,sizeOfFFT)/numberOfBins;#/len(inputSamples);
		real_part = np.real(freq);
		imag_part = np.imag(freq);
		
		magn_spectrum = np.absolute(freq);	
		lin_space = np.linspace(0,(44100)/2,numberOfBins);

		plt.title('Library FFT');
		plt.stem(lin_space, magn_spectrum[:numberOfBins],'r');		
		plt.show();
		
		
		
		return 0;

	if __name__ == "__main__": main()