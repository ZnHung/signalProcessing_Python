import torch
import pyaudio
import librosa
import wave
import numpy as np
from matplotlib import pyplot as plt

Chunk = 1024
Format = pyaudio.paInt16
Channels = 1
Rate = 8000
recordSecond = 2
waveOutputFileName = "audio1.wav"

p = pyaudio.PyAudio()
stream = p.open(format = Format,
                channels = Channels,
                rate = Rate,
                input = True,
                frames_per_buffer = Chunk)

print("start Recording!..........")

frames = []

for i in range(0, int(Rate/Chunk * recordSecond)):
    data = stream.read(Chunk)
    frames.append(data)

print("end!.....")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(waveOutputFileName, "wb")
wf.setnchannels(Channels)
wf.setsampwidth(p.get_sample_size(Format))
wf.setframerate(Rate)
wf.writeframes(b''.join(frames))
wf.close()

def player(filename):
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    # stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)
    data = wf.readframes(Chunk)
    while data != b'':
        stream.write(data)
        data = wf.readframes(Chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()

filename = waveOutputFileName
player(filename)

f = wave.open(filename, 'rb')
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(params)
strData = f.readframes(nframes)
waveData = np.fromstring(strData, dtype = np.short)
waveData = waveData * 1.0 / max(abs(waveData))
waveData = np.reshape(waveData, [nframes, nchannels]).T
f.close()

time = np.arange(0, nframes) * (1/ framerate)
time = np.reshape(time, [nframes, 1]).T

plt.plot(time[0, :nframes], waveData[0, :nframes])
plt.show()

framelength = 0.025
framesize = framelength * framerate
nfft = {}
lists = [32, 64, 128, 256, 512, 1024]
for i in lists:
    nfft[i] = abs(framesize - i)

sortlist = sorted(nfft.items(), key = lambda X:X[1])

framesize = int(sortlist[0][0])
NFFT = framesize
overlapsize = int(round(1/3 * framesize))

spec, freq, ts, fig = plt.specgram(waveData[0], NFFT = NFFT, Fs = framerate, window = np.hanning(M = framesize), noverlap = overlapsize, \
                                   mode = "default", scale_by_freq = False, sides = "default", scale = "dB", xextent = None)
plt.show()
