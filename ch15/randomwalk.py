import matplotlib.pyplot as plt
import random

# x= list(range(100))
# y= list(range(100,200))

x = [random.randint(0,100) for _ in range(100)]
y = [random.randint(0,100) for _ in range(100)]

x_walks = [5,-5]
y_walks = [5,-5]

x_data, y_data= [],[]
x,y=0,0

x_data.append(x)
y_data.append(y)
for x_move,y_move in zip(x_walks,y_walks):
    x,y = x+x_move , y+y_move
    x_data.append(x)
    y_data.append(y)
    
print(x,y)

fig ,ax = plt.subplots()
# ax.plot(x[:50],y[:50], color='red')
# ax.scatter(x[50:],y[50:], color='blue')
# ax.plot(x[:50],y[:50],color='red')
# ax.scatter(x[50:],y[50:],color='blue')

plt.show()

