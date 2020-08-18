# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:16:32 2020

@author: 1773296008
"""
#[H2.3]做计时实验，比较list和dict的del操作符性能

#H2.3.2 dict中del操作符的性能

import numpy as np
import matplotlib.pyplot as plt
from timeit import Timer

#计时实验程序
def test320():
    for i in range(100000):
        d[n+i] = 0  #插入100000个键值对所需时间
t320=Timer("test320()","from __main__ import test320")        
def test321():
    del d[0]
    d[0] = 0
t321=Timer("test321()","from __main__ import test321")
def test322():
    del d[a2]
    d[a2] = 0
t322=Timer("test322()","from __main__ import test322")
def test323():
    del d[a3]
    d[a3] = 0
t323=Timer("test323()","from __main__ import test323")
def test324():
    del d[a4]
    d[a4] = 0
t324=Timer("test324()","from __main__ import test324")
def test325():
    del d[a5]
    d[a5] = 0
t325=Timer("test325()","from __main__ import test325")
x_list32=[]
y_list321, y_list322 = [], []
y_list323, y_list324, y_list325 = [], [], []
for n in range(10000,2510000,10000): #250个数据点
    a2=int(n/4)
    a3=int(n/2)
    a4=int(3*n/4)
    a5=n-1
    d=dict(list((j,j) for j in range(n)))
    x_list32.append(n) 
    y_list321.append(t321.timeit(number=100000)-t320.timeit(number=1))
    y_list322.append(t322.timeit(number=100000)-t320.timeit(number=1))
    y_list323.append(t323.timeit(number=100000)-t320.timeit(number=1))
    y_list324.append(t324.timeit(number=100000)-t320.timeit(number=1))
    y_list325.append(t325.timeit(number=100000)-t320.timeit(number=1))
 
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
for i in range(len(x_list32)):
    x_list32[i]/=1000000
r1=linefit(x_list32,y_list321)
print('k1='+str(r1[0]))
print('b1='+str(r1[1]))
print('r1='+str(r1[2]))
print('\nt1=%.2fn+%.2f\n'%(r1[0], r1[1]))
#拟合结果（斜率k，截距b，相关系数r）
r2=linefit(x_list32,y_list322)	
print('k2='+str(r2[0]))
print('b2='+str(r2[1]))
print('r2='+str(r2[2]))
print('\nt2=%.2fn+%.2f\n'%(r2[0], r2[1]))
#拟合结果（斜率k，截距b，相关系数r）
r3=linefit(x_list32,y_list323)
print('k3='+str(r3[0]))
print('b3='+str(r3[1]))
print('r3='+str(r3[2]))
print('\nt3=%.2fn+%.2f\n'%(r3[0], r3[1]))
#拟合结果（斜率k，截距b，相关系数r）
r4=linefit(x_list32,y_list324)
print('k4='+str(r4[0]))
print('b4='+str(r4[1]))
print('r4='+str(r4[2]))
print('\nt4=%.2fn+%.2f\n'%(r4[0], r4[1]))
#拟合结果（斜率k，截距b，相关系数r）
r5=linefit(x_list32,y_list325)
print('k5='+str(r5[0]))
print('b5='+str(r5[1]))
print('r5='+str(r5[2]))
print('\nt5=%.2fn+%.2f\n'%(r5[0], r5[1]))
#拟合结果（斜率k，截距b，相关系数r）
		
#绘图
xmax31 = x_list32[-1] 
#x轴的上界
dx31 = (x_list32[-1])/5 
#x轴的单位长度
ymax31 = float("{0:.2f}".format(max(y_list321)))  
#y轴的上界
dy31 = ymax31 / 5 
#y轴的单位长度
x31 = np.arange(0, xmax31+0.5*dx31, 0.01) #绘直线用
plt.figure(figsize=(16, 10))
plt.scatter(x_list32, y_list321, color='g', marker='+')
plt.plot(x31, r1[0]*x31+r1[1] , color='r')  #红色
plt.scatter(x_list32, y_list322, color='g', marker='+')
plt.plot(x31, r2[0]*x31+r2[1] , color='b')  #蓝色
plt.scatter(x_list32, y_list323, color='g', marker='+')
plt.plot(x31, r3[0]*x31+r3[1] , color='#924900')  #咖啡色
plt.scatter(x_list32, y_list324, color='g', marker='+')
plt.plot(x31, r4[0]*x31+r4[1] , color='#FF7700')  #橙色
plt.scatter(x_list32, y_list325, color='g', marker='+')
plt.plot(x31, r5[0]*x31+r5[1] , color='m')  #品红
plt.title('H2.3.2', fontsize=24)
plt.xlabel("n(*10^6)", fontsize=16)
plt.ylabel("time(s)", fontsize=16)
plt.xlim((0, xmax31 + dx31))
plt.ylim((0, ymax31 + dy31))
xaxis = np.arange(0, xmax31 + dx31, dx31)
yaxis = np.arange(0, 2 * ymax31 + 4 * dy31, dy31)
#使数据点落在图像的中央
plt.xticks(xaxis)
plt.yticks(yaxis)
plt.show()
