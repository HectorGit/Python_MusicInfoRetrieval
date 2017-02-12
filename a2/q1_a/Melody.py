import mir
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class Melody():

	def main():
		
		#theme for mario bros.
		list_of_MIDI_values = [72, 12,12, 20, 24, 67, 12,12, 20, 24, 64, 12, 20, 24, 69, 12, 20, 12, 71, 12, 20, 70, 12, 69, 20, 12, 67, 16, 76, 16, 79, 16, 81, 12, 20, 12, 77, 12, 79, 12, 20, 12, 76, 12, 20, 12, 72, 12, 74, 12, 71, 12, 20, 24];
		list_of_MIDI_values2 = [48, 12, 20, 12, 79, 12, 78, 12, 77, 12, 75, 12, 60, 12, 76, 12, 53, 12, 68, 12, 69, 12, 72, 12, 60, 12, 69, 12, 72, 12, 74, 12, 48, 12, 20, 12, 79, 12, 78, 12, 77, 12, 75, 12, 55, 12, 76, 12, 20, 12, 84, 12, 20, 12, 84, 12, 84, 12];
		list_of_MIDI_values = np.insert(list_of_MIDI_values,len(list_of_MIDI_values),list_of_MIDI_values2);
		
		f_and_amp = [[1300,0.25],[3600,0.12],[3700,0.12],[3800,0.12],[4500,0.12],[5300,0.12],[8400,0.6]];
		ratios = np.zeros(len(f_and_amp),);
		
		for k in range(0,len(f_and_amp)):
			ratios[k] = f_and_amp[k][0]/f_and_amp[0][0];
		
		#trying to get this played into a file - must use sequence in mir.py file.
		seed = mir.Sinusoid(freq = 0, duration = 0.09);
		sequence = mir.Sequence(seed);
		
		for i in range(0,len(list_of_MIDI_values)):
			#calculate freq with the formula
			#A is 440 Hz
			difference = (list_of_MIDI_values[i]-69);
			exponent = difference/12.0;
			f = 440.0*(2.0**(exponent)); #we can see that 12th root of 2 is used.
			
			seed = mir.Sinusoid(freq = 0, duration = 0.09);
			mixture = mir.Mixture(seed);
			
			for k in range(0,len(ratios)):
				if ((ratios[k]*f) >= 500.0 and (ratios[k]*f) <= 44100.0/2):
					sinTemp = mir.Sinusoid(freq = ratios[k]*f, duration = 0.09, amp = float(f_and_amp[k][1]));
					#print 0.01*float(f_and_amp[k][1]);
				else:
 					sinTemp = mir.Sinusoid(freq = 0, duration = 0.09, amp = 0);

				mixture = mir.Mixture(mixture,sinTemp);
			
			sequence = mir.Sequence(sequence,mixture);
			#reset the mixture to zeros?
			mixture = mir.Mixture(seed);
				
		outputSignal = sequence;
		outputSignal.wav_write('../q1audioSignals/outMelody.wav');
										
		return 0;

	if __name__ == "__main__": main()