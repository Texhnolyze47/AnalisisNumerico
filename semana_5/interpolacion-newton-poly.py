import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# for graph comparison purposes

def divided_difference(x, y):
    # length/number of datapoints
    n = len(x)
    # divided difference initialization
    fdd = [[None for x in range(n)] for x in range(n)]

    # finding divided difference
    for i in range(n):
        fdd[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (x[i + j] - x[i])

    return fdd


# polynomial at len(datapoints) order
def newton_polynomial(fdd, xi):
    n = len(fdd)
    # f(X) values at different degrees
    yint = [None for x in range(n)]
    # error value
    ea = [None for x in range(n)]

    # interpolating xi
    xterm = 1
    yint[0] = fdd[0][0]
    for order in range(1, n):
        xterm = xterm * (xi - yint[order - 1])
        yint2 = yint[order - 1] + fdd[0][order] * xterm
        ea[order - 1] = yint2 - yint[order - 1]
        yint[order] = yint2

    return yint


x = [1, 4, 6, 5, 3, 1.5, 2.5, 3.5]
y = [0, 1.3862944, 1.7917595, 1.6094379, 1.0986123, 0.4054641, 0.9162907, 1.2527630]
xi = 2
dd = divided_difference(x, y)
df = pd.DataFrame(dd)

# newton polynomial interpolation at varying orders
xxxx = np.linspace(1, 8, 200)
yyyy = []
for i in xxxx:
    yyyy.append(newton_polynomial(dd, 0))

yyyy.append(newton_polynomial(dd))
plt.plot(xxxx, yyyy)

# actual function
xo = np.linspace(1, 8, 200)
plt.plot(xo, np.log(xo), label="f(x)=lnx", color="black")

# datapoints scatter plot
plt.scatter(x, y)

plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.show()