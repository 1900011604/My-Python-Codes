import json as js
from __1900011604_FIN_Graph__ import Graph
import time
import matplotlib.pyplot as plt


########################################################
'''
@@@@@@@@@@@@@@@@@@@@  构建图数据结构  @@@@@@@@@@@@@@@@@@@@
'''
########################################################


t0 = time.time()

# 创建电影的列表：
films = js.load(open('Film.json'))
films = list(films)

# 创建演员的列表：
actors = set()
for i in films:
    filmActors = i['actor'].split(',')
    filmActors = set(filmActors)
    filmActors = list(filmActors)
    for j in filmActors:
        actors.add(j)
actors = list(actors)

# 创建以演员为节点的图：
g = Graph()
for i in actors:
    g.addVertex(i)

# 遍历每一部电影，在每一部电影的演员中两两建立无向边
lenedge = 0
for f in films:
    actorlist = f['actor'].split(',')
    l = len(actorlist)
    for i in range(l):
        for j in range(i, l):
            if i != j:  # 去除重复
                k = f["_id"]["$oid"]
                g.addEdge(actorlist[i], actorlist[j], k)
                lenedge += 1
                # 在每一部电影的演员中两两建立无向边，边的属性为该电影的$oid
            else:  # 一部电影中有两个相同的演员
                g.getVertex(actorlist[j]).attribute.add(f["_id"]["$oid"])
    if l == 1:
        g.getVertex(actorlist[0]).attribute.add(f["_id"]["$oid"])
        
print('顶点数：', len(g.vertList))
print('边数：', lenedge)

# 将films转化为以$oid为key，film为value的字典
films_key = []
films_value = []
for i in films:
    films_key.append(i["_id"]["$oid"])
    films_value.append(i)
films = dict(zip(films_key, films_value))

t1 = time.time()
print('\nTime to build Graph =', "{:.2f}s\n".format(t1 - t0))


########################################################
'''
@@@@@@@@@@@@@@@@@@@@  Question 1  @@@@@@@@@@@@@@@@@@@@
'''
########################################################


t0 = time.time()

CClist = g.CC()  # 计算演员构成的图的所有连通分支
CClist.sort(key=lambda i: len(i), reverse=False)  
# 连通分支按照规模从小到大排列
print('连通分支的个数：', len(CClist))  # 连通分支的个数

CClist_min_max = CClist[-1:-21:-1] + CClist[0:20:]  
# 按照连通分支规模从大到小排序，最大和最小的20个连通分支
sizeList = []
for i in CClist_min_max:
    sizeList.append(len(i))  # 每个连通分支有多少演员

# 每个连通分支电影所属类别的前三名和平均星级
CCfilms_type = []
CCfilms_avgstar = []

# first_three函数，获取一个列表中出现次数前三名的元素
def first_three(lst):
    lst_copy = list(set(lst[:]))  # 复制列表，并将其转化为集合去重，再恢复为列表
    lst_dict = dict(zip(lst_copy, [0 for i in range(len(lst_copy))]))
    # 创造以列表项为key，该项出现次数（默认为0）为value的字典
    for i in lst:
        for j in lst_copy:
            if i == j:
                lst_dict[j] += 1  # 对lst_copy中每一项逐一统计其在lst中出现的次数
    lst_level = sorted(lst_dict.items(),\
                       key=lambda lst_dict: lst_dict[1], reverse=True)
    # 对lst_level按照value的大小（出现次数）从大到小排序
    lst_level = lst_level[0:4]
    i = 0
    lst_123 = []
    while i < len(lst_level) and i < 3:
        lst_123.append(lst_level[i][0])
        i += 1
    return lst_123

for i in CClist_min_max:  # 每一个连通分支
    CCfilms = []  # 连通分支中的电影
    CCstar = 0
    CCtype = []  # 每个连通分支中电影所属类别的总和
    for j in i:  # 遍历每一个演员
        CCfilms += list(g.getVertex(j).attribute)
    CCfilms = set(CCfilms)  # 转化为集合去重
    CCfilms = list(CCfilms)
    for i in CCfilms:
        CCstar += films[i]["star"]
        CCtype += films[i]["type"].split(',')
    CCtype = first_three(CCtype)  # 每个连通分支中电影所属类别的前三名
    CCfilms_type.append(CCtype)
    CCfilms_avgstar.append("{:.2f}".format(CCstar / len(CCfilms)))
    # 平均星级保留两位小数

t1 = time.time()
print('\nTime to calculate Question 1 =', "{:.2f}s\n".format(t1 - t0))


########################################################
'''
@@@@@@@@@@@@@@@@@@@@  Question 2  @@@@@@@@@@@@@@@@@@@@
'''
########################################################


