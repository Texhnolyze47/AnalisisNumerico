import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 5, 7, 11])
y = np.array([-2, 4, -5, 7])
n = len(x)

x = np.random.randint(0, 100, size=10)
y = np.random.randint(0, 100, size=10)
x = sorted(x)

for i in range(1, n):
    m = (y[i] - y[i - 1]) / (x[i] - x[i - 1])

    b = y[i] - m * x[i]

    xx = np.arange(x[i - 1], x[i] + 0.001, 0.001)
    yy = m * xx + b
    plt.plot(x, y, "r*", xx, yy, "b:")

plt.show()
