from __future__ import division 
from pymir import AudioFile
from pymir import Pitch
from pymir import Onsets
import argparse
import sys
import librosa
import matplotlib.pyplot as plt
import numpy as np
from librosa.display import TimeFormatter
from librosa.display import specshow

def print_a_thing():
	print 'Probabilities For Rap';

def obtain_onsets_env(input_file):	
	print('Loading ', input_file)
	y, sr = librosa.load(input_file);
	hop_length = 512;
	onset_env = librosa.onset.onset_strength(y, sr=sr,aggregate=np.median);
	return onset_env;
	
def beat_track(input_file):
	print('Loading ', input_file)
	y, sr = librosa.load(input_file);

	hop_length = 512;

	print('Tracking beats');
	tempo, beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop_length);

	print('Estimated tempo: {:0.2f} beats per minute'.format(tempo));

		
	#printing as timestamps
	beat_times = librosa.frames_to_time(beats, sr=sr, hop_length=hop_length);
	
	print beat_times;
	
	return beats;
	
def plot_beats_and_onsets(input_file,beats):
	print('Loading ', input_file)
	y, sr = librosa.load(input_file);
	hop_length = 512;
	onset_env = librosa.onset.onset_strength(y, sr=sr,aggregate=np.median);
	plt.figure(figsize=(8, 4));
	times = librosa.frames_to_time(np.arange(len(onset_env)),sr=sr, hop_length=hop_length);
	plt.plot(times, librosa.util.normalize(onset_env),label='Onset strength');
	plt.vlines(times[beats], 0, 1, alpha=0.5, color='r',linestyle='--', label='Beats');
	plt.legend(frameon=True, framealpha=0.75);
	plt.xlim(0, times[-1]);
	#plt.xlim(0, 15);
	plt.show();
	plt.gca().xaxis.set_major_formatter(librosa.display.TimeFormatter());
	plt.tight_layout();
	
def chromagram(input_file):
	print('Loading ', input_file);
	y, sr = librosa.load(input_file);
	hop_length = 512;
	n_fft = 2048;
	chroma = librosa.feature.chroma_stft(y=y,sr=sr,hop_length=hop_length)
	return chroma;
	
def plot_chromagram(chroma):
	plt.figure(figsize=(10, 4));
	librosa.display.specshow(chroma, y_axis='chroma', x_axis='time');
	plt.colorbar();
	plt.title('Chromagram');
	plt.tight_layout();
	plt.show();
		
def process_arguments(args):

    parser = argparse.ArgumentParser(description='Beat tracking example')

    parser.add_argument('input_file',
                        action='store',
                        help='path to the input file (wav, mp3, etc)')

    return vars(parser.parse_args(args))

	
#accumulating the chords found in an array and returning it.
#also returning an array of timestamps, by converting the number of the frame 
#to seconds using seconds = (i * frameSize / 44100)

def get_chords(chords, startTimes, endTimes, numFrames, input_file):
		
	audiofile = AudioFile.open(input_file);
	o = Onsets.onsetsByFlux(audiofile)

	frames = audiofile.framesFromOnsets(o)
	
	frameSize = 16384
	frames = audiofile.frames(frameSize)

	frameIndex = 0;
	startIndex = 0;

	for frame in frames:
	
		spectrum = frame.spectrum();
		chroma = spectrum.chroma();
		
		chord, score = Pitch.getChord(chroma);
		
		chords = np.append(chords, chord);

		endIndex = startIndex + len(frame);
		
		startTime = startIndex / frame.sampleRate; 
		
		startTimes = np.append(startTimes, startTime);
		
		endTime = endIndex / frame.sampleRate;
		
		endTimes = np.append(endTimes, endTime);
		
		frameIndex = frameIndex + 1
		startIndex = startIndex + len(frame)
		
	return chords, startTimes, endTimes, frameIndex;
		
