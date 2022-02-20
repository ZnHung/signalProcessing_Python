import numpy as np
from matplotlib import pyplot as plt
sampleRate = 8000
fft_size = 512
t = np.arange(0, 1, 1/sampleRate)
x = np.sin(2 * np.pi * 156.25 * t) + 2 * np.sin(2 * np.pi * 234 * t)
xs = x[: sampleRate]
xf = np.fft.fft(xs)
xp = np.fft.rfft(xs) / sampleRate
f = np.linspace(0, sampleRate, sampleRate, endpoint = False)

plt.plot(f, np.abs(xf))
plt.show()

f = np.linspace(0, len(xp), len(xp), endpoint = False)
plt.plot(f, xp)
plt.show()


