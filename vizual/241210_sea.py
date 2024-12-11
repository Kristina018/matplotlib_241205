import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy.polynomial.polynomial as poly


# # Example data
# data = {
#     'x asis': [1, 2, 3, 4, 5],
#     'y asis': [2, 4, 6, 8, 10]
# }
#
# # Create the line plot
# sns.lineplot(x = 'x asis', y = 'y asis', data = data)
#
# # Show the plot
# plt.show()

# a = np.arange(1,11)
# b = np.random.randint(-5,25,10)
# sns.lineplot(x=a,y=b) #grąžina ašis (axes object)
# plt.show()

# #• Taškinis
# a = np.arange(1,11)
# b = np.random.randint(-5,25,10)
# sns.scatterplot(x=a,y=b) #grąžina ašis (axes object)
# plt.show()

rch = ['Red','Green','Blue'] #iš čia generuosime 30 atsitiktinių ↪ pasirinkimų
a = np.arange(1,31) # 1-30
b= np.random.randint(-5,50,30)
rng = np.random.default_rng() #pasirinkimų generatorius
r = rng.choice(rch, size=30) # 30 random iš rch.
df = pd.DataFrame(data={'x':a, 'y':b, 'h':r}) #df susikūrimas
sns.scatterplot(data=df, x='x',y='y',hue='h') #hue parametro # demonstracija
plt.show()

# df = pd.DataFrame(data={'x':[*range(0,5)], 'y':np.random.randint(0,10,5)})
# coef = np.polyfit(x=df['x'], y=df['y'], deg=1)
# ffit = poly.Polynomial(coef=coef[::-1])
# #ffit
#
# y_fitted = ffit(df['x'])
# plt.show()