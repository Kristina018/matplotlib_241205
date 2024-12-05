import matplotlib.pyplot as plt
import numpy as np

# A) Duotas sąrašas x=[1,2,3,4,5,6,7,8,9]
# Viename lange, skirtinguose grafikuose atvaizduokite 𝑥 , 𝑥 ⋅ 3,
# 𝑥 ⋅ 𝑎, čia a - įvedamas vartotojo.
# Panaudokite skirtingas spalvas, linijų tipus.

# %matplotlib qt

def squared(x):
    return x ** 2
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x_squared = x * 2
# x_3 = x * 3
# a = int(input(f'Įveskite kažkokį skaičių: '))
# x_input = x * a
langas, grafikas = plt.subplots(2, 2)
grafikas.plot(x, squared(x))
plt.show()

