import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Užduotis 1: Pardavimų duomenų stulpelinė diagrama
# ● Nubraižykite stulpelinę diagramą, kurioje pateikiami įmonės mėnesiniai pardavimai.
# ● Pridėkite etiketes kiekvienai juostai ir pritaikykite juostų spalvas.
# ● Įrašykite diagramai pavadinimą ir pažymėkite ašių pavadinimus.

months = ['January', 'February', 'March', 'April', 'May']
sales = [1500, 2000, 1800, 2200, 2100]
colors = ['indigo', 'navy', 'violet', 'midnightblue', 'crimson'] # ar rasiu kaip padaryti perejima spalvu pagal pardavimu kieki, kad issirikiuotu didejimo tvarka, o ne pagal menesius
fig, ax = plt.subplots()
labels = ['test', 'test', 'te', 'tes', 'test'] # 'Įmonės pardavimai'
ax.bar(months, sales, width = 0.5, label = labels, color = colors)
ax.legend()
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May'])

ax.set_ylabel('Eurai', fontsize = 15)
ax.set_xlabel('Mėnesiai', fontsize = 15)
ax.set_title('Pusmečio pardavimai', fontsize = 17)
ax.tick_params(axis = 'x', labelsize = 12)
ax.tick_params(axis = 'y', labelsize = 12)

plt.show()

# TEMPERATUROS
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
# fig.tight_layout() # ka jis daro?
# plt.show()