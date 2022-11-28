import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from vrp import VRP,Delivery,Ride,Vehicle,Order

vrp = VRP(50)
vrp.vehicles = [
    Vehicle(1, 3, 12),
    Vehicle(2, 5, 22),
    Vehicle(3, 8, 36),
]
vrp.orders = [
    
]


fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

plt.show()
