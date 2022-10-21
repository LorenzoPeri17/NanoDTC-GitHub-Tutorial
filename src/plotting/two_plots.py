import matplotlib.pyplot as plt
import numpy as np


dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))  # white noise 1
nse2 = np.random.randn(len(t))  # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, s1, "-k")
ax1.plot(t, s2, "--r")
ax1.set_xlim(0, 2)
ax1.set_xlabel("time")
ax1.set_ylabel("s1 and s2")
ax1.grid(True)

ax2.plot(np.fft.fftfreq(len(t), dt), np.abs(np.fft.fft(s1)), "o", color="grey")
ax2.plot(np.fft.fftfreq(len(t), dt), np.abs(np.fft.fft(s2)), "D", color="magenta")
ax1.set_xlabel("frequency")
ax1.set_ylabel("fft")

fig.tight_layout()
plt.show()
