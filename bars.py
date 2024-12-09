import numpy as np
import matplotlib.pyplot as plt
import matplotlib

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

# TEMPERATUROS
# x = ['sau', 'vas', 'kov', 'bal', 'geg', 'bir', 'lie', 'rugp', 'rugs', 'spa', 'lap', 'gru']
# # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# # x = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22] # ka tai duoda?..
# tC = [-3.2, -3.2, 0.4, +6.7, +12.4, +15.4, +17.9, +17.1, +12.3, +7.2, +1.9, -1.9]
# fig, ax = plt.subplots()
#
# ax.bar(x, tC, color = ['green' if t > 0 else 'blue' for t in tC], label = 'BLUE', width = 0.5)
# # label spalba lieka melyna, tai zaliu kaip ir "nepaaiskina"
#
# # ax.bar(x, tC, color = 'green', label = 'temperos', width = 0.5)
# # ax.set_xticks(x)
# # ax.set_xticklabels(['sau', 'vas', 'kov', 'bal', 'geg', 'bir', 'lie', 'rugp', 'rugs', 'spa', 'lap', 'gru'])
# ax.set_ylabel('Laipsniai C', fontsize = 15)
# ax.set_xlabel('Mėnesiai', fontsize = 15)
# ax.set_title('Stulpelinė diagrama', fontsize = 20)
# ax.tick_params(axis = 'x', labelsize = 12)
# ax.tick_params(axis = 'y', labelsize = 12)
# ax.legend()
# fig.tight_layout() # ka jis daro?
# plt.show()

# # TEMPERATUROS kaip isspresta skaidrej
# tC = [-3.2, -3.2, +0.4, +6.7, +12.4, +15.4, +17.9, +17.1, +12.3, +7.2, +1.9, -1.9]
# colors = []
# x = np.arange(1, len(tC) + 1.0)
# for i in tC:
#     if i < 0:
#         colors.append('blue')
#     else:
#         colors.append('green')
# months = ['Saus.', 'Vas.', 'Kov.', 'Bal.', 'Geg.', 'Bir.', 'Liep.', 'Rugpj.', 'Rugs.', 'Spa.', 'Lapk.', 'Gruod.']
# fig, ax = plt.subplots()
# P = ax.bar(x, tC, color = colors)
# if float('{}'. format(matplotlib. __version__)[0:3]) >= 3.4:
#     plt.bar_label(P, fmt = '%.2f') #fmt - teksto formatas
# else:
#     for i in range(1, len(months)):
#         a = i
#         b = tC[i - 1]
#         txt = str(b)
#         ax.text(a * 0.99, b * 1.01, txt)
# ax.set_xticks(x)
# ax.set_xticklabels(months, rotation = 45)
# fig.tight_layout()
# plt.show()