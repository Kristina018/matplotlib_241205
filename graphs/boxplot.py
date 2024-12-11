import numpy as np
import matplotlib.pyplot as plt
import matplotlib

a = np.random.randint(2, 20, 10)
b = np.random.rand(10) * 10.0
fig, ax = plt.subplots()
ax.boxplot([a, b], showmeans = True)
ax.set_xticks([1, 2])
ax.set_xticklabels(['a', 'b'])
plt.show()

