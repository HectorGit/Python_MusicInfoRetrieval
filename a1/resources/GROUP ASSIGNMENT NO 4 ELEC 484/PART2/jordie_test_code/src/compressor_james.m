function [output,output_gain,output_reduction] = compressor(input, sr, ratio, threshold, attack_tau, release_tau)
% Apply compression to the input signal.
%   param input: Input vector in samples
%   param sr: Sample rate in Hz
%   param ratio: Double ratio representing gain reduction
%   param threshold: dB threshold after which gain reduction should be
%   applied to the input signal
%   param attack_tau: Attack time in ms
%   param release_tau: Release time in ms

    input_length = length(input);
    
    % Working buffers for calculating control voltage
    input_gain = zeros(input_length, 1);
    output_gain = zeros(input_length, 1);
    input_reduction = zeros(input_length, 1);
    output_reduction = zeros(input_length, 1);
    
    % Peak detection smoothing variables
    peakAttack = 0;    % Peak attack in ms
    peakRelease = 25;  % Peak release in ms
    pAttack = exp(-1/(0.001 *sr * peakAttack));
    pRelease = exp(-1/(0.001 * sr * peakRelease));

    % Output buffer
    output = zeros(input_length, 1);
    
    noise_floor = 0.000001; % Lowest representable amplitude
    makeup = 0; % Makeup gain
    
    attack_alpha = exp(-1/(0.001 * sr * attack_tau));
    release_alpha = exp(-1/(0.001 * sr * release_tau));
    
    % Variable to track previous gain reduction for ballistics
    prev_gain_reduction = 0;
    prev_input_gain = -120;
    
    for n = 1:input_length
        % Level detection 
        if abs(input(n)) < noise_floor
            input_gain(n) = -120;
        else
            input_gain(n) = 20.0*log10(abs(input(n)));
        end
        
        % Apply peak detection smoothing
        if input_gain(n) > prev_input_gain
            input_gain(n) = prev_input_gain * pAttack + (1 - pAttack) * input_gain(n);
        else
            input_gain(n) = prev_input_gain * pRelease + (1 - pRelease) * input_gain(n);
        end
        
        prev_input_gain = input_gain(n);
        
        % Gain computation: Apply static curve
        if input_gain(n) >= threshold
            % If we exceed the threshold, apply the ratio to reduce the
            % gain by the correct amount
            output_gain(n) = threshold + ((input_gain(n) - threshold) / ratio);
        else
            output_gain(n) = input_gain(n);
        end
        
        % Calculate the amount of gain reduction in dB
        input_reduction(n) = input_gain(n) - output_gain(n);
        
        % Apply attack/release ballistics to smooth out the gain
        if input_reduction(n) > prev_gain_reduction
            output_reduction(n) = (attack_alpha * prev_gain_reduction) + ((1-attack_alpha) * input_reduction(n));
        else
            output_reduction(n) = (release_alpha * prev_gain_reduction) + ((1-release_alpha) * input_reduction(n));
        end
        
        % Calculate the control voltage
        cv = 10.0^((makeup - output_reduction(n)) / 20.0);
        prev_gain_reduction = output_reduction(n);
        
        % Apply control voltage to input and add to output
        output(n) = input(n) * cv; 
    end
end

