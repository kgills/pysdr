#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

Fs = 8e6 # sample rate
Ts = 1/Fs # sample period
N = 2048 # number of samples to simulate
Ft = 2.4e9
# center_freq = 2.4e9 # frequency we tuned our SDR to

t = Ts*np.arange(N)
x = np.exp(1j*2*np.pi*Ft*t) # simulates sinusoid at 50 Hz

# add the following line after doing x = x[0:1024]
x = x * np.hamming(len(x)) # apply a Hamming window

n = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2) # complex noise with unity power
noise_power = 2
r = x + n * np.sqrt(noise_power)

PSD = (np.abs(np.fft.fft(r))/N)**2
PSD_log = 10.0*np.log10(PSD)
PSD_shifted = np.fft.fftshift(PSD_log)

f = np.arange(Fs/-2.0, Fs/2.0, Fs/N) # start, stop, step
f += Ft

plt.plot(f, PSD_shifted)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.grid(True)
plt.show()
