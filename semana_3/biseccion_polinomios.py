import sympy as sp

x = sp.Symbol("x")
# expresion a evualuar
y =  4 * x ** 4 - 9 * x ** 2 + 1

# y = input("Ingrese el polimonio a resolver")
# y = sp.simplify(y)

s = 0
while s == 0:
    x0 = float(input("Proporcione un valor inicial"))
    x1 = float(input("Proporcione un valor final"))
    # esta condicional evaluar si la raiz esta dentro del intervalo
    if y.subs(x, x0) * y.subs(x, x1) < 0:
        s = 1
    # si no se cumple proponer otro intervalo
    else:
        print("Los valores proporcionados son incorrentos")

xr = 0
er = 5
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
print("La raiz del polinomio ", y, "es", xr, " con ", i, "interaciones")
print("Con un error del " , er)
