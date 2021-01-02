import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

t = [15*i for i in range(0,7)]
t_ = [0,16,28,42,58,74,88]
t_array = np.arange(0,90,0.0001)

plt.figure(figsize=(16, 10),dpi=200)
plt.xlim(-15, 105)
plt.ylim(-15, 105)
my_x_ticks = np.arange(0, 105, 15)
my_y_ticks = np.arange(0, 105, 15)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.scatter(t, t_, marker='+', color='r')
plt.plot(t_array, 0.9761904762*t_array-0.214285714, color='g')
plt.show() 
