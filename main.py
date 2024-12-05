import matplotlib.pyplot as plt
import numpy as np

# langas, grafikas = plt.subplots()
# x = [1,2,3,4,5]
# # y = [1,3,6,8,9]
# y = [1,5,2,10,3]
# grafikas.plot(x,y)
# plt.show()

# langas, grafikas = plt.subplots(2,2)
# x1 = [1,2,3,4,5]
# x2 = [1,4,6,8,10]
# y1 = [1,3,6,8,9]
# y2 = [1,5,2,10,3]
# grafikas[0][0].plot(x1,y1)
# grafikas[0][1].plot(x2,y1)
# grafikas[1][0].plot(x1,y2)
# grafikas[1][1].plot(x2,y2)
# plt.show()

# langas, grafikas = plt.subplots(2,2)
# x1 = [1,2,3,4,5]
# x2 = [1,2,3,4,5,6,7,8,9,10]
# y1 = [1,3,6,8,9,5,7,8,6,4]
# y2 = [1,5,2,10,3]
# grafikas[0][0].plot(x1,y1[::2])
# grafikas[0][1].plot(x2,y1)
# grafikas[1][0].plot(x1,y2)
# grafikas[1][1].plot(x2[::2],y2)
# plt.show()

# langas, grafikas = plt.subplots()
# y = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
# x = [1,5,2,4,3,4,5,3,2,4]
# grafikas.plot(y,x)
# plt.show()

# langas, grafikas = plt.subplots()
# x = np.array([1,5,2,4,3,4,5,3,2,4,8,5,8,6,0,1,0,10,7,8,5,10,9,9,7,8,6,4,3,4,5])
# y = np.linspace(x.min(),x.max(),x.size)
# grafikas.plot(y, x) #piesia linija
# grafikas.scatter(y, x) # rodo taskus
# plt.show()

# langas, grafikas = plt.subplots()
# x = [1,2,3,4,5]
# y = [1,5,2,6,3]
# grafikas.plot(x,y,color="red",marker="d", ms=12,lw=3) #ms = marker size; lw = line weight
# grafikas.set_xlabel("gauti pazymiai")
# grafikas.set_ylabel("ivertinimu ribos", fontsize=15)
# grafikas.set_title("mokinio rezultatai")
# grafikas.tick_params(axis='x',labelsize=20)
# # grafikas.legend(loc=10)
# plt.show()


# langas, grafikas = plt.subplots()
# x = [1,2,3,4,5]
# y = [1,5,2,6,3]
# grafikas.scatter(x,y,color="red",marker="o") #ms = marker size; lw = line weight
# # grafikas.legend(loc=10)
# plt.show()


# # dvi linijos, su skirtingu spalvu linijomis IR taskais
# langas, grafikas = plt.subplots()
# x = [1, 2, 3, 4, 5]
# y1 = [1, 3, 6, 8, 9]
# y = [1, 5, 2, 10, 3]
# grafikas.scatter(x, y, color="red")
# grafikas.scatter(x, y1, color="red")
# grafikas.plot(x, y, color="yellow")
# grafikas.plot(x, y1, color="blue")
# langas.tight_layout()
# plt.show()

# matric = np.array([[1, 2, 3], [4, 2, 6],[1,2,3],[6,7,8]])
# langas, grafikas = plt.subplots(2)
# print(matric[0])
# print(matric[1])
# grafikas[0].plot(matric[0],matric[1])
# grafikas[0].plot(matric[2],matric[3], color='red') # dvi matricos grafos vienoje lenteleje
# grafikas[1].plot(matric[2],matric[3], color='red') #dvi matricos grafos atskirose lentelese
#
# plt.show()
# print(matric)


# matrix_3d = np.random.randint(0, 20, (4, 5, 5))
# langas, grafikas = plt.subplots(2, 2)
#
# for i in range(2):
#     for j in range(2):
#         grafikas[i, j].plot(matrix_3d[i * 2 + j][0]) # Plot only the first row
#         # grafikas[i, j].set_title(f"Matrix {i * 2 + j}")
#
# plt.tight_layout()
# plt.show()


# from mpl_toolkits.mplot3d import Axes3D
# matrix_3d = np.random.randint(0, 20, (4, 5, 5))
#
# fig = plt.figure(figsize=(10, 10))
# ax = fig.add_subplot(111, projection='3d')
#
# # Generate a grid of x, y coordinates for plotting
# x = np.arange(matrix_3d.shape[1])
# y = np.arange(matrix_3d.shape[2])
# x, y = np.meshgrid(x, y)
#
# # Plot each matrix in 3D (for example, using matrix_3d[0] as an example)
# ax.plot_surface(x, y, matrix_3d[0], cmap='viridis')

# plt.show()