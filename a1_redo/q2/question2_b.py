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
		relative_path = '../wav_files/flutehighMono.wav'
		sign.wav_read(relative_path);
		
		sizeOfFFT = 2048; #2048 points, but need to ignore half of the results, by symmetry?
		sizeOfBin = 44100/float(sizeOfFFT);
		print 'size of bin';
		print sizeOfBin;
			
		sizeSignal = len(sign.data);
		#create Hanning window
		hanning_window = np.hanning(2048.0); #just a window that is this many samples long.
		                                   #note input is much larger !!! must multiply input by 
										   #window every 2048 samples.
										   #Doesn't satisfy the Overlap and Add condition-> Artifacts.
										   
	
		question2functions.windowSignal(sign,hanning_window);
		question2functions.plotMagnitudeSpectrum(sign,sizeOfFFT);
		
		plt.show();
		
		return 0;
		

	if __name__ == "__main__": main()