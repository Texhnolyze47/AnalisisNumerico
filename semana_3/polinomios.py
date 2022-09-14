import numpy as np
import sympy as sp

x = sp.Symbol("x")

y = x ** 3 - 125
x0 = 1
x1 = 20
xr = 0
er = 1
# contador para saber que nivel de aproximacion puede
i = 0

while er > 1e-15:
    xr = float(x1 - y.subs(x, x1) * (x1 - x0) / (y.subs(x, x1) - y.subs(x, x0)))
    if y.subs(x, x1) * y.subs(x, xr) < 0:
        xr0 = x0
        x0 = xr

    else:
        xr0 = x1
        x1 = xr
    # La variable que mide el error
    er = float(abs((y.subs(x, xr) - y.subs(x, xr0)) / y.subs(x, xr)))
    i += 1
print("La raiz del polinomio ", y, "es", xr, " ", i)
