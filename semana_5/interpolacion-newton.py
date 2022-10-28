import numpy as np
import matplotlib.pyplot as plt
#splits con newton orden tres

x = np.random.randint(0, 100, size=10)
y = np.random.randint(0, 100, size=10)
n = len(x)

x = sorted(x)
b0 = y[0]
b1 = (y[1]-y[0]) / (x[1]-x[0])
b2 = (y[2]-y[1]) / (x[2]-x[1]) - (y[1]-y[0]) / (x[1]-x[0]) / (x[2]-x[0])

xx = np.arange(x[0], x[n-1] + 0.001, 0.001)
yy =b0 + b1 * (xx-x[0])+b2*(xx-x[0])*(xx-x[1])
plt.plot(x,y,"r*",xx,yy,"b:")
plt.show()