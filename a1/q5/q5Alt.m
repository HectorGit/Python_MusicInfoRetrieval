clc;

sizeFFT = 1024;
sizeWindow = 128;

filename = 'outSinusoid.wav';

[inputSamples,Fs] = audioread(filename);

disp('inputSamples(1:sizeWindow)');
disp(inputSamples(1:sizeWindow));
disp(size(inputSamples(1:sizeWindow)));

fftData = fft(inputSamples(1:sizeWindow),sizeFFT); %real and imaginary

disp('fftData(1:25)');
disp(fftData(1:25));
disp(size(fftData));

ifftData = ifft(fftData,sizeWindow);

disp('ifftData(1:25)');
disp(ifftData(1:25));
disp(size(ifftData));

soundsc(real(ifftData),Fs);



