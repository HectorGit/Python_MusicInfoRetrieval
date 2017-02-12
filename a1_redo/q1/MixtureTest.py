import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class MixtureTest():

	def main():
		
		sine1 = mir.Sinusoid(amp = 1,freq = 2000.0,phase = 0);
		sine2 = mir.Sinusoid(amp = 0.50,freq = 4000.0, phase = np.pi/2);
		sine3 = mir.Sinusoid(amp = 0.25,freq = 8000.0, phase = np.pi/4);

		print 'Created sinewaves';
		
		mixture = mir.Mixture(sine1,sine2,sine3);
		mixture.wav_write('wav_files/outMixture.wav');
		
		print 'Writing mixture to File';
		
		arr1 = np.linspace(0,len(mixture.data)/440,len(mixture.data)/440);#len(sign.data),len(sign.data)); #x's
		print arr1.shape;
		
		arr2 = mixture.data[:len(mixture.data)/440]; #y's
		print arr2.shape;
		
		plt.title('Mixture Graphed');
		plt.ylabel('this_is_ylabel');
		plt.xlabel('this_is_xlabel');
		plt.stem(arr1,arr2);
		plt.show();
		
		print 'Plotting';
		
		return 0;

	if __name__ == "__main__": main()