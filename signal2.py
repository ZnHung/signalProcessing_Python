import numpy as np
from matplotlib import pyplot as plt

SAMPLE_RATE = 44100
DURATION = 5

def generate_sin_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, sample_rate * duration, endpoint = False )
    y = 100 * np.cos((2 * np.pi) * freq * t)
    return t, y

t, signal = generate_sin_wave(2000, SAMPLE_RATE, DURATION)
plt.plot(t, signal)
plt.show()

yft = np.fft.fft(signal, SAMPLE_RATE)
print("len(yft) = ", len(yft))
f = np.linspace(0, SAMPLE_RATE, SAMPLE_RATE, endpoint = False)
print("len(f) = ", len(f))
plt.plot(f, yft)
plt.show()

plt.plot(f[:(len(f)//2-1)], yft[:(len(yft)//2-1)])
plt.show()