import numpy as np
import matplotlib.pyplot as plt
from timeit import Timer
from H5 import mydict

md = mydict()

# 测试del函数的性能
def test_del():
    for i in range(500):
        del md[n - 1000 + i]  # 删除500个元素
t = Timer("test_del()", "from __main__ import test_del")

'''
# 测试set函数的性能
md = mydict()
def test_set():
    for i in range(50000000,50000500):
	    md[i] = i   # 添加500个元素
t = Timer("test_set()", "from __main__ import test_set")
'''

'''
# 测试get函数的性能
def test_get():
    a = 0
    for i in range(1000):
        a = md[n - 1020 + i]    # 按key查找1000个元素
t = Timer("test_get()", "from __main__ import test_get")
'''

'''
# 测试in函数的性能
def test_in():
    a = True
    for i in range(1000):
	    a = 50000000 in md  # 判断1000次（全部输出为False，可以遍历整个字典）
t = Timer("test_in()", "from __main__ import test_in")
'''

# 数据表
x_list = []
y_list = []
Nlist = []
for i in range(200, 400):
    Nlist.append(int(2 ** (i / 20)))
for n in Nlist:  # 200个数据点
    for j in range(n):
        md[j] = j
    x_list.append(np.log2(n))
    y_list.append(t.timeit(number=1))
    print(len(md))
    md.clear()

# 拟合数据点，得到平均值和标准差
def linefit(x, y):
    N = len(x)
    sy, syy = 0, 0
    for i in range(0, N):
        sy += y[i]
        syy += y[i] ** 2
    ybar = sy / N   # 平均值
    σ = ((syy - N * ybar ** 2) / N) ** 0.5  # 标准差
    return [ybar, σ]

# 拟合结果
r = linefit(x_list, y_list)
print(r)
print('Average =', str(r[0]))
print('σ =', str(r[1]))

# 绘图
xmax = x_list[-1]
# x轴的上界
dx = x_list[-1] / 5
# x轴的单位长度
ymax = float("{0:.2f}".format(max(y_list)))
# y轴的上界
dy = ymax / 5
# y轴的单位长度
x = np.arange(0, xmax + 0.5*dx, 0.01)  # 绘直线用
plt.figure(figsize=(16, 10))
plt.scatter(x_list, y_list, color='g', marker='+')
plt.plot(x, r[0] + r[1] + 0 * x, color='b')
plt.plot(x, r[0] + 0 * x, color='r')
plt.plot(x, r[0] - r[1] + 0 * x, color='b')
plt.title('H5', fontsize=24)
plt.xlabel("log_2(n)", fontsize=16)
plt.ylabel("time(s)", fontsize=16)
plt.xlim((0, xmax + dx))
plt.ylim((0, ymax + dy))
xaxis = np.arange(0, xmax + dx, dx)
yaxis = np.arange(0, 2 * ymax + 4 * dy, dy)
# 使数据点落在图像的中央
plt.xticks(xaxis)
plt.yticks(yaxis)
plt.show()
