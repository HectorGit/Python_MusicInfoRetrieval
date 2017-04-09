
from __future__ import division 

import sys
sys.path.append('..')

from pymir import AudioFile
from pymir import Pitch
from pymir import Onsets

import matplotlib.pyplot as plt

# Load the audio

print "Enter a file name:",
filename = raw_input()

print "Loading Audio"
audiofile = AudioFile.open(filename);

plt.plot(audiofile)
plt.show()

print "Finding onsets using Spectral Flux (spectral domain)"
o = Onsets.onsetsByFlux(audiofile)
print o

print "Extracting Frames"
frames = audiofile.framesFromOnsets(o) #cant find this method anywhere.

#it seems to be extracting the audio frame from the audio where onsets are.
#each frame must have a specific time length.

#for i in range(0, len(frames)):
#	print "Frame " + str(i)
#	plt.plot(frames[i])
#	plt.show()

#frameSize = 16384 # this is how many  samples each frame has??? 
				   # how many seconds is that if sample rate is 44100.
				   # why so arbitrary number
#frames = audioFile.frames(frameSize)

print "Start | End  | Chord | (% match)"
print "-------------------------------"

frameIndex = 0
startIndex = 0

for frame in frames:
	spectrum = frame.spectrum() # spectrum of a 16384 sample frame
	chroma = spectrum.chroma()  # chroma folded over to 12 pitch classes.
	#print chroma #printing the values for each of the 12 pitch classes.
	
	chord, score = Pitch.getChord(chroma); #cosine similarity to vector for this frame.

	endIndex = startIndex + len(frame); #this is actual indexes in a frame.

	startTime = startIndex / frame.sampleRate #this is converting to seconds.
	endTime = endIndex / frame.sampleRate     #conv. to s. e.g. 16384/44100 is 0.37 seconds.

	print "%.2f  | %.2f | %-4s | (%.2f)" % (startTime, endTime, chord, score)
    
	frameIndex = frameIndex + 1
	startIndex = startIndex + len(frame)