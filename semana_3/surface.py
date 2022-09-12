import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot
import sympy as sp
import math as mt

x = np.arange(-2, 2, 0.001)
y = np.arange(-2, 2, 0.001)

# convierte la info
x, y = np.meshgrid(x,y)

z = (3*x-2*y+5)
# proyeccion en 3 dimensiones
ax = plt.axes(projection="3d")
# se grafica como una superficie
ax.plot_surface(x,y,z, cmap="hot")
plt.show()


