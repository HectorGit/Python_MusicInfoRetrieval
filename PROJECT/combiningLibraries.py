import argparse
import sys
import librosa #takes a long time to import
import librosaFunctions
import matplotlib.pyplot as plt
import numpy as np
from librosa.display import specshow

class combiningLibraries():
	
	def main():
		#onset strength detection with librosa and plotting it
		
		#beat detection with librosa -> returns timestamps.
		
		parameters = librosaFunctions.process_arguments(sys.argv[1:]);
		
		#onset_env = librosaFunctions.obtain_onsets_env(parameters['input_file']);
		#plt.plot(onset_env);
		#plt.show();
		
		beats = librosaFunctions.beat_track(parameters['input_file']);
		
		#plotting the onsets overlayed with the beats
		#https://librosa.github.io/librosa/generated/librosa.beat.beat_track.html
		
		librosaFunctions.plot_beats_and_onsets(parameters['input_file'],beats);
		
		#chroma extraction with librosa - what is the time interval used?
		
		chromagram = librosaFunctions.chromagram(parameters['input_file']);
		librosaFunctions.plot_chromagram(chromagram);
		
		#chord detection with librosa ->  THERE ISN'T WAS REMOVED IN 0.3 - > Used hidden markov model
		#librosa.chord
		#http://pydoc.net/Python/librosa/0.3.1/librosa.chord/
		#https://github.com/orchidas/Chord-Recognition orchidas/Chord-Recognition -> Very complicated, HMM, and Viterbi?
		
		#the chords are calculated every 0.37 seconds, because the frame size is 16384 with sampling rate 44100 seconds.
		chords = [];
		startTimes = [];
		endTimes = [];
		numFrames = 0;
				
		chords, startTimes, endTimes, numFrames = librosaFunctions.get_chords(chords, startTimes, endTimes, numFrames, parameters['input_file']);
		
		#print chords;     #letter name of chords predicted.
		#print startTimes; #time in seconds that chord starts 
		#print endTimes;   #time in seconds chord ends
		#print numFrames;  #total number of chords predicted 
		
		for i in range (numFrames):
			print('frame : %6d | chord : %6s | startTime : %8.5f | endTime : %7.5f ' % (i,chords[i],startTimes[i],endTimes[i]))
		
		#NEXT STEPS: compare the beat times and onset times with the chord times, (IN SECONDS) and so we will know
					 #when to insert a new note for the Accompaniment we are creating.
		
		
	if __name__ == "__main__": main()







