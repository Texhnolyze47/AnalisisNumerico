import numpy as np
import matplotlib.pyplot as plt

# splits de orden 2 y 3

x = np.random.randint(0, 100, size=9)
n = len(x)
y = np.random.randint(0, 100, size=9)
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
