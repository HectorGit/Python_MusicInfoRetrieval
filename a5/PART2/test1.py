#import mir_eval
#import librosa #used to get the audio file read
import vamp

#read audio files in with librosa (?)

#print('Loading %s '% ('gloria.wav'));
#audio1, sr1 = librosa.load('gloria.wav',sr = 44100);

#print('sampling rate : %f' % (sr1));

#print('Loading %s '% ('turca.wav'));
#audio2, sr2 = librosa.load('turca.wav',sr = 44100);

#print('sampling rate : %f' % (sr2));


#use vampy to run the segmentation plugins

vamp.list_plugins();
#vamp.load_plugin();

#this returns a dict of all the things within that 
segmentsSegmenter = vamp.collect(audio1, sr1,"segmentino:segmentino");

#------------get segments from segmenter

#for gloria

#for turca

#-------------get segments from segmentino

#for gloria

#for turca

# task - use mir_eval to get F measure of
# the segmenter's and segmentino's output