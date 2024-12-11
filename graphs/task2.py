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

langas, grafikas = plt.subplots(2, 2)
grafikas[0][0].plot(x, y1, ls='-', label='line 1', color='red')
grafikas[0][1].plot(x, y2, ls='dashed', marker='o', color='green', label='2')
grafikas[1][0].plot(x, y3, ls='-.', label='label', color='blue')
grafikas[1][1].plot(x, y4, ls='dotted', color='purple', label='4')

grafikas[0][0].set_xlabel("I grafiko x ašis", fontsize='7', color='red')
grafikas[0][0].set_ylabel("I grafiko y ašis", fontsize='7', color='red')

grafikas[0][1].set_xlabel("II grafiko x ašis", fontsize='10', color='green')
grafikas[0][1].set_ylabel("II grafiko y ašis", fontsize='10', color='green')

grafikas[1][0].set_xlabel("III grafiko x ašis", fontsize='12', color='blue')
grafikas[1][0].set_ylabel("II grafiko y ašis", fontsize='12', color='blue')

grafikas[1][1].set_xlabel("IV grafiko x ašis", fontsize='20', color='purple')
grafikas[1][1].set_ylabel("IV grafiko y ašis", fontsize='20', color='purple')

grafikas[0,0].legend()
grafikas[0,1].legend()
grafikas[1,0].legend()
grafikas[1,1].legend()

plt.show()