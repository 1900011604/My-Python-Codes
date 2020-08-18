# -*- coding: utf-8 -*-

#[H2.2]做计时实验，验证dict的get item和set item都是O(1)的

#[H2.2.1]做计时实验，验证dict的get item是O(1)的

import numpy as np
import matplotlib.pyplot as plt
from timeit import Timer

#计时实验程序
def test21():
    return d[n-1]
t21=Timer("test21()","from __main__ import test21")
x_list21 = []
y_list21 = []
for n in range(10000,2510000,10000): #250个数据点
    d=dict(list((j,j) for j in range(n)))
    x_list21.append(n) 
    y_list21.append(t21.timeit(number=1000000))
  
#线性拟合数据点 
def linefit(x, y):
    N = len(x)
    sx,sy,sxx,syy,sxy=0,0,0,0,0
    for i in range(0,N):
        sx  += x[i]
        sy  += y[i]
        sxx += x[i]*x[i]
        syy += y[i]*y[i]
        sxy += x[i]*y[i]
    k = (sy*sx/N-sxy)/(sx*sx/N-sxx)
    b = (sy-k*sx)/N
    R = (sxy-sx*sy/N)/((sxx-sx*sx/N)*(syy-sy*sy/N))**0.5 
    return [k,b,R]
for i in range(len(x_list21)):
    x_list21[i]/=1000000
r=linefit(x_list21,y_list21)
print('k='+str(r[0]))
print('b='+str(r[1]))
print('r='+str(r[2]))
print('\nt=%.2fn+%.2f\n'%(r[0], r[1]))
#拟合结果（斜率k，截距b，相关系数r）	
		
#绘图
xmax21 = x_list21[-1]
#x轴的上界
dx21 = x_list21[-1] / 5 
#x轴的单位长度
ymax21 = float("{0:.2f}".format(max(y_list21)))  
#y轴的上界
dy21 = ymax21 / 5 
#y轴的单位长度
x21 = np.arange(0, xmax21 + 0.5*dx21, 0.01) #绘直线用
plt.figure(figsize=(16, 10))
plt.scatter(x_list21, y_list21, color='g', marker='+')
plt.plot(x21, r[0]*x21+r[1] , color='r')
plt.title('H2.2.1', fontsize=24)
plt.xlabel("n(*10^6)", fontsize=16)
plt.ylabel("time(s)", fontsize=16)
plt.xlim((0, xmax21 + dx21))
plt.ylim((0, ymax21 + dy21))
xaxis = np.arange(0, xmax21 + dx21, dx21)
yaxis = np.arange(0, 2 * ymax21 + 4 * dy21, dy21)
#使数据点落在图像的中央
plt.xticks(xaxis)
plt.yticks(yaxis)
plt.show()

