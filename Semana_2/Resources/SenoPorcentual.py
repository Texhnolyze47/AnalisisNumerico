
import numpy as np
import math as mt

x = np.pi/3

y = mt.sin(x)

print("Valor real ", y)

y1 =  1 - x**2 /(2)

print("Valor aproximado ", y1)


e = (y - y1)

ep = abs((y-y1) / y)

# En caso de que no se sepa el valor real, el valor por el cual nos debemos decantar el error porcental

print("Error absoluto " , e , "Error porcentual", ep )