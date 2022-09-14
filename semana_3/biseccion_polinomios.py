import sympy as sp

x = sp.Symbol("x")

y = x ** 3 - 125

y = input("Ingrese el polimonio a resolver")
y = sp.simplify(y)
s = 0
while s == 0:
    x0 = float(input("Proporcione un valor inicial"))
    x1 = float(input("Proporcione un valor final"))
    if y.subs(x, x0) * y.subs(x, x1) < 0:
        s = 1
    else:
        print("Los valores proporcionados son incorrentos")

# x0 = 6
# x1 = 20
xr = 0
er = 1
# contador para saber que nivel de aproximacion puede
i = 0

while er > 1e-15:
    xr = (x0 + x1) / 2
    if y.subs(x, x1) * y.subs(x, xr) < 0:
        xr0 = x0
        x0 = xr
    else:
        xr0 = x1
        x1 = xr
    # Esto evita que el programa divida entre 0
    if y.subs(x, xr) == 0:
        er = 0
    else:
        er = float(abs((y.subs(x, xr) - y.subs(x, xr0)) / y.subs(x, xr)))
    # La variable que mide el error
    i += 1
print("La raiz del polinomio ", y, "es", xr, " ", i)
