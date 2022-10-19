import numpy as np
import matplotlib.pyplot as plt


x = np.array([1,4])
y = np.array([-3,5])
n = len(x)
h = 0.001
xx = np.arange(x[0],x[1]+h,h)
yy = (xx-x[1]) / (x[0]-x[1]) * y[0] + (xx-x[0]) / (x[1]-x[0]) * y[1]
plt.plot(xx,yy,"r",x,y,"b*")
plt.show()