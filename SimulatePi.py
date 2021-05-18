import numpy as np 
import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


angle = np.linspace( 0 , 2 * np.pi , 150) 
radius = 1
x = radius * np.cos(angle) 
y = radius * np.sin(angle) 
#prints the circle

style.use('fivethirtyeight')
fig = plt.figure()
axes = fig.add_subplot(1,1,1)
axes.plot( x, y, color="red") 

inside = []
outside = []

def inCircle(x, y):
    return math.sqrt( (x**2) + (y**2) ) =< 1

def animate(i):
    x = random.uniform(1,-1)
    y = random.uniform(1,-1)
    if (inCircle(x, y)):
        point = axes.scatter(x, y, color="blue")
        inside.append(point)
    else:
        point = axes.scatter(x, y, color="red")
        outside.append(point)
    try:
        ratio = len(inside) / len(outside)
        print(ratio)
    except ZeroDivisionError:
        print(0)


ani = animation.FuncAnimation(fig, animate, interval=5)
plt.show()
