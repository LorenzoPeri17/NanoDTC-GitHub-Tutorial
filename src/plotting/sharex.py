import matplotlib.pyplot as plt
import numpy as np


dt = 0.01
t = np.arange(0, 30, dt)


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(t, np.sin(t), "-k")
ax2.plot(t, np.cos(t), "--r")

ax2.set_xlabel("time")
ax1.set_ylabel("sin")
ax2.set_ylabel("cos")

fig.tight_layout()
plt.show()
