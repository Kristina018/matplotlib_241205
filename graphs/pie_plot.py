import matplotlib.pyplot as plt

x = [1,2,3,5,8]
explode = [0,0,0,0,0.25]
fig, ax = plt.subplots()
ax.pie(x, labels = x, explode = explode, autopct = '%1.2f%%', shadow = True)
plt.show()