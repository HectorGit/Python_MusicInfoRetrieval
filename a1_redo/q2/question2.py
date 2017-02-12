import mir
import question2functions
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

class question2():

	def main():

		sign = mir.Signal();
		relative_path = 'wav_files/flutehighMono.wav'
		sign.wav_read(relative_path);
	
		sizeOfFFT = 2048; 
		sizeOfBin = 44100/float(sizeOfFFT);
		
		sine_a = mir.Sinusoid(freq = 525.0* sizeOfBin);
		sine_b = mir.Sinusoid(freq = 600.5* sizeOfBin);
		sine_c = mir.Sinusoid(freq = 525.5* sizeOfBin);
		
		sizeSinA = len(sine_a.data);
		sizeSinB = len(sine_b.data);
		sizeSinC = len(sine_c.data); 
		
		hanning_window = np.hanning(2048.0); 						   
	
		question2functions.plotWindowedAndNonWindowed(sign,sizeOfFFT,hanning_window);#525.0
		
		#question2functions.plotWindowedAndNonWindowed(sine_b,sizeOfFFT,hanning_window);#600.5

		#question2functions.plotWindowedAndNonWindowed(sine_c,sizeOfFFT,hanning_window);#525.5

		return 0;
		

	if __name__ == "__main__": main()