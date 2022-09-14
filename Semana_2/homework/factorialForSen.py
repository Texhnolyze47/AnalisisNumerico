import numpy as np
from math import *

x = np.pi / 3
# Expresiones
yy = sin(x)
print('VaIor real seno', yy)
y2 = 0
# El valor del range es la cantidad de veces para acercarse al valor
# real
for i in range(13):
    y2 = y2 + x ** (2 * i + 1) / factorial(2 * i + 1) * (-1) ** i

    print("VaIor aproximado sen ", y2)

    e = abs(yy - y2)
    ep = abs((yy - y2) / yy)

    print("Error absoluto para seno", e, "Error porcentual para seno", ep, "\n")
