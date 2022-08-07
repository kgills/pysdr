#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

sample_rate = 1e6

# Generate tone plus noise
t = np.arange(1024*1000)/sample_rate # time vector
f = 100e3 # freq of tone
x = np.sin(2*np.pi*f*t) + 0.2*np.random.randn(len(t))

f = 50e3 # freq of tone
x = x + np.sin(2*np.pi*f*t) + 0.2*np.random.randn(len(t))

# plt.plot(t[:200], x[:200],'.-')
# plt.show()


# simulate the signal above, or use your own signal

fft_size = 1024
num_rows = int(np.floor(len(x)/fft_size))
print("num_rows:",num_rows)
spectrogram = np.zeros((num_rows, fft_size))
for i in range(num_rows):
    spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x[i*fft_size:(i+1)*fft_size])))**2)
spectrogram = spectrogram[:,fft_size//2:] # get rid of negative freqs because we simulated a real signal

plt.imshow(spectrogram, aspect='auto', extent = [0, sample_rate/2/1e6, 0, len(x)/sample_rate])
plt.xlabel("Frequency [MHz]")
plt.ylabel("Time [s]")
plt.show()
