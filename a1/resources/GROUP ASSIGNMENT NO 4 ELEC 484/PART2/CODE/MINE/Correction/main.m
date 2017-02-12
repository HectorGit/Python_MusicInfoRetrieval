%generate sinusoid
clear all;
close all;

fs = 11000;
T = 1/fs;
freq = (fs/2)/4; %pi/2 
L = fs*8;
n = (0:L-1);
x = 0.1*sin(2*pi*freq*T*n);

envelope = zeros(1,L);
highgain = 0; %gain in decibels
lowgain = -6;
high = 10^(highgain/20); %because this is linear it is the inverse of 10 log (x1/x2)^2 = 20 log (R)
low = 10^(lowgain/20);

%OBTAIN sinusoid to input to the compressor:
%plot resulting sinusoid.
for n = 1:L
    if mod(floor(n/fs), 2)==0 %envelope changes every 300 milliseconds.
        envelope(n) = high;
    else
        envelope(n) = low;
    end
end

%apply envelope
x = x.*envelope;
%plot(1:length(x), x);

%PARAMETERS (x, CT, ratio)
[G_vector, X_vector, f_vector,g_vector, xrms_vector, output_vector]= compexp(x,fs,-25, 4);

l = linspace(1,length(x),L);
%m = logspace(1,length(x),L);

figure(1)
plot(l, x);
title('input');


figure(2)
plot(l, f_vector);%STATIC (Linear)
title('Static Gain');

figure(3)
plot(l, g_vector);%DYNAMIC (Linear)
title('Dynamic Gain');

figure(4)
plot(l, output_vector); %COMPRESSED OUTPUT (Linear)
title('Output');

figure(5) %rms measurement?
plot(l, xrms_vector); %envelope?
title('rms measurment result');
grid on;

figure(6)
plot(l, G_vector); %gain to be applied?
title('Gain to be applied');
grid on;

figure(7)
plot(l, X_vector); %envelope?
title('Amplitude in dB of the Input');
grid on;




