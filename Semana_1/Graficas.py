import numpy as np
import matplotlib.pyplot as plt
# Se pueden usar literales
from sympy import *
#
x = Symbol("x")

y = x ** 2

xx = np.arange(-2,2,.1)

n = len(xx)
# genera valores de arreglos con zeros
yy = np.zeros(n)
# la funcion subs evalua una sola variable
# en caso de dos se usa evaluaf
for i in range(n):
    yy[i] = y.subs(x,xx[i])
#
plt.plot(xx,yy)
plt.show()




