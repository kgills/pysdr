#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import sys

numSymbols = 4
modulationIndex = 0.5
sampleRate = 8
symbolRate = 1
centerFreq = 2

samplesPerSymbol = sampleRate/symbolRate

# Used for graphing smooth lines between samples
upSampleFactor = centerFreq/symbolRate*samplesPerSymbol

# Create random data bits
dataBits = np.random.randint(0, 2, numSymbols)

# Make the bits not random for debugging
dataBits[0] = 0
dataBits[1] = 0
dataBits[2] = 1
dataBits[3] = 1

# Convert data to -1,1
dataBits = dataBits * 2 - 1

# Spread the phase change over the symbol
dataBits = dataBits / (samplesPerSymbol)
dataBits = np.repeat(dataBits, samplesPerSymbol)

# Accumulate the phase change
dataBits = dataBits.cumsum()
dataBits = dataBits * np.pi*modulationIndex

# Create the time vector
t = np.arange(numSymbols * sampleRate / symbolRate ) / sampleRate

I = np.cos(2*np.pi*symbolRate*t + dataBits)
Q = np.sin(2*np.pi*symbolRate*t + dataBits)

# Upscale to create smooth lines to connect the samples
t_up = np.linspace(t.min(), t.max(),int(numSymbols*samplesPerSymbol*upSampleFactor))

tI = interp1d(t, I, kind='quadratic')
tQ = interp1d(t, Q, kind='quadratic')
I_smooth=tI(t_up)
Q_smooth=tQ(t_up)

# Create the plots
fig, axs = plt.subplots(2)

axs[0].plot(t_up, I_smooth, color="blue")
axs[0].plot(t_up, Q_smooth, color="red")

# Plot the IQ samples
axs[0].plot(t, I,'.', label="I", color="blue")
axs[0].plot(t, Q,'.', label="Q", color="red")
axs[0].legend(loc='lower left')

# Mixed signal
X = I*np.cos(centerFreq*2*np.pi*t) + Q*np.sin(centerFreq*2*np.pi*t)

# Upscale the mixed signal
X_smooth = I_smooth*np.cos(centerFreq*2*np.pi*t_up) + Q_smooth*np.sin(centerFreq*2*np.pi*t_up)

axs[1].plot(t,X,'.',label="X", color="green")
axs[1].plot(t_up,X_smooth, color="green")
axs[1].legend(loc='lower left')

plt.show()