t0 = time.time()

# 顶点颜色归零
for i in g:
    i.color = 0

CCdist_list = [17]  # 连通分支直径的列表
# 第一个连通分支的直径是17
CClist_min_max_part = CClist_min_max[1:20]
# 最后20个连通分支直径都是0（因为规模为1），只需要算19个

for i in CClist_min_max_part:  # i是连通分支
    CCdist = []
    for j in i:  # j是演员名字的字符串，也就是顶点的id
        g.bfs_dist(j)
        distList = []  # 每个顶点的距离值
        for k in i:
            distList.append(g.getVertex(k).dist)
        distMax = max(distList)  # 一个顶点到其它所有顶点距离中的最大值
        CCdist.append(distMax)
    CCdist_Max = max(CCdist)  # 连通分支的直径
    CCdist_list.append(CCdist_Max)  

for i in range(20):
    CCdist_list.append(0)  # 最后20个连通分支直径都是0（因为规模为1）


# 输出40个连通分支的规模、直径、电影所属类别的前三名和电影的平均星级
print('{:<20}'.format('Connected component'), \
      '{:<10}'.format('Size'), \
      '{:<30}'.format('Diameter'), \
      '{:<30}'.format('Average number of stars'), \
      '{:<20}'.format('First three types of films')) 


for i in range(40):
    print('{:<20}'.format(str(i+1)), \
          '{:<10}'.format(str(sizeList[i])), \
          '{:<30}'.format(str(CCdist_list[i])), \
          '{:<30}'.format(str(CCfilms_avgstar[i])), \
          '{:<20}'.format(str(CCfilms_type[i]))) 

t1 = time.time()
print('\nTime to calculate Question 2 =', "{:.2f}s\n".format(t1 - t0))


########################################################
'''
@@@@@@@@@@@@@@@@@@@@  Question 3  @@@@@@@@@@@@@@@@@@@@
'''
########################################################


# 用subplot()方法绘制多幅图形
plt.figure(figsize=(15, 10), dpi=100)

# 用matplotlib画出连通分支的规模（顶点个数）
ax1 = plt.subplot(311)

x = [i for i in range(1,41)]   
y = [85] + sizeList[1:]  # 最大的连通分支规模为84687，显示高度为85
# 画出柱状图
plt.bar(x, y, width=0.75, align='center', color='r')
# 设置y轴的范围
plt.ylim(0, 100)
# 设置x、y轴的刻度
plt.xticks([i for i in range(1,41)])
plt.yticks([0, 20, 40, 60])
# x、y轴标签与图形标题
plt.xlabel('connected component')
plt.ylabel('vertex')
plt.title('Size for each connected component')
# 设置数字标签
for a, b in zip(x[0:1], sizeList[0:1]):  
    # 最大的连通分支规模为84687，显示高度为85，需要对标签位置作出调整
    plt.text(a, b-84602+0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)
for a, b in zip(x[1:], sizeList[1:]):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)


# 用matplotlib画出连通分支的直径
ax2 = plt.subplot(312)

x = [i for i in range(1,41)]   
y = CCdist_list
# 画出柱状图
plt.bar(x, y, width=0.75, align='center', color='g')
# 设置x轴的刻度
plt.xticks([i for i in range(1,41)])
plt.yticks([0, 5, 10, 15, 20])
# 设置y轴的范围
plt.ylim(0, 20)
# x、y轴标签与图形标题
plt.xlabel('connected component')
plt.ylabel('diameter / vertex')
plt.title('Diameter for each connected component')
# 设置数字标签
for a, b in zip(x, y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)


# 用matplotlib画出连通分支的平均星级
ax3 = plt.subplot(313)

CCfilms_avgstar_list = []
for i in CCfilms_avgstar:
    CCfilms_avgstar_list.append(float(i))  
# 将平均星级（原来是字符串类型）转化为浮点数类型，用于绘图

x = [i for i in range(1,41)]     
y = CCfilms_avgstar_list
# 画出柱状图
plt.bar(x, y, width=0.75, align='center', color='c')
# 设置x轴的刻度
plt.xticks([i for i in range(1,41)])
# 设置y轴的范围
plt.ylim(0, 10)
# x、y轴标签与图形标题
plt.xlabel('connected component')
plt.ylabel('star')
plt.title('Average number of stars for each connected component')
# 设置数字标签
for a, b in zip(x, y):
    plt.text(a, b+0.05, '%.2f' % b, ha='center', va='bottom', fontsize=8)


# 调整每个子图之间的距离
plt.tight_layout()
plt.show()


########################################################
'''
@@@@@@@@@@@@@@@@@@@@  Question 4  @@@@@@@@@@@@@@@@@@@@
'''
########################################################

