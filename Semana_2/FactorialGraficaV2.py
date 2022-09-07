import numpy as np
from math import *
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.001)

n = len(x)

# puntos de la grafica
y = np.zeros(n)
yy = np.zeros(n)

for i in range(n):
    y[i] = cos(x[i])
    yy[i] = sin(x[i])

y1 = np.zeros(n)
y2 = np.zeros(n)

c = ["r", "g", "b", "c", "m", "y", "k", "gold", "firebrick", "forestgreen"]

# El valor del range es la cantidad de veces para acercarse al valor
# real
for i in range(10):
    y1 = y1 + x ** (2 * i) / factorial(2 * i) * (-1) ** i
    y2 = y2 + x ** (2 * i + 1) / factorial(2 * i + 1) * (-1) ** i

    plt.figure(1)
    plt.plot(x, y,"fuchsia",x,y1, c[i])
    plt.figure(2)
    plt.plot(x, yy,"fuchsia",x,y2, c[i])

    plt.show()


# se necesità la serie de potencias de la  tangetes7
# graficar la tangete
# se tiene que derivar
# la tangente en pi cuartos
# 5 elementos de la serie minino
# maclaurin
