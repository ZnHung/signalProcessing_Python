import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# 采样频率
fs = 100
T = 1/fs

# 生成信号
t = np.arange(0, 100)
t = t * T
N = len(t)
# y = 10*np.sin(20*2*np.pi*t)
y = 10*np.sin(20*2*np.pi*t) + 20*np.sin(30*2*np.pi*t)

# 傅里叶变换
yf = np.fft.fft(y, fs)
# xf = fftfreq(N, 1/fs)# [:N//2]
d = np.abs(yf)
xf = np.arange(0, len(yf))
print("yf = ",len(yf))
# 画图

# plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.plot(xf, np.abs(yf))
plt.xlabel('Frequency (B:Hz)')
plt.ylabel('Amplitude (A)')
plt.grid()
plt.show()