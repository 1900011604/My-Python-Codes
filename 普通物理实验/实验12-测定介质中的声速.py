import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


data = [45.890 , 55.060 , 64.220 , 73.310 , 82.410 , 91.470 , 100.590 , 109.730 , 118.740 , 127.860] 
i = [j for j in range(1,11)]

Sum = 0
E = []
for j in i:
    y = 9.102666667 * j + 36.86333333
    e = data[j-1] - y
    Sum += e**2
    E.append(e)
print('sum = '+str(Sum))
print(E)

sigma = (Sum / 8) ** 0.5
print('sigma = '+str(sigma))


U1 = [804 , 764 , 736 , 684 , 636 , 580 , 544 , 500 , 460 , 432]
x1 = [46.290 , 50.900 , 55.470 , 60.000 , 64.630 , 69.190 , 73.760 , 78.310 , 82.870 , 87.420]

U2 = [804 , 764 , 740 , 688 , 636 , 584 , 544 , 500 , 460 , 440]
x2 = [46.090 , 50.690 , 55.230 , 59.770 , 64.390 , 68.920 , 73.510 , 78.060 , 82.630 , 87.300]

f1 = interp1d(x1, U1, kind='cubic')
f2 = interp1d(x2, U2, kind='cubic')

x_linspace1 = np.linspace(46.290, 87.420, num=4500, endpoint=True)
x_linspace2 = np.linspace(46.090, 87.300, num=4500, endpoint=True)

plt.figure(figsize=(16, 10))
plt.xlim(45, 90)
plt.ylim(400, 900)
my_x_ticks = np.arange(45,95,5)
my_y_ticks = np.arange(400,1000,100)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.scatter(x1, U1, marker='+', color='r')
plt.plot(x_linspace1, f1(x_linspace1),linestyle='--', color='g')
plt.plot(x_linspace1, 1725.542793*np.e**(-0.01575677*x_linspace1),linestyle='-', color='b')
plt.show()

plt.figure(figsize=(16, 10))
plt.xlim(45, 90)
plt.ylim(400, 900)
my_x_ticks = np.arange(45,95,5)
my_y_ticks = np.arange(400,1000,100)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.scatter(x2, U2, marker='+', color='r')
plt.plot(x_linspace2, f2(x_linspace2),linestyle='--', color='g')
plt.plot(x_linspace2, 1700.611326*np.e**(-0.015545037*x_linspace2),linestyle='-', color='b')
plt.show()