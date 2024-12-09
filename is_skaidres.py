import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
fig, ax = plt.subplots()
ax.plot(t1, f(t1), color='red', marker='d', ms=12, linewidth=3.0, label='$e^{-x}\cdot\cos(2\pi x)$')
ax.set_ylabel('Y ašies pavadinimas')
ax.set_xlabel('X ašies pavadinimas')
ax.set_title('Grafiko pavadinimas')
ax.legend(loc=9) # 0 - 9
plt.show()