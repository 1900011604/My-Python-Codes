# -*- coding: utf-8 -*-

#[H2.3]做计时实验，比较list和dict中del操作符的性能

#H2.3.1 list中del操作符的性能

import numpy as np
import matplotlib.pyplot as plt
from timeit import Timer

#计时实验程序
def test311():
    del l[0]
t311=Timer("test311()","from __main__ import test311")
def test312():
    del l[int(n/4)]
t312=Timer("test312()","from __main__ import test312")
def test313():
    del l[int(n/2)]
t313=Timer("test313()","from __main__ import test313")
def test314():
    del l[int(3*n/4)]
t314=Timer("test314()","from __main__ import test314")
def test315():
    del l[-1]
t315=Timer("test315()","from __main__ import test315")
x_list31 = []
y_list311, y_list312 = [], []
y_list313, y_list314, y_list315 = [], [], []
for n in range(40000,10040000,40000): #250个数据点
    l=list((j,j) for j in range(n))
    x_list31.append(n) 
    y_list311.append(t311.timeit(number=10))
    y_list312.append(t312.timeit(number=10))
    y_list313.append(t313.timeit(number=10))
    y_list314.append(t314.timeit(number=10))
    y_list315.append(t315.timeit(number=10))
    
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
for i in range(len(x_list31)):
    x_list31[i]/=1000000
    y_list311[i]*=1000
    y_list312[i]*=1000
    y_list313[i]*=1000
    y_list314[i]*=1000
    y_list315[i]*=1000
r1=linefit(x_list31,y_list311)
print('k1='+str(r1[0]))
print('b1='+str(r1[1]))
print('r1='+str(r1[2]))
print('\nt1=%.2fn+%.2f\n'%(r1[0], r1[1]))
#拟合结果（斜率k，截距b，相关系数r）
r2=linefit(x_list31,y_list312)	
print('k2='+str(r2[0]))
print('b2='+str(r2[1]))
print('r2='+str(r2[2]))
print('\nt2=%.2fn+%.2f\n'%(r2[0], r2[1]))
#拟合结果（斜率k，截距b，相关系数r）
r3=linefit(x_list31,y_list313)
print('k3='+str(r3[0]))
print('b3='+str(r3[1]))
print('r3='+str(r3[2]))
print('\nt3=%.2fn+%.2f\n'%(r3[0], r3[1]))
#拟合结果（斜率k，截距b，相关系数r）
r4=linefit(x_list31,y_list314)
print('k4='+str(r4[0]))
print('b4='+str(r4[1]))
print('r4='+str(r4[2]))
print('\nt4=%.2fn+%.2f\n'%(r4[0], r4[1]))
#拟合结果（斜率k，截距b，相关系数r）
r5=linefit(x_list31,y_list315)
print('k5='+str(r5[0]))
print('b5='+str(r5[1]))
print('r5='+str(r5[2]))
print('\nt5=%.2fn+%.2f\n'%(r5[0], r5[1]))
#拟合结果（斜率k，截距b，相关系数r）
		
#绘图
xmax31 = x_list31[-1] 
#x轴的上界
dx31 = (x_list31[-1])/5 
#x轴的单位长度
ymax31 = float("{0:.2f}".format(max(y_list311)))  
#y轴的上界
dy31 = ymax31 / 5 
#y轴的单位长度
x31 = np.arange(0, xmax31+0.5*dx31, 0.01) #绘直线用
plt.figure(figsize=(16, 10))
plt.scatter(x_list31, y_list311, color='g', marker='+')
plt.plot(x31, r1[0]*x31+r1[1] , color='r')  #红色
plt.scatter(x_list31, y_list312, color='g', marker='+')
plt.plot(x31, r2[0]*x31+r2[1] , color='b')  #蓝色
plt.scatter(x_list31, y_list313, color='g', marker='+')
plt.plot(x31, r3[0]*x31+r3[1] , color='#924900')  #咖啡色
plt.scatter(x_list31, y_list314, color='g', marker='+')
plt.plot(x31, r4[0]*x31+r4[1] , color='#FF7700')  #橙色
plt.scatter(x_list31, y_list315, color='g', marker='+')
plt.plot(x31, r5[0]*x31+r5[1] , color='m')  #品红
plt.title('H2.3.1', fontsize=24)
plt.xlabel("n(*10^6)", fontsize=16)
plt.ylabel("time(*10^(-3)s)", fontsize=16)
plt.xlim((0, xmax31 + dx31))
plt.ylim((0, ymax31 + dy31))
xaxis = np.arange(0, xmax31 + dx31, dx31)
yaxis = np.arange(0, 2 * ymax31 + 4 * dy31, dy31)
#使数据点落在图像的中央
plt.xticks(xaxis)
plt.yticks(yaxis)
plt.show()

