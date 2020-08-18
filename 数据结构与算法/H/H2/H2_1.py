# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:16:27 2020

@author: 1773296008
"""
#[H2.1]做计时实验，验证list的按索引取值确实是O(1)
import numpy as np
import matplotlib.pyplot as plt
from timeit import Timer
		
#计时实验程序
def test1():
	return l[n-1]  #list按索引取值函数
t1=Timer("test1()","from __main__ import test1")
x_list1 = []
y_list1 = []
for n in range(10000,2510000,10000):  #250个数据点
	l=list(range(n))
	x_list1.append(n) 
	y_list1.append(t1.timeit(number=1000000))
		
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
for i in range(len(x_list1)):
    x_list1[i]/=1000000  
r=linefit(x_list1,y_list1)
print('k='+str(r[0]))
print('b='+str(r[1]))
print('r='+str(r[2]))
print('\nt=%.2fn+%.2f\n'%(r[0], r[1]))
#拟合结果（斜率k，截距b，相关系数r）		
	
#绘图 
xmax1 = x_list1[-1]
#x轴的上界
dx1 = x_list1[-1] / 5 
#x轴的单位长度
ymax1 = float("{0:.2f}".format(max(y_list1)))  
#y轴的上界
dy1 = ymax1 / 5 
#y轴的单位长度
x1 = np.arange(0, xmax1 + 0.5*dx1, 0.01)  #绘直线用
plt.figure(figsize=(16, 10))
plt.scatter(x_list1, y_list1, color='g', marker='+')
plt.plot(x1, r[0]*x1+r[1] , color='r')
plt.title('H2.1', fontsize=24)
plt.xlabel("n(*10^6)", fontsize=16)
plt.ylabel("time(s)", fontsize=16)
plt.xlim((0, xmax1 + dx1))
plt.ylim((0, ymax1 + dy1))
xaxis = np.arange(0, xmax1 + dx1, dx1)
yaxis = np.arange(0, 2 * ymax1 + 4 * dy1, dy1)
#使数据点落在图像的中央
plt.xticks(xaxis)
plt.yticks(yaxis)
plt.show()

