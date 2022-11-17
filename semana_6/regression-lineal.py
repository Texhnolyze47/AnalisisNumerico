import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0, 100, size=10)
y = np.random.randint(0, 100, size=10)
n = len(x)

b = sum(n * sum(x * y) - sum(x) * sum(y))/(n*sum(x**2) - sum(x) ** 2)
a = sum(y) / n - sum(x) / n * b

xx = np.arange( min(x) -0.5, max(x) + 0.5,0.001)
yy = a * b * xx
print(a,b)

plt.plot(x,y,'g*',xx,yy,'r:')

