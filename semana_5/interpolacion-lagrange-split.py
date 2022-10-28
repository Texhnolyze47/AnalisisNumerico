import numpy as np
import matplotlib.pyplot as plt


x = np.random.randint(0,100, size=10)
y = np.random.randint(0,100, size=10)

n = len(x)
h = 0.001
plt.plot(x,y,"b*")
for i in range(1,n):
    xx = np.arange(x[i-1],x[i]+h,h)
    yy = (xx-x[i]) / (x[i-1]-x[i]) * y[i-1] + (xx-x[i-1]) / (x[i]-x[i-1]) * y[i]
plt.show()