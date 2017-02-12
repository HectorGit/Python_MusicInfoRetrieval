function y = compexpModified(x, fs,  CT, ratio, tauAttack, tauRelease)

 %x = input buffer
 buffer_size = length(x);
 sample_rate = fs;

 threshold = CT;
 ratio; % is this true?

 tauAttack = at;
 tauRelease = rt;
 
 yL_prev = 0;
 %how big to make these buffers?
 x_g = zeros(1, buffer_size); 
 x_l = zeros(1, buffer_size); 
 y_g = zeros(1, buffer_size); 
 y_l = zeros(1, buffer_size);
 c = zeros(1, buffer_size);
 
 makeUpGain = 0;
 alphaAttack = exp(-1/(0.001*samplerate*tauAttack));
 alphaRelease = exp(-1/(0.001*samplerate*tauRelease));
 
 for n = 1:length(x)
    if(abs(x(n))<0.000001)
        x_g(n) = -120;
    else
        x_g(n) = 20*log(abs(x(n)));
    end
    
    if(x_g(n) >= threshold)
        y_g(n) = threshold + (x_g(n) - threshold) / ratio;
    else
        y_g(n)= x_g(n);
    end
        
    x_l(n) = x_g(n) - y_g(n);
    
    if(x_l(0)>yL_prev)
        y_l(n) = alphaAttack * yL_prev + (1-alphaAttack) * x_l(n);
    else
        y_l(n) = alphaRelease * yL_prev + (1-alphaRelease) * x_l(n);
    end
    
    c(n) = 10^((makeUpGain- y_l(n))/20);
    yL_prev = y_l(n);
 end
 
 for n: 1:length(x)
     x(n) = x(n)*c(n);
 end
 
 
end