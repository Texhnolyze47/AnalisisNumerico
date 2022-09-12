import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot
import sympy as sp
import math as mt

x = np.arange(-4, 4, 0.1)
y = np.arange(-4, 4, 0.1)

# convierte la info
X, Y = np.meshgrid(x,y)

z = (np.cos(X)-np.sin(Y)+5)
# proyeccion en 3 dimensiones
ax = plt.axes(projection="3d")
# se grafica como una superficie
ax.plot_surface(x,y,z, cmap="hot")
plt.show()

