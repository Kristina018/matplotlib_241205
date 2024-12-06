import numpy as np
import matplotlib.pyplot as plt

# x = [1,2,3]
# y = [9,6,8]
# fig, ax = plt.subplots()
# ax.bar(x,y)
# plt.show()

# x = [1, 2, 3]
# y = [9, 6, 8]
# fig, ax = plt.subplots()
# ax.bar(x, y, color='green', label = 'Žali', width = 0.25)
# ax.legend()
# plt.show()

# x = [1,2,3]
# y = [9,6,8]
# fig, ax = plt.subplots()
# ax.bar(x,y, color='green', label='Žali', width=0.25)
# ax.set_xticks(x)
# ax.set_xticklabels(['Sausis', 'Vasaris', 'Kovas'])
# ax.legend()
# plt.show()

# x = [1,2,3]
# y = [9,6,8]
# fig, ax = plt.subplots()
# ax.bar(x,y, color='green', label='Žali', width=0.25)
# ax.set_xticks(x)
# ax.set_xticklabels(['Sausis', 'Vasaris', 'Kovas'])
# ax.set_ylabel('Skaičiai', fontsize=16)
# ax.set_xlabel('Mėnesiai', fontsize=16)
# ax.set_title('Stulpelinė diagrama', fontsize=22)
# ax.tick_params(axis='x', labelsize=16)
# ax.tick_params(axis='y', labelsize=16)
# ax.legend()
# fig.tight_layout()
# plt.show()
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# x = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22] # ka tai duoda?..
tC = [-3.2, -3.2, +0.4, +6.7, +12.4, +15.4, +17.9, +17.1, +12.3, +7.2, +1.9, -1.9]
fig, ax = plt.subplots()
ax.bar(x, tC, color='green', label='temperos', width=0.5)
ax.set_xticks(x)
ax.set_xticklabels(['sau', 'vas', 'kov', 'bal', 'geg', 'bir', 'lie', 'rugp', 'rugs', 'spa', 'lap', 'gru'])
ax.set_ylabel('Laipsniai C', fontsize=15)
ax.set_xlabel('Mėnesiai', fontsize=15)
ax.set_title('Stulpelinė diagrama', fontsize=20)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)
ax.legend()
fig.tight_layout() # ka jis daro?
plt.show()