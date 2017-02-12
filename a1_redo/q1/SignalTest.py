import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class SignalTest():

	def main():
		
		sign = mir.Signal();
		relative_path = 'wav_files/flutehighMono.wav';
		sign.wav_read(relative_path);
		sign.wav_write('wav_files/outSignal.wav');
		
		
		arr1 = np.linspace(0,len(sign.data),len(sign.data));#len(sign.data),len(sign.data)); #x's
		arr3 = np.linspace(0,2048,2048);#len(sign.data),len(sign.data)); #x's
		print arr1.shape;
		
		arr2 = sign.data[:len(sign.data)]; #y's
		arr4 = sign.data[len(sign.data)/2:(len(sign.data)/2)+2048];
		print arr2.shape;
		
		plt.title('Flute Signal Graphed');
		plt.ylabel('Amplitude');
		plt.xlabel('Time');
		plt.plot(arr3,arr4);
		plt.show();
		
		return 0;

	if __name__ == "__main__": main()