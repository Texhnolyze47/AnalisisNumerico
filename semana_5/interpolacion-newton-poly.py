import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def divided_difference(x, y):
    # cantidad de puntos de datos
    n = len(x)

    # inicialización una lista donde se
    # guardara la diferencia dividida
    dd = [[None for x in range(n)] for x in range(n)]

    # donde se encuentra la diferencia dividida
    for i in range(n):
        dd[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            dd[i][j] = (dd[i + 1][j - 1] - dd[i][j - 1]) / (x[i + j] - x[i])

    return dd


# polinomio en len(datapoints) orden
def newton_polynomial(fdd, xi):
    n = len(fdd)
    # valores de f(X) en diferentes grados
    yint = [None for x in range(n)]
    # valor del error
    ea = [None for x in range(n)]

    # interpolando xi
    xterm = 1
    yint[0] = fdd[0][0]
    for order in range(1, n):
        xterm = xterm * (xi - yint[order - 1])
        yint2 = yint[order - 1] + fdd[0][order] * xterm
        ea[order - 1] = yint2 - yint[order - 1]
        yint[order] = yint2

    return yint


x = [1, 4, 6, 5, 3, 1.5, 2.5, 3.5]
y = [0, 1.3862944, 1.7917595, 1.6094379, 1.0986123, 0.4054641, 0.9162907, 1.2527630]
xi = 2
dd = divided_difference(x, y)

# interpolación polinómica de newton en varios órdenes
xxxx = np.linspace(1, 8, 200)
yyyy = []
for i in xxxx:
    yyyy.append(newton_polynomial(dd, 0))

yyyy.append(newton_polynomial(dd))
plt.plot(xxxx, yyyy)

# función real
xo = np.linspace(1, 8, 200)
plt.plot(xo, np.log(xo), label="f(x)=lnx", color="black")

# gráfico de dispersión de puntos de datos
plt.scatter(x, y)

plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.show()