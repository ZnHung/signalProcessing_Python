import numpy as np
import matplotlib.pyplot as plt
import os
import wave

path = "bluesky1.wav"
filename = path
f = wave.open(filename, "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(params)
strData = f.readframes(nframes)
waveData = np.fromstring(strData, dtype = np.short)
waveData = waveData * 1.0 /max(abs(waveData))
waveData = np.reshape(waveData, [nframes, nchannels]).T
f.close()

time = np.arange(0, nframes) * (1 / framerate)
time = np.reshape(time, [nframes, 1]). T
plt.plot(time[0, :nframes], waveData[0, :nframes])
plt.title("Origin Wave")
plt.show()

framelength = 0.025
framesize = framelength * framerate
nfft = { }      # 建立一个空的字典
lists = [32, 64, 128, 256, 512, 1024]
for i in lists:
    nfft[i] = abs(framesize - i)
    print("nfft[i]=", nfft[i])
sortlist = sorted(nfft.items(), key = lambda x: x[1])
# nfft为一个字典，将每一对nfft的第2个元素作为排序的依据进行排序，选择出最合适的用来做fft的点数

framesize = int(sortlist[0][0])
print(framesize)
# sortlist[0][0]为最适合用来做fft的点数

NFFT = framesize
overlapSize = 1.0/3 * framesize
overlapSize = int(round(overlapSize))  # round 返回浮点数的四舍五入值
spectrum, freq, ts, fig = plt.specgram(waveData[0], NFFT = NFFT, Fs = framerate, window = np.hanning(M = framesize), noverlap = overlapSize, \
                                       mode = "default", scale_by_freq = False, sides = 'default', scale = 'dB', xextent = None)
                                      # mode : 使用什么样的频谱，默认为PSD谱（功率谱）{'default', 'psd', 'magnitude', 'angle', 'phase'}
                                      # scale_by_freq : bool, optional是否按密度缩放频率
                                      # sides : {'default', 'onesided', 'twosided'}单边频谱或双边谱
                                      # scale : {'default', 'linear', 'dB'}频谱纵坐标单位,默认为dB
                                      # xextent : None or (xmin, xmax)图像x轴范围

# spectrum:频谱矩阵
# freqs：频谱图每行对应的频率
# ts：频谱图每列对应的时间
# fig ：图像

plt.show()