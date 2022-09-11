import numpy as np
from math import *
x = np.pi/3
y = cos(x)
print('VaIor real' , y)

y1=0
# El valor del range es la cantidad de veces para acercarse al valor
# real
for i in range(10):
    y1=y1+x**(2*i)/factorial(2*i)*(-1)**i
    print("VaIor aproximado", y1)
    e=abs(y-y1)
    ep =abs((y-y1)/y)

    print("Error absoluto" , e, "Error porcentual" , ep, "\n")