import matplotlib.pyplot as plt

x = list(range(1,101))
squares = [i**2 for i in x]


fig, ax = plt.subplots()
ax.scatter(x, squares, c=squares, cmap=plt.cm.Blues,s=10)

plt.style.use('seaborn-v0_8-pastel')
ax.ticklabel_format(style='plain')



plt.show()

