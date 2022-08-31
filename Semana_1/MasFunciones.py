import numpy as np
import matplotlib.pyplot as plt
# Se pueden usar literales
from sympy import *
# Convierte en una literal
x = Symbol("x")
# Se eleva al cuadrado para graficar
y = x ** 2
# Las expresiones que se van a evaluar
y1 = exp(-x)
y2 = (x + 5) / (x ** 2 + 3)
y3 = cos(x)
# el rango y los intervalos
xx = np.arange(-2, 2, .1)

n = len(xx)
# genera valores de arreglos con zeros
yy = np.zeros((4, n))
# la funcion subs evalua una sola variable
# en caso de dos se usa evaluaf
for i in range(n):
    yy[0, i] = y.subs(x, xx[i])
plt.subplot(2, 2, 1)
plt.plot(xx, yy[0, :], "g")
for i in range(n):
    yy[1, i] = y1.subs(x, xx[i])
plt.subplot(2, 2, 2)
plt.plot(xx, yy[1, :], "r")
for i in range(n):
    yy[2, i] = y2.subs(x, xx[i])
plt.subplot(2, 2, 3)
plt.plot(xx, yy[2, :], "b")
for i in range(n):
    yy[3, i] = y3.subs(x, xx[i])
plt.subplot(2, 2, 4)
plt.plot(xx, yy[3, :, ], "m")
plt.show()
