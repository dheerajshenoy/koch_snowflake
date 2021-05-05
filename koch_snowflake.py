from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import numpy as np

SQRT_3 = np.sqrt(3)

fig, ax = plt.subplots()
ax.set_xlim([-0.2, 1.2])
ax.set_ylim([-0.5, 1])
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
for i in ax.spines:
    ax.spines[i].set_visible(False)

def kochSnowflakeImpl(p1, p2):
    u = p2 - p1
    v = np.array([-u[1], u[0]])

    n1 = p1 + u * (1.0 / 3.0)
    n2 = n1 + u * (1.0 / 6.0) + v * (SQRT_3 / 6.0)
    n3 = p1 + u * (2.0 / 3.0)
    return [p1, n1, n2, n3, p2]

def kochSnowflake(level):
    p1 = np.array([0.0, 0.0])
    p2 = np.array([0.5, SQRT_3 / 2.0])
    p3 = np.array([1.0, 0.0])

    array = [p1, p2, p3, p1]

    for _ in range(level):
        new_array = []

        for (p1, p2) in zip(array, array[1:]):
            new_array.extend(kochSnowflakeImpl(p1, p2))

        array = new_array

    return array

xdata, ydata = [], []
ln, = plt.plot([], [], marker=".", ls="-")
points = kochSnowflake(4)
x, y = zip(*points)
plt.plot(x, y)
def animate(i):
    ln.set_data(x[i], y[i])
    plt.plot(x[i], y[i], '.b')

if __name__ == '__main__':
    anim = FuncAnimation(fig, animate, interval=0.01, repeat=False, frames=10)
    writer = animation.ImageMagickFileWriter()
    anim.save("dd.gif", writer=writer)
