
clear;
clc;
% THIS DOESN'T BUFFER THE DATA!
%For some reason when you buffer
%the data matlab doens’t playback 
%the ifftData directly, because it’s not real
filename = 'battleScene.wav';
[inputSamples,Fs] = audioread(filename);
fftData = fft(inputSamples); 
ifftData = ifft(fftData);
soundsc(ifftData,Fs);


