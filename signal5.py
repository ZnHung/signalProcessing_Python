import numpy as np
import matplotlib.pyplot as plt
import os
import wave
from scipy.io import wavfile

path = "bluesky1.wav"
f = wave.open(path, 'rb')
params = f.getparams()
print("params:\n", params)
nchannels, sampwidth, framerate, nframes = params[: 4]
print("params:\n", params[: 4])
voiceStrData = f.readframes(nframes)                        # nframes = 32000 为采样总点数
print("nframes = ", nframes, type(nframes))
waveData = np.fromstring(voiceStrData, dtype = np.short)
waveData = waveData * 1.0 / max(abs(waveData))
waveData = np.reshape(waveData, [nframes, nchannels]). T
f.close()

time = np.arange(0, nframes) * (1.0/ framerate)
plt.plot(time, waveData[0, :], c = 'b')
plt.show()


filename = 'bluesky1.wav'
WAVE = wave.open(filename)
print("WAV FILE INFORMATION----------------------------")
params = WAVE.getparams()
for item in enumerate(params):
    numberPoint = params.nframes        # 采样点个数
    f = params.framerate                # 采样率
    samplePeriod = 1/f                  # 采样周期
    timeLength = numberPoint/f          # 音频时间长度（单位：秒）

sampleRate, audioSequence = wavfile.read(filename)
# sampleRate为采样率
# audioSequence 为音频序列

print(audioSequence)

xAxis = np.arange(0, timeLength, samplePeriod)
plt.plot(xAxis, audioSequence)
plt.show()

wavfreq = np.fft.fft(audioSequence, sampleRate)
print(len(wavfreq), type(len(wavfreq)))
fAxis = np.linspace(0, sampleRate//2, sampleRate//2, endpoint = False)
print(len(wavfreq))
plt.plot(fAxis, np.abs(wavfreq[:len(wavfreq)//2]))
plt.show()