import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# configurar la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# crear los datos de la figura 3D
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

# dibujar el objeto inicial
line, = ax.plot(x, y, z)

# función de animación para rotar el objeto
def animate(i):
    ax.view_init(elev=10., azim=i)
    return line,

# crear la animación
ani = animation.FuncAnimation(fig, animate, frames=360, interval=50, blit=True)

# guardar la animación como gif
ani.save('rotating_object.gif', writer='imagemagick')
