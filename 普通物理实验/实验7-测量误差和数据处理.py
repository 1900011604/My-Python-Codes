from matplotlib import pyplot as plt
import numpy as np


x = [0.535, 0.988, 1.424, 1.787, 2.169, 2.552, 2.932]
y = [i for i in range(10, 45, 5)]

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='g', marker='+')
x1 = np.arange(0, 3.001, 0.001)
plt.plot(x1, 12.63671005*x1+2.638438938, color='r')

plt.xlim((0, 3.5))
plt.ylim((0, 50))
xaxis = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]
yaxis = [i for i in range(0, 55, 5)]
plt.xticks(xaxis)
plt.yticks(yaxis)
plt.show()
