import numpy as np
import matplotlib.pyplot as plt

# A) Duotas sąrašas x=[1,2,3,4,5,6,7,8,9]
# Viename lange, skirtinguose grafikuose atvaizduokite 𝑥^2, 𝑥⋅3, 𝑥⋅𝑎, čia a - įvedamas vartotojo.
# Panaudokite skirtingas spalvas, linijų tipus.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x_three = np.array(x) * 3
x_zero = np.array(x) * 0

def squared(x):
    return np.array(x) ** 2

def input_a():
    a = int(input(f'Įveskite kažkokį skaičių: '))
    return np.array(x) * a # tik asys keiciasi

langas, grafikas = plt.subplots(2, 2)
grafikas[0][0].plot(x, squared(x))
grafikas[0][1].plot(x, input_a())
grafikas[1][0].plot(x, x_three)
grafikas[1][1].plot(x, x_zero)


plt.show()

# y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# x_squared = x * 2
# x_3 = x * 3
# x_input = x * a