% ELEC 484 - Assignment 4
%
% Compressor Testing File

addpath('src');
clear all; close all;

% Compressor Test Settings
ratio = 4;      % Compression ratio
threshold = -4; % Threshold dB
attack = 100;   % Attack time ms
release = 250;  % Release time ms

fs = 48000;     % Sample rate
Ts = 1/fs;      % Sample period

f1 = 440;       % Sine wave frequency
L = fs * 4;     % Signal length
n = 0:L-1;      % Samples for creating a sine wave

% Calculate test signal
x = cos(2*pi*n*f1*Ts);

% Create an amplitude envelope for the input sine wave
env = zeros(1, L);

% Create amplitude envelope that cycles between high & low every second
highGain = 0;   % Envelope high part in dB
lowGain = -6;   % Envelope low part in dB
high = 10^(highGain/20);    % Linear amplitude high part
low = 10^(lowGain/20);      % Linear amplitude low part

for i = 1:L
    if mod(floor(i/fs),2) == 0
        env(i) = high;
    else
        env(i) = low;
    end
end

% Apply the amplitude envelope to the sine wave signal
x = x.*env;

%plot(1:length(x), x);
 
% Run compression on input signal
[y, static, dynamic] = compressor_james(x, fs, ratio, threshold, attack, release);

% Convert the static reduction from dB to linear scale
static = 10.^(static./20);

% Convert the dynamic gain reduction from dB to linear scale
dynamic =  10.^((-dynamic)./20);

% Convert samples to time for plotting
t = n./fs;

plot(t,abs(x), 'g');
hold on;
plot(t,abs(y),'b');
plot(t,static,'m', 'LineWidth', 2);
plot(t,dynamic,'c', 'LineWidth', 2);

title('Peak Compression Plot');
xlabel('Time (Seconds)');
ylabel('Amplitude');
legend('Input Signal (ABS)', 'Output Signal (ABS)', 'Static Gain', 'Dynamic Gain');

hold off;
