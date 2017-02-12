function [G_vector, X_vector, f_vector,g_vector,xrms_vector, output_vector] = compexp(x, fs, threshold,ratio)

tav = 0.01; %CHANGE
Ts = 1/fs;
TA = 5;
TR = 5;
%at = exp(2.2*Ts/1000*TA);  %CHANGE
%rt = exp(2.2*Ts/1000*TR); %CHANGE
delay = 150;%CHANGE?

L = length(x);
xrms = 0;
g = 1;
buffer = zeros(1,delay);
xrms_vector = zeros(1,L);
G_vector = zeros(1,L);
X_vector = zeros(1,L);
f_vector = zeros(1,L);
g_vector = zeros(1,L);
output_vector = zeros(1,L);

slope = 1-(1/ratio);

for n = 1:L
    
  xrms = (1-tav) * xrms + tav * x(n)^2;
  xrms_vector(n) = xrms;
  X = 10*log10(xrms);
  X_vector(n) = X;
  G = min([0, -slope*(X-threshold)]);
  %G = min([0, X+(X-threshold)/ratio]);
  G_vector(n) = G;
  f = 10^(G/20);
  f_vector(n) = f;
  if f < g
    coeff = 1-exp(-2.2*Ts/TA*1000);%at;
  else
    coeff = 1-exp(-2.2*Ts/TR*1000);%rt;
  end;
  g = (1-coeff) * g + coeff * f;
  g_vector(n) = g;
  output_vector(n) = g * buffer(end);
  buffer = [x(n) buffer(1:end-1)];
end;