import matplotlib.pyplot as plt
import random


fig, ax = plt.subplots()  # Create a figure containing a single axes.

ax.set_title('Plot A and B')
ax.set_aspect('equal')
ax.set_xlabel('Age')
ax.set_ylabel('BMI')
ax.set_xlim(0,10)
ax.set_ylim(0,10)


x1 = [1, 2, 3, 4, 7, 8, 9]
y1 = [2, 3, 4, 6, 7, 8, 4]
ax.plot(x1,y1, label ='blue')
ax.scatter(x1, y1)  # Plot some data on the axes.

x2 = [1, 2, 3, 4, 7, 8, 9]
y2 = [1, 2, 3, 4, 3, 5, 7]
ax.plot(x2,y2, label = 'yellow')
ax.scatter(x2, y2)

ax.legend()
plt.savefig('plot.png')
plt.show()
