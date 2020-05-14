# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:16:31 2020

@author: 1773296008
"""
#[H2.2.2]做计时实验，验证dict的set item是O(1)的
import numpy as np
import matplotlib.pyplot as plt
from timeit import Timer

#计时实验程序
def test22():
    d[n-1]=n
t22=Timer("test22()","from __main__ import test22")
x_list22 = []
y_list22 = []
for n in range(10000,110000,10000): #10个数据点
    d=dict(list((j,j) for j in range(n)))
    x_list22.append(n) 
    y_list22.append(t22.timeit(number=1000000))
    print(n//10000)

  
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
for i in range(len(x_list22)):
    x_list22[i]/=1000000
r=linefit(x_list22,y_list22)
print('k='+str(r[0]))
print('b='+str(r[1]))
print('r='+str(r[2]))
print('\nt=%.2fn+%.2f\n'%(r[0], r[1]))
#拟合结果（斜率k，截距b，相关系数r）	
		
#绘图
xmax22 = x_list22[-1] 
#x轴的上界
dx22 = x_list22[-1] / 5 
#x轴的单位长度
ymax22 = float("{0:.2f}".format(max(y_list22)))  
#y轴的上界
dy22 = ymax22 / 5 
#y轴的单位长度
x22 = np.arange(0, xmax22 + 0.5*dx22, 0.01) #绘直线用
plt.figure(figsize=(16, 10))
plt.scatter(x_list22, y_list22, color='g', marker='+')
plt.plot(x22, r[0]*x22+r[1] , color='r')
plt.title('H2.2.2', fontsize=24)
plt.xlabel("n(*10^6)", fontsize=16)
plt.ylabel("time(s)", fontsize=16)
plt.xlim((0, xmax22 + dx22))
plt.ylim((0, ymax22 + dy22))
xaxis = np.arange(0, xmax22 + dx22, dx22)
yaxis = np.arange(0, 2 * ymax22 + 4 * dy22, dy22)
#使数据点落在图像的中央
plt.xticks(xaxis)
plt.yticks(yaxis)
plt.show()