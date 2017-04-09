### tempo extraction.
### demo tempo - not sure what it is doing.
### seems to be extracting the beats at the seconds that they are.
### returning as an array of beats.

import sys
from aubio import tempo, source

win_s = 2048
hop_s = 1024 

filename = 'audioSignal/hectorHigh.wav';

samplerate = 0

s = source(filename, samplerate, hop_s)
samplerate = s.samplerate
o = tempo("default", win_s, hop_s, samplerate)

# tempo detection delay, in samples
# default to 4 blocks delay to catch up with
delay = 4. * hop_s

# list of beats, in samples initialized as empty.
beats = []

# total number of frames read
total_frames = 0
while True:
    samples, read = s()
    is_beat = o(samples)
    if is_beat:
        this_beat = int(total_frames - delay + is_beat[0] * hop_s); #wtf
        print("%f" % (this_beat / float(samplerate)))
        beats.append(this_beat)
    total_frames += read
    if read < hop_s: break