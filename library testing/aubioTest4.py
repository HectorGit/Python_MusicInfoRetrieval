# pitch extraction example

import sys
from aubio import source, pitch

filename = 'audioSignal/outMelody.wav';

downsample = 1 #hmm???
samplerate = 44100;

win_s = 2048 
hop_s = 1024

s = source(filename, samplerate, hop_s)
samplerate = s.samplerate

tolerance = 0.8; #not sure why this is needed

pitch_o = pitch("default", win_s, hop_s, samplerate)
pitch_o.set_unit("midi"); ### WTF
pitch_o.set_tolerance(tolerance);

pitches = []
confidences = []

# total number of frames read
total_frames = 0
while True:
    samples, read = s()
    pitch = pitch_o(samples)[0]
    confidence = pitch_o.get_confidence()
    print("%f %f %f" % (total_frames / float(samplerate), pitch, confidence))
    pitches += [pitch]
    confidences += [confidence]
    total_frames += read
    if read < hop_s: break

if 0: sys.exit(0)

#this part doesnt work -> DEMO WAVEFORM PLOT DOESN'T INSTALL W PIP.

#print pitches
#import os.path
#from numpy import array, ma
#import matplotlib.pyplot as plt
#from demo_waveform_plot import get_waveform_plot, set_xlabels_sample2time

#skip = 1

#pitches = array(pitches[skip:])
#confidences = array(confidences[skip:])
#times = [t * hop_s for t in range(len(pitches))]

#fig = plt.figure()

#ax1 = fig.add_subplot(311)
#ax1 = get_waveform_plot(filename, samplerate = samplerate, block_size = hop_s, ax = ax1)
#plt.setp(ax1.get_xticklabels(), visible = False)
#ax1.set_xlabel('')

#def array_from_text_file(filename, dtype = 'float'):
#    filename = os.path.join(os.path.dirname(__file__), filename)
#    return array([line.split() for line in open(filename).readlines()],
#        dtype = dtype)

#ax2 = fig.add_subplot(312, sharex = ax1)
#ground_truth = os.path.splitext(filename)[0] + '.f0.Corrected'
#if os.path.isfile(ground_truth):
#    ground_truth = array_from_text_file(ground_truth)
#    true_freqs = ground_truth[:,2]
#    true_freqs = ma.masked_where(true_freqs < 2, true_freqs)
#    true_times = float(samplerate) * ground_truth[:,0]
#    ax2.plot(true_times, true_freqs, 'r')
#    ax2.axis( ymin = 0.9 * true_freqs.min(), ymax = 1.1 * true_freqs.max() )
# plot raw pitches
#ax2.plot(times, pitches, '.g')
# plot cleaned up pitches
#cleaned_pitches = pitches
#cleaned_pitches = ma.masked_where(cleaned_pitches < 0, cleaned_pitches)
#cleaned_pitches = ma.masked_where(cleaned_pitches > 120, cleaned_pitches)
#cleaned_pitches = ma.masked_where(confidences < tolerance, cleaned_pitches)
#ax2.plot(times, cleaned_pitches, '.-')
#ax2.axis( ymin = 0.9 * cleaned_pitches.min(), ymax = 1.1 * cleaned_pitches.max() )
#ax2.axis( ymin = 55, ymax = 70 )
#plt.setp(ax2.get_xticklabels(), visible = False)
#ax2.set_ylabel('f0 (midi)')

# plot confidence
#ax3 = fig.add_subplot(313, sharex = ax1)
# plot the confidence
#ax3.plot(times, confidences)
# draw a line at tolerance
#ax3.plot(times, [tolerance]*len(confidences))
#ax3.axis( xmin = times[0], xmax = times[-1])
#ax3.set_ylabel('condidence')
#set_xlabels_sample2time(ax3, times[-1], samplerate)
#plt.show()
#plt.savefig(os.path.basename(filename) + '.svg')