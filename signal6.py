import numpy as np
import scipy.fft as fft
import matplotlib.pyplot as plt
from scipy import signal as sg

fs = 1000
T = 1/fs
t = np.linspace(0, 1000, 1000, endpoint = False)
t = t * T
signal = 10 * np.sin(2 * np.pi * 50 * t) + 20 * np.sin(2 * np.pi * 100 * t) + 30 * np.sin(2 * np.pi * 200 * t) + 40 * np.sin(2 * np.pi * 300 *t)
timeAxis = np.linspace(0, len(signal), len(signal), endpoint = False)
plt.plot(timeAxis, signal)
plt.show()

signalFFT = fft.fft(signal, fs)
fAxis = np.linspace(0, fs//2, fs//2, endpoint = False)
plt.plot(fAxis, np.abs(signalFFT[:fs//2]))
plt.title("signal Spectrum")
plt.show()

b, a = sg.butter(8, 0.3, "highpass")        # 150Hz高通滤波器
signalHighPass = sg.filtfilt(b, a, signal)
signalFFT = fft.fft(signalHighPass, fs)
fAxis = np.linspace(0, fs//2, fs//2, endpoint = False)
plt.plot(fAxis, np.abs(signalFFT[:fs//2]))
plt.title("150Hz High pass filter")
plt.show()

b, a = sg.butter(8, 0.44, "lowpass")         # 220Hz低通滤波器
signalLowPass = sg.filtfilt(b, a, signal)
signalFFT = fft.fft(signalLowPass, fs)
fAxis = np.linspace(0, fs//2, fs//2, endpoint = False)
plt.plot(fAxis, np.abs(signalFFT[:fs//2]))
plt.title("220Hz Low pass filter")
plt.show()

b, a = sg.butter(8, [0.1, 0.5], "bandpass")
signalBandPass = sg.filtfilt(b, a, signal)
signalFFT = fft.fft(signalBandPass, fs)
fAxis = np.linspace(0, fs//2, fs//2, endpoint = False)
plt.plot(fAxis, np.abs(signalFFT[:fs//2]))
plt.title("50--250Hz Band pass filter")
plt.show()

b, a = sg.butter(8, [0.15, 0.44], "bandstop")
signalBandStop = sg.filtfilt(b, a, signal)
signalFFT = fft.fft(signalBandStop, fs)
fAxis = np.linspace(0, fs//2, fs//2, endpoint = False)
plt.plot(fAxis, np.abs(signalFFT[:fs//2]))
plt.title("75--220Hz Lowstop filter")
plt.show()