import numpy as np
import matplotlib.pyplot as plt

# splits de orden 2 y 3

#x = np.random.randint(0, 100, size=9)
#y = np.random.randint(0, 100, size=9)
x = np.array([1910, 1921, 1930, 1940,1950,1960,1970,1980,1990,1995,2000,2005,2010,2015,2020])
y = np.array([15150, 14334, 16552, 19552,19653,25791,34923,48225,66846,81249,91158,97483,103262,112336,126814])
n = len(x)

max = y.max()

x = sorted(x)
h = 0.001
plt.figure(2)
plt.plot(x, y, "b*")
xx = np.arange(x[0], x[n - 1] + h, h)
yy = 0
for i in range(n):
    m = 1
    for j in range(n):
        if i != j:
            m = (xx - x[j]) / (x[i] - x[j]) * m
    yy = m * y[i] + yy
plt.plot(xx, yy, "r")
plt.show()
