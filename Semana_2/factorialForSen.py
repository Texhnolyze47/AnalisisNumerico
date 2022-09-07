import numpy as np
from math import *
x = np.pi/3
# Expresiones
y = cos(x)
yy = sin(x)
print('VaIor real coseno' , y)
print('VaIor real seno' , yy)
y1=0
y2 = 0
# El valor del range es la cantidad de veces para acercarse al valor
# real
for i in range(20):
    y1=y1+x**(2*i)/factorial(2*i)*(-1)**i
    y2=y2+x**(2*i+1)/factorial(2*i+1)*(-1)**i

    print("VaIor aproximado cos", y1)
    print("VaIor aproximado sen ", y2)

    e=abs(y-y1)
    ep =abs((y-y1)/y)

    print("Error absoluto para coseno" , e, "Error porcentual para conseno" , ep, "\n")

    e = abs(yy - y2)
    ep = abs((yy - y2) / yy)

    print("Error absoluto para seno", e, "Error porcentual para seno", ep, "\n")