t0 = time.time()

# 返回演员actorname出演的电影以及电影星级之和的函数
def actordata(actorname):
    actorname = g.getVertex(actorname)
    filmlist = list(actorname.attribute)  
    # 将演员actorname出演的电影集合转化为可迭代的列表
    actorstar = 0
    for i in filmlist:
        actorstar += films[i]["star"]  # 电影星级之和
    avgStar = actorstar / len(actorname.attribute)
    return avgStar

zxcAvgStar = actordata('周星驰')
print("周星驰所出演的电影平均星级：", "{:.2f}".format(zxcAvgStar))
# 计算周星驰所出演的电影平均星级（电影星级之和除以电影数目），并保留两位小数输出

t1 = time.time()
print('\nTime to calculate Question 4 =', "{:.2f}ms\n".format((t1 - t0) * 1000))


########################################################
'''
@@@@@@@@@@@@@@@@@@@@  Question 5  @@@@@@@@@@@@@@@@@@@@
'''
########################################################


t0 = time.time()

def Question_5(actorname): 
    # 返回演员和共同出演者总人数、出演的电影总数、电影所属类别的前三名和平均星级的函数
    actorname = g.getVertex(actorname)
    coActor = list(actorname.connectedTo.keys())  # 邻接顶点
    coActor.append(actorname)  # 加上演员自身
    coActor_num = len(coActor)  # 演员与共同出演者的总人数
    coFilm = []  # 出演的电影总数
    coFilmType = []
    for i in coActor:
        coFilm += list(i.attribute)
    coFilm = set(coFilm)  # 转化为集合去重
    coFilm = list(coFilm)
    coFilm_num = len(coFilm)  # 各自一共出演的电影总数
    coStar = 0
    coFilmType = []
    for i in coFilm:
        coStar += films[i]["star"]
        coFilmType += films[i]["type"].split(',')
    coFilmType_123 = first_three(coFilmType)  # 电影所属类别的前三名
    coStar_avg = "{:.2f}".format(coStar / coFilm_num)  # 所出演的电影平均星级
    solution = [coActor_num, coFilm_num, coStar_avg, coFilmType_123]
    return solution


zxclist5 = Question_5('周星驰')
print("周星驰和他的共同出演者一共有{}人".format(zxclist5[0]))
print("他们各自一共出演的电影总数：", zxclist5[1])
print("所出演的电影平均星级：", zxclist5[2])
print("电影所属类别的前三名为{}、{}与{}".format(\
        zxclist5[3][0], zxclist5[3][1], zxclist5[3][2]))

t1 = time.time()
print('\nTime to calculate Question 5 =', "{:.2f}ms\n".format((t1 - t0) * 1000))


########################################################
'''
@@@@@@@@@@@@@@@@@@@@  Question 6  @@@@@@@@@@@@@@@@@@@@
'''
########################################################


t0 = time.time()

_4Kings = ['张学友', '刘德华', '黎明', '郭富城']
co4Kings = {}

def getTitle(i, j):  
    # 获取顶点为i、j的边属性中的电影名称列表
    titleList = []
    for i in g.getEdge(i, j):
        titleList.append(films[i]["title"])
    return titleList
    
for i in range(4):
    for j in range(i, 4):
        if i != j:
            king_i = _4Kings[i]
            king_j = _4Kings[j]
            co4Kings[king_i, king_j] = getTitle(king_i, king_j)

for i in co4Kings:
    print("{}与{}共演的电影：".format(i[0], i[1]),'\n', co4Kings[i], '\n')
    
print("{}、{}与{}共演的电影：".format('张学友', '刘德华', '黎明'))
setabc = set(getTitle('张学友', '刘德华')) & set(getTitle('刘德华', '黎明'))
print(setabc, '\n')

print("{}、{}与{}共演的电影：".format('张学友', '刘德华', '郭富城'))
setabd = set(getTitle('张学友', '刘德华')) & set(getTitle('刘德华', '郭富城'))
print(setabd, '\n')

print("{}、{}与{}共演的电影：".format('张学友', '黎明', '郭富城'))
setacd = set(getTitle('张学友', '黎明')) & set(getTitle('黎明', '郭富城'))
print(setacd, '\n')

print("{}、{}与{}共演的电影：".format('刘德华', '黎明', '郭富城'))
setbcd = set(getTitle('刘德华', '黎明')) & set(getTitle('黎明', '郭富城'))
print(setbcd, '\n')

print('集齐香港四大天王的电影：')
setabcd = setabc & setbcd
print(setabcd)

t1 = time.time()
print('\nTime to calculate Question 6 =', "{:.2f}ms\n".format((t1 - t0) * 1000))