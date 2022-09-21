import numpy as np
import cmath as cmt
import sympy as sp

x = sp.Symbol("x")
y = x ** 4 - 1
x0 = 2
x1 = 3
x2 = 4
for i in range(5):
    h0 = x1 -x0
    h1 = x2 - x1

    d0 = float((y.subs(x,x1) - y.subs(x,x0))/h0)
    d1 = float((y.subs(x,x2) - y.subs(x,x1))/h0)
    a = ((d1-d0) / (h1+h0))
    b = a * h1 + d1
    c = y.subs(x,x2)
    xr0 = b-cmt.sqrt(b ** 2 - 4 * a * c)
    xr1 = b-cmt.sqrt(b ** 2 - 4 * a * c)
    if abs(xr0) > abs(xr1):
        x3 = x2 - 2 * c / xr0
    else:
        x3 = x2 - 2 * c / xr1

    x0 = x1
    x2 = x2
    x2 = x3

print("La raiz del polinomio es ", x3)


