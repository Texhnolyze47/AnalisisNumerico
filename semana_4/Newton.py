import sympy as sp

x = sp.Symbol("x")
#Funcion a evaluar
y = x ** 3 - 27
# nuestro valor de arranque
x1 = 1

y = sp.simplify(y)
# derivada
dy = y.diff(x)

# valor de la raiz
xr = 0
# iterador
i = 0

while(y.subs(x,xr) != 0):
    xr = float(x1 - y.subs(x,x1)/ dy.subs(x,x1)) # formula del metodo
    x1 = xr
    er = abs( y.subs(x,x1))
    i+=1
print("La raiz del polinomio" , y, "es" , xr, "se consiguio en ", i)
print("Con un error del ", er)