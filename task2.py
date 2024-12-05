import numpy as np
import matplotlib.pyplot as plt

# B) Duoti sąrašai x = [1,2,3,4,5], y1=[2,2,0,0,2], y2 = [4,3,2,1,-1], y3 = [2,4,9,16,25], y4 = [-1,1,-1,1,-1]
# Atvaizduokite viename lange, skirtinguose grafikuose x~y1, x~y2, x~y3, x~y4 grafikus.
# Pirmasis grafikas - linijinis, antrasis - taškinis, trečiasis - linija su duomenų taškais,
# ketvirtasis - brūkšninis. Spalvos visų turi būti skirtingos. Grafikai, ašys turi turėti pavadinimus.

x = [1, 2, 3, 4, 5]
y1 = [2, 2, 0, 0, 2]
y2 = [4, 3, 2, 1, -1]
y3 = [2, 4, 9, 16, 25]
y4 = [-1, 1, -1, 1, -1]

# def squared(x):
#     return np.array(x) ** 2
#
# def input_a():
#     a = int(input(f'Įveskite kažkokį skaičių: '))
#     return np.array(x) * a # tik asys keiciasi

langas, grafikas = plt.subplots(2, 2)
grafikas[0][0].plot(x, y1)
grafikas[0][1].plot(x, y2)
grafikas[1][0].plot(x, y3)
grafikas[1][1].plot(x, y4)

plt.show()

# y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
