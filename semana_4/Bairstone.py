import numpy as np
import sympy as cm
from numpy.linalg import inv

# a = np.array([1,-3,2.75,2.125,3.875,1.2])
r = s = -1
a = np.array([1.25, -3.875, 2.125, 2.75, -3.5, 1])
n = int(len(a))
er = 1
es = 1
while n > 3:
    while er > 0.00006 and es > 0.00004:
        # calculol de b
        b = np.zeros(n)
        b[n - 1] = a[n - 1]
        b[n - 2] = a[n - 2] + r * b[n - 1]

        for i in range(n - 3, -1, -1):
            b[i] = a[i] + r * b[i + 1] + s * b[i + 2]

        # print(b)
        # calculo de c
        c = np.zeros(n)
        c[n - 1] = b[n - 1]
        c[n - 2] = b[n - 2] + r * c[n - 1]
        for i in range(n - 3, 0, -1):
            c[i] = b[i] + r * c[i + 1] + s * c[i + 2]
        # print(c)
        # calculo del sistema
        d = np.matrix([[c[2], c[3]], [c[1], c[2]]])
        d1 = inv(d) * np.matrix([[-b[1]], [-b[0]]])
        # print(d1)
        r = r + d1[0, 0]
        s = s + d1[1, 0]

        er = abs(d1[0, 0] / r)
        es = abs(d1[1, 0] / r)
            # print(er,es)

        # print(r,s)
    x1 = (r + cm.sqrt(r ** 2 + 4 * s)) / 2
    x2 = (r - cm.sqrt(r ** 2 + 4 * s)) / 2

    print("\n", x1, x2)
    # polinomio incial modificado
    a1 = a[::-1]
    # print("\n",a1)
    d1 = np.array([1, -r, -s])
    p1, r1 = np.polydiv(a1, d1)
    # print(p1)
    er = 1
    es = 1
    a = p1[::-1]
    n = len(a)
    r = -0.5
    s = 0.5

print("\n", p1)
# calcular el en caso de sea de orden 1 o orden 2