import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class SinusoidTest():

	def main():
		
		#sign = mir.Signal();
		#relative_path = 'wav_files/audio1.wav'
		#sign.wav_read(relative_path);
		#sign.wav_write('out.wav');
		
		sine = mir.Sinusoid(freq = 1764.0);#sign); #this calls __init__ automatically
		#sine.freq = 800.0;
		#sine.make();             #is this called automatically?
		
		sine.wav_write('wav_files/outSinusoid.wav');
		
		arr1 = np.linspace(0,len(sine.data)/440,len(sine.data)/440)#sine.duration*sine.Fs,sine.duration*sine.Fs); #x's
		#print arr1.shape;
		
		arr2 = sine.data[:len(sine.data)/440]; #y's
		#print arr2.shape;
		
		plt.title('Sine - 1764 Hz Sine Tone');
		plt.ylabel('Amplitude');
		plt.xlabel('Time');
		plt.plot(arr1,arr2);
		
		
		#Create a cosine.
		#cosine = mir.Sinusoid(freq = 800.0, phase = np.pi/2); #phase = 2/pi * (90) ;
		
		#plt.title('COSINE Test - 880 Sine Tone');
		#plt.ylabel('this_is_ylabel');
		#plt.xlabel('this_is_xlabel');
		
		#arr3 = np.linspace(0,len(cosine.data)/440,len(cosine.data)/440)#sine.duration*sine.Fs,sine.duration*sine.Fs); #x's
		
		#arr4 = cosine.data[:len(cosine.data)/440]; #y's
		
		#plt.plot(arr3,arr4);
		plt.show();
		
		
		return 0;

	if __name__ == "__main__": main()