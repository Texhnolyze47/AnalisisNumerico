import numpy as np
import matplotlib.pyplot as plt


x = np.random.randint(0, 100, size=10)
y = np.random.randint(0, 100, size=10)
n = len(x)

x = sorted(x)
for i in range(int(n/2)):
    b0 = y[2*i]
    b1 = (y[2*i+1]-y[2*i]) / (x[2*i+1]-x[2*i])
    b2 = ((y[2*i+2]-y[2*i+1]) / (x[2*i+2]-x[2*i+1]) - b1) / (x[2*i+2]-x[2*i])
    xx = np.arange(x[2*i], x[2*i+2] + 0.001, 0.001)
    yy =b0 + b1 * (xx-x[2*i])+b2*(xx-x[2*i])*(xx-x[2*i+1])
    plt.plot(x,y,"r*",xx,yy,"b:")
plt.show()