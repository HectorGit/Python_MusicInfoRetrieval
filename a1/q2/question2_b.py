import mir
import question2functions
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

class question2_b():

	def main():

		sign = mir.Signal();
		relative_path = 'wav_files/flutehighMono.wav'
		sign.wav_read(relative_path);
		plt.plot(sign.data);
		plt.show();
		sizeOfFFT = 2048;
		sizeOfBin = 44100/float(sizeOfFFT);
		hanning_window = np.hanning(2048.0); 
		question2functions.plotMagnitudeSpectrumReduced(sign,sizeOfFFT);
		plt.show();
		
		question2functions.windowSignal(sign,hanning_window);
		question2functions.plotMagnitudeSpectrumReduced(sign,sizeOfFFT);
		plt.show();

		return 0;
		

	if __name__ == "__main__": main()