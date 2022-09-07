import numpy as np
from math import *
x = np. pi/3
y = cos (x)
print('VaIor real' , y)
y1=x**2/(2)+(2)+x**4/factorial(4)-x**6/factorial(6)
print('VaIor aproximado' , y1)

e=abs(y-y1)
ep = ((y-y1)/y)

print("Error absoluto" , e, "Error porcentual" , ep)