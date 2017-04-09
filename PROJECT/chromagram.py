from __future__ import print_function

import sys
import librosa
from librosa.display import specshow
import argparse
import matplotlib.pyplot as plt


def chroma_detect(input_file):
    '''chroma detection function

    :parameters:
      - input_file : str
          Path to input audio file (wav, mp3, m4a, flac, etc.)
    '''

    print('Loading ', input_file);
    y, sr = librosa.load(input_file, sr=22050);

    hop_length = 512;

    n_fft = 2048;

    print('Detecting chroma...');
    chroma = librosa.feature.chroma_stft(y=y,sr=sr,hop_length=hop_length);
										
def process_arguments(args):
    '''Argparse function to get the program parameters'''

    parser = argparse.ArgumentParser(description='librosa onset detection example');

    parser.add_argument('input_file',action='store',help='path to the input file (wav, mp3, etc)');

    return vars(parser.parse_args(args))
										
def plot_chromagram(chroma):
	plt.figure(figsize=(10, 4))
	librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
	plt.colorbar()
	plt.title('Chromagram')
	plt.tight_layout()
											
if __name__ == '__main__':
	parameters = process_arguments(sys.argv[1:])
	chroma = chroma_detect(parameters['input_file'])
	plot_chromagram(chroma);
