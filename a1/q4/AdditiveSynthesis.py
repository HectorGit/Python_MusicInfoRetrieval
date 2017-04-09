import mir
import methodsForFFT
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class AdditiveSynthesis():

	def main():
		list_of_frequencies_and_amplitudes = [[50,1],[100,0.75],[200,0.5],[400,0.25],[800,0.5],[1600,0.75]];
		instrumentData = np.zeros(44100,);
		for sublist in list_of_frequencies_and_amplitudes:
			sinTemp = mir.Sinusoid(freq = sublist[0], amp = sublist[1]);
			instrumentData = np.add(instrumentData,sinTemp.data);
		outputSignal =	mir.Signal(data = instrumentData);
		outputSignal.wav_write('outInstrument.wav');
		inputSamples = outputSignal.data;		
		sizeOfFFT = 4096;
		numberOfBins = sizeOfFFT;
		freq = np.fft.fft(inputSamples,sizeOfFFT);
		real_part = np.real(freq);
		imag_part = np.imag(freq);
		magn_spectrum = np.absolute(freq)/len(inputSamples);	
		lin_space = np.linspace(0,sizeOfFFT,sizeOfFFT);
		plt.title('Library FFT');
		print len(lin_space);
		print len(magn_spectrum);
		plt.plot(lin_space[:sizeOfFFT/10], magn_spectrum[:sizeOfFFT/10],'r');		
		plt.show();
		
		return 0;

	if __name__ == "__main__": main()