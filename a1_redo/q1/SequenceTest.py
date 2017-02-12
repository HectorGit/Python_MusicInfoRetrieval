import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class SequenceTest():

	def main():
		
		sine1 = mir.Sinusoid(amp = 0.5, freq = 440.0);
		sine2 = mir.Sinusoid(amp = 0.75, freq = 770.0);
		sine3 = mir.Sinusoid(freq = 690.0);
		
		print 'Created sinewaves';
		
		seq = mir.Sequence(sine1,sine2,sine3);
		seq.wav_write('wav_files/outSequence.wav');
		
		print 'Writing sequence to File';
		
		arr1 = np.linspace(0,len(seq.data),len(seq.data));#len(sign.data),len(sign.data)); #x's
		print arr1.shape;
		
		arr2 = np.multiply(0.5,seq.data[:len(seq.data)]); #y's
		print arr2.shape;
		
		plt.title('Sequence Graphed');
		plt.ylabel('this_is_ylabel');
		plt.xlabel('this_is_xlabel');
		plt.plot(arr1,arr2);
		plt.show();
		
		print 'Plotting';
		
		return 0;

	if __name__ == "__main__": main()