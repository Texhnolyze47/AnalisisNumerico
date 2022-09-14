import numpy as np
from math import *

x = np.pi / 3
# variable del valor real
y = cos(x)
print(x)
print('VaIor real', y)

y1 = 0
# El valor del range es la cantidad de veces va intentar acercarse al valor real
for i in range(10):
    # formula
    y1 = y1 + x ** (2 * i) / factorial(2 * i) * (-1) ** i
    # se imprime el valor aproximado
    print("VaIor aproximado", y1)

    # error absoluto
    e = abs(y - y1)
    # error porcentual
    ep = abs((y - y1) / y)

    print("Error absoluto", e, "Error porcentual", ep, "\n")
