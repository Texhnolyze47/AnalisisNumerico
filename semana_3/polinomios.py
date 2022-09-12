import numpy as np
import sympy as sp

x = sp.Symbol("x")

y = x ** 3 - 64
x0 = 1
x1 = 5
xr = 20

while(y.subs(x,xr) > 1e-15 ):
    xr = x1 - y.subs(x, x1) * (x1 - x0) / (y.subs(x, x1) - y.subs(x, x0))
    if y.subs(x, x1)* y.subs(x, xr) < 0:
        x0 = xr
    else:
        x1 = xr

print("La raiz del polinomio ", y , "es", xr)