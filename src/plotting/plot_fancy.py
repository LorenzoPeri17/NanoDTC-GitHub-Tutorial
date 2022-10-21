import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"text.usetex": True, "font.family": "serif", "font.size": 27})

minpow = 1
maxpow = 7

num = 100

x = np.linspace(0.1, 10, num=num)


fig, ax = plt.subplots(1, 1)

color = plt.cm.rainbow(np.linspace(0, 1, maxpow - minpow))

for n, c in enumerate(color):
    ax.plot(x, x**-n, label=f"{n}", color=c)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$x^{-n}$")

ax.set_xscale("log")
ax.set_yscale("log")

ax.legend(loc="upper right", fontsize=17)

plt.tight_layout()
plt.show()
