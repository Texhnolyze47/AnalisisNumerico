import numpy as np
from math import *
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.001)

n = len(x)

# puntos de la grafica

y1 = np.zeros(n)
y2 = np.zeros(n)

c = ["r", "g", "b", "c", "m", "y", "k", "gold", "firebrick", "pink"]

# El valor del range es la cantidad de veces para acercarse al valor
# real
for i in range(10):
    y1 = y1 + x ** (2 * i) / factorial(2 * i) * (-1) ** i
    y2 = y2 + x ** (2 * i + 1) / factorial(2 * i + 1) * (-1) ** i

    plt.figure(1)
    plt.plot(x, y1, c[i])
    plt.figure(2)
    plt.plot(x, y2, c[i])

plt.show()
