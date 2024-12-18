import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return (np.exp(-t) * np.cos(2 * np.pi * t))
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
fig, ax = plt.subplots()
ax.plot(t1, f(t1), color = 'red', marker = 'd', ms = 12, lw = 3.0)
plt.show()