import sys, aubio

samplerate = 0; #if zero is passed in, then 
				#original Fs is used.
hop_size = 1024;
s = aubio.source('audioSignal/outMelody.wav',samplerate,hop_size);

total_frames = 0;

while True: # reading loop
    samples, read = s() #this is weird, it has two returns...
    total_frames += read
    if read < hop_size: break # end of file reached

fmt_string = "read {:d} frames at {:d}Hz from {:s}"
print (fmt_string.format(total_frames, s.samplerate, 'audioSignal/outMelody'))