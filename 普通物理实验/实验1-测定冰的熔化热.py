from matplotlib import pyplot as plt
import numpy as np


t1 = [i for i in range(0, 100, 10)]
T1 = [36.5, 36.5, 36.4, 36.4, 36.4, 36.4, 36.4, 36.3, 36.3, 36.3]

plt.figure(figsize=(8, 5))
plt.scatter(t1, T1, color='g', marker='+')
x1 = np.arange(0, 160.01, 0.01)
plt.plot(x1, -2.242424242424242424*0.001*x1+36.49090909090909091, color='r')
plt.scatter(141, 36.174727272727272727, color='b', marker='+')
plt.text(130, 36.1, (141, 36.175), color='b')
plt.xlabel("$t$/s", fontsize=16)
plt.ylabel("$T$/℃", fontsize=16)
plt.xlim((0, 160))
plt.ylim((36, 37.1))
xaxis = [i for i in range(0, 170, 10)]
yaxis = [0.1*i for i in range(360, 371, 1)]
plt.xticks(xaxis)
plt.yticks(yaxis)
plt.show()


x2 = np.arange(0, 280.01, 0.01)
t2 = sorted(t1 + [150, 160, 170, 175, 180, 185, 190, 195, 200,
                  205, 210, 215, 220, 225, 230, 235, 240, 250, 260, 270, 280])
T2 = T1 + [34.1, 34.1, 29.6, 28, 26.1, 24.8, 24.1, 23.7, 22.6,
           21.7, 21, 20.4, 20, 19.5, 19, 18.7, 18.4, 18, 17.9, 17.9, 17.9]

plt.figure(figsize=(8, 5))
plt.scatter(t2, T2, color='g', marker='+')
plt.scatter(141, 36.174727272727272727, color='b', marker='+')
t2 = sorted(t2+[141])
T2 = T1 + [36.174727272727272727, 34.1, 34.1, 29.6, 28, 26.1, 24.8, 24.1,
           23.7, 22.6, 21.7, 21, 20.4, 20, 19.5, 19, 18.7, 18.4, 18, 17.9, 17.9, 17.9]

plt.plot(t2, T2, color='r')
plt.plot(x2, x2-x2+27, color='#ffA500')
plt.text(225, 27.25, r'$\theta=$27.0℃', color='#ffA500')
plt.xlabel("$t$/s", fontsize=16)
plt.ylabel("$T$/℃", fontsize=16)
plt.show()
