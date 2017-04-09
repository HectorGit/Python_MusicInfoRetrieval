import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class BasisFunctions():

	def main():
		Fs = 44100;
		TotalNumBin = 1024;
		FundamentalBin = 15;
		SizeOfBin = Fs/TotalNumBin;
		FundamentalFreq = FundamentalBin*SizeOfBin;
		BasisFreq = 128*SizeOfBin;

		testsine1 = mir.Sinusoid(freq = FundamentalFreq);
		sine1 = mir.Sinusoid(freq = BasisFreq);
		cosine1 = mir.Sinusoid(freq = BasisFreq, phase = np.pi/2);

		testsine2 = mir.Sinusoid(freq = 2*FundamentalFreq);
		sine2 = mir.Sinusoid(freq = 2*BasisFreq);
		cosine2 = mir.Sinusoid(freq = 2*BasisFreq, phase = np.pi/2);

		testsine3 = mir.Sinusoid(freq = 3*FundamentalFreq);
		sine3 = mir.Sinusoid(freq = 3*BasisFreq);
		cosine3 = mir.Sinusoid(freq = 3*BasisFreq, phase = np.pi/2);		
		
		mixture = mir.Mixture(testsine1,testsine2,testsine3);
		
		#plt.plot([1,2,3],[4,5,6]);
		plt.plot(sine1.data[:10]);
		plt.plot(cosine1.data[:10]);
		plt.show();
		
		plt.plot(sine2.data[:10]);
		plt.plot(cosine2.data[:10]);
		plt.show();
	
		plt.plot(sine3.data[:10]);
		plt.plot(cosine3.data[:10]);
		plt.show();
	
		#multiply everything.
	
		arr4 = np.multiply(mixture.data, sine1.data);
		arr5 = np.multiply(arr4, cosine1.data);
		arr6 = np.multiply(arr5, sine2.data);
		arr7 = np.multiply(arr6, cosine2.data);
		arr8 = np.multiply(arr7,sine3.data);
		arr9 = np.multiply(arr8, cosine3.data);

		plt.title('bin 128 test sinusoid mult. w bin 128 basis');
		plt.ylabel('Amplitude');
		plt.xlabel('Time');
		plt.plot(arr9[:40]);
		plt.show();
		
		return 0;

	if __name__ == "__main__": main()