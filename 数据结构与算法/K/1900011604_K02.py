import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
from timeit import Timer

#计时实验程序1 list.insert(0, item)：添加数据项成为列表的第一个元素
def test1():
    return l.insert(0, -1)

t1 = Timer('test1()', 'from __main__ import test1')
x_list1 = []
y_list1 = []
for n in range(100000, 1100000, 100000):  #10个数据点
    l = list(range(n))
    x_list1.append(n)
    y_list1.append(t1.timeit(number = 1000))
for i in range(len(x_list1)):
    x_list1[i] /= 1000000
    print('%.7f'%(y_list1[i]))

def f1(n, k, b):  #线性拟合数据点
    return k * n + b
fita, fitb = opt.curve_fit(f1, x_list1, y_list1)
print('\nk=' + str(fita[0]))
print('b=' + str(fita[1]))
print('t=%.2fn+%.2f\n'%(fita[0], fita[1]))
#拟合结果（斜率k，截距b）

# 绘图
xmax1 = x_list1[-1]  #x轴的上界
dx1 = x_list1[-1] / 5  #x轴的单位长度
ymax1 = float('%.4f'%max(y_list1))  #y轴的上界
dy1 = ymax1 / 5  #y轴的单位长度
x1 = np.arange(0,xmax1 + dx1, 0.01) #绘直线用
plt.figure(figsize = (16, 10))
plt.scatter(x_list1, y_list1, color = 'g', marker = '+')
plt.plot(x1, f1(x1, fita[0], fita[1]), color = 'r')
plt.title('K02-1', fontsize = 24)
plt.xlabel("n(*10^6)", fontsize = 16)
plt.ylabel("time(s)", fontsize = 16)
plt.xlim((0, xmax1 + dx1))
plt.ylim((0,ymax1+dy1))
xaxis = np.arange(0, xmax1 + dx1, dx1)
yaxis = np.arange(0, 2 * ymax1 + 4 * dy1, dy1)
#使数据点落在图像的中央
plt.xticks(xaxis)
plt.yticks(yaxis)

plt.show()

#计时实验程序2 list.append(item)：添加数据项成为列表的最后一个元素
def test2():
    return l.append(-1)

t2 = Timer('test2()', 'from __main__ import test2')
x_list2 = []
y_list2 = []
for n in range(100000, 1100000, 100000):  #10个数据点
    l = list(range(n))
    x_list2.append(n)
    y_list2.append(t2.timeit(number = 100000))
for i in range(len(x_list2)):
    x_list2[i] /= 1000000
    print('%.7f'%(y_list2[i]))

def f2(n,k,b):  #线性拟合数据点
    return k * n + b
fita, fitb = opt.curve_fit(f2, x_list2, y_list2)
print('\nk=' + str(fita[0]))
print('b=' + str(fita[1]))
print('t=%.2fn+%.2f\n'%(fita[0], fita[1]))
#拟合结果（斜率k，截距b）

# 绘图
xmax2 = x_list2[-1]  #x轴的上界
dx2 = x_list2[-1] / 5  #x轴的单位长度
ymax2 = float('%.4f'%max(y_list2))  #y轴的上界
dy2 = ymax2 / 5  #y轴的单位长度
x2 = np.arange(0, xmax2 + dx2, 0.01) #绘直线用
plt.figure(figsize = (16, 10))
plt.scatter(x_list2, y_list2, color='g', marker='+')
plt.plot(x2, f2(x2, fita[0], fita[1]), color='r')
plt.title('K02-2', fontsize=24)
plt.xlabel("n(*10^6)", fontsize=16)
plt.ylabel("time(ms)", fontsize=16)
plt.xlim((0, xmax2 + dx2))
plt.ylim((0,ymax2+dy2))
xaxis = np.arange(0, xmax2 + dx2, dx2)
yaxis = np.arange(0, 2 * ymax2 + 4 * dy2, dy2)
#使数据点落在图像的中央
plt.xticks(xaxis)
plt.yticks(yaxis)

plt.show()
