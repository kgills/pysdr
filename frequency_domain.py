#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

Fs = 1 # Hz
N = 100 # number of points to simulate, and our FFT size
Ft = 0.15 # Hz

t = np.arange(N) # because our sample rate is 1 Hz
s = np.sin(Ft*2*np.pi*t)

# Apply windowing
s = s * np.hamming(N)

S = np.fft.fftshift(np.fft.fft(s))
S_mag = np.abs(S)
S_phase = np.angle(S)
f = np.arange(Fs/-2, Fs/2, Fs/N)
plt.figure(0)
plt.plot(f, S_mag,'.-')
plt.figure(1)
plt.plot(f, S_phase,'.-')
plt.show()
