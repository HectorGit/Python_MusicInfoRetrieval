clc;
clear;

filename = 'violaCsharp.wav';

[inputSamples,Fs] = audioread(filename);

L = length(inputSamples); 

windowSize = 2048; 

num_Avail_Windows = floor(L/windowSize); 

sizeOfFFT = 2048;

fftData = zeros(sizeOfFFT,1);   
inversefftData = zeros(windowSize,1);
inversefftSamples = zeros(1,1);

for i = 1:num_Avail_Windows-1

    curr_input_samples = inputSamples(i*windowSize:(i+1)*windowSize); 
    
    Y = fft(curr_input_samples,sizeOfFFT); 
    fftData = fftData + Y; %real and imaginary
   
    inversefftData = ifft(Y,windowSize); 

    inversefftSamples = [inversefftSamples; inversefftData];
    
end    

disp('sounding');
soundsc((1/L).*abs(inversefftSamples),Fs);
disp('sounded');
audiowrite('outInverseFFT.wav',(1/L).*abs(inversefftSamples),Fs);

magn_spectrum = abs(real(fftData)/L);
magn_spectrum = magn_spectrum(1:sizeOfFFT/2);

f = (Fs/sizeOfFFT).*(0:sizeOfFFT/2-1);

plot(f,magn_spectrum);

title 'Magnitude Spectrum'
ylabel 'DFT magnitude'
xlabel('f (Hz)')
ylabel('|Magnitude|')

