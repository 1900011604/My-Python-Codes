import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 2. 计算霍尔电压 UH,验证 UH -B线性关系。计算霍尔元件的灵敏度 KH 及其不确定度

I_H = 10
U_H = [0.285,11.07,22.4525,33.635,44.8,55.7625,66.8675,77.725,88.52,98.81,109.0775]
I_M = [0.1*i for i in range(0,11)]
B_array = np.arange(0, 360, 0.01)
BI_H = [0.004, 0.3595, 0.726, 1.086, 1.45, 1.8025,
     2.166, 2.514, 2.8655, 3.2025, 3.5295]
B = []
for i in BI_H:
    i = i * 100
    B.append(i)
K_H, b = 30.86345545, 0.0749707814
U_H_array = 0.01 * K_H * B_array + b

plt.figure(figsize=(16, 10))
plt.xlim(0, 370)
plt.ylim(0, 115)
my_x_ticks = np.arange(0, 400, 50)
my_y_ticks = np.arange(0, 120, 10)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.scatter(B, U_H, marker='+', color='r')
plt.plot(B_array, U_H_array, color='g')
plt.show()

# 3. 根据2中计算的 U H 和 KH,计算B,作出磁化曲线图

U_H_array = np.array([0.285,11.07,22.4525,33.635,44.8,55.7625,66.8675,77.725,88.52,98.81,109.0775])

B_array = (U_H_array-b)/(K_H*I_H)

f = interp1d(I_M, B, kind='cubic')

I_M_linspace = np.linspace(0, 1, num=1000, endpoint=True)

plt.figure(figsize=(16, 10))
plt.xlim(0, 1.05)
plt.ylim(0, 375)
my_x_ticks = np.arange(0, 1.1, 0.1)
my_y_ticks = np.arange(0, 400, 50)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.scatter(I_M, B, marker='+', color='r')
plt.plot(I_M_linspace, f(I_M_linspace), color='g')
plt.show()

# 4. 根据测得的 UH-x关系和 KH,计算B-x关系,并作图

U_H_array = np.array([5.72,7.54,10.68,17.57,45.69,58.77,67.33,69.14,68.60,67.78,67.29,67.13,67.02,66.97,66.98,67.01,67.13,67.18,67.22,67.26,67.22,67.12,66.83,66.23])

x = np.array([98,93,88,83,78,77,76,75,74,73,72,71,70,68,66,64,60,56,52,48,46,44,42,40])

I_H = 10
K_H, b = 30.86345545, 0.0749707814
B_array = 1000*(U_H_array-b)/(K_H*I_H)

f = interp1d(x, B_array, kind='cubic')

x_linspace = np.linspace(40, 98, num=5800, endpoint=True)

plt.figure(figsize=(16, 10))
plt.xlim(38, 102)
plt.ylim(0, 250)
my_x_ticks = np.arange(40,110,10)
my_y_ticks = np.arange(0, 300, 50)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.scatter(x, B_array, marker='+', color='r')
plt.plot(x_linspace, f(x_linspace), color='g')
plt.show()

# a接法，1,2端
U_2 = [13.27, 13.40, 13.28, 13.30]
U_4 = [26.75, 26.84, 26.55, 26.63]
U_6 = [40.05, 40.28, 39.78, 40.11]
U_8 = [53.29, 53.80, 53.07, 53.62]
U_10 = [66.52, 67.35, 66.38, 67.21]
U = [U_2, U_4, U_6, U_8, U_10]
U_0 = 0
for i in U:
    U_0 = (i[0] - i[1] - i[2] + i[3])*0.25
    print(U_0)
U_NR = 0
for i in U:
    U_NR = (i[0] + i[1] - i[2] - i[3])*0.25
    print(U_NR)

# b接法，3,4端
U_2 = [13.31, 13.30, 13.38, 13.39]
U_4 = [26.63, 26.60, 26.76, 26.80]
U_6 = [40.02, 39.91, 40.14, 40.22]
U_8 = [53.45, 53.31, 53.59, 53.68]
U_10 = [67.08, 66.66, 67.00, 67.10]
U = [U_2, U_4, U_6, U_8, U_10]
U_0 = 0
for i in U:
    U_0 = (i[0] - i[1] - i[2] + i[3])*0.25
    print(U_0)
U_NR = 0
for i in U:
    U_NR = (i[0] + i[1] - i[2] - i[3])*0.25
    print(U_NR)