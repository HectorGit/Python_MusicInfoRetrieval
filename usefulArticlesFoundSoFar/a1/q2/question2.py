import mir
import question2functions
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt

class question2():

	def main():

		#sign = mir.Signal();
		#relative_path = 'wav_files/clarinetD3sharp_truncated.wav'
		#sign.wav_read(relative_path);
		
		#since Fs = 44100, 
		#we have size of a bin = 44100/ 2048 = 21.53 Hz
		sizeOfFFT = 2048; #2048 points, but need to ignore half of the results, by symmetry?
		sizeOfBin = 44100/float(sizeOfFFT);
		print 'size of bin';
		print sizeOfBin;
		
		#Create sinusoids with correct frequencies.
		sine_a = mir.Sinusoid(freq = 525.0* sizeOfBin);#sign); #this calls __init__ automatically
		sine_b = mir.Sinusoid(freq = 600.5* sizeOfBin);
		sine_c = mir.Sinusoid(freq = 525.5* sizeOfBin);
		
		sizeSinA = len(sine_a.data);
		sizeSinB = len(sine_b.data);
		sizeSinC = len(sine_c.data); #needs to be windowed.
		
		#create Hanning window
		hanning_window = np.hanning(2048.0); #just a window that is this many samples long.
		                                   #note input is much larger !!! must multiply input by 
										   #window every 2048 samples.
										   #Doesn't satisfy the Overlap and Add condition-> Artifacts.
										   
	
		#question2functions.windowSignal(sine_a,hanning_window);
		question2functions.plotMagnitudeSpectrum(sine_a,sizeOfFFT);
		
		#question2functions.windowSignal(sine_b,hanning_window);
		#question2functions.plotMagnitudeSpectrum(sine_b,sizeOfFFT);
				
		#question2functions.windowSignal(sine_c,hanning_window);
		#question2functions.plotMagnitudeSpectrum(sine_c,sizeOfFFT);
		
		plt.show();
		
		return 0;
		

	if __name__ == "__main__": main()