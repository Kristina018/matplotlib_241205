import numpy as np
import matplotlib.pyplot as plt
import matplotlib

a = np.random.randint(2,20,10)
b = np.random.rand(10) * 10.0
c = np.random.rand(100) * 3.0
avg_a = np.average(a)
avg_b = np.average(b)
avg_c = np.average(c)
fig, ax = plt.subplots()
ax.boxplot([a,b,c], zorder = 1)
ax.scatter([1,2,3], [avg_a, avg_b, avg_c], color = "xkcd:marine", zorder = 3)
ax.plot([1,2,3], [avg_a,avg_b, avg_c], color='red', zorder=2)
ax.bar([1,2,3], [avg_a * 0.75, avg_b * .75, avg_c * .75], width = 0.15, color = 'green', zorder = 0, label = 'nice, very nce')
ax.set_xticks([1,2,3])
ax.set_xticklabels(['a', 'b', 'c'])
ax.legend()
plt.show()