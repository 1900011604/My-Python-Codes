#uuid_share#  5d37551e-17d8-41e7-bc98-76b37187478c  #
# SESSDSA20课程上机作业
# 【H4】动态规划作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的*函数体内*编写代码，每个题目的函数后有调用语句用于检验
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业在4月1日18:00之前提交到PyLn编程学习系统，班级码见Canvas系统


# =========== 1 博物馆大盗问题 ===========
# 给定一个宝物列表treasureList = [{'w': 2,'v': 3}, {'w': 3,'v': 4}, ...]
# 注意：每样宝物只有1个。
# 这样treasureList[0]['w']就是第一件宝物的重量，等等
# 给定包裹最多承重maxWeight > 0
# 实现一个函数，根据以上条件得到最高总价值以及对应的宝物
# 参数：宝物列表treasureList，背包最大承重maxWeight
# 返回值：最大总价值maxValue，选取的宝物列表choosenList(格式同treasureList)

def dpMuseumThief(treasureList, maxWeight):
    
    MaxValue = {(i, w):0 for i in range(len(treasureList) + 1)
                     for w in range(maxWeight + 1)}  #前i个宝物中，最大重量为w时装入宝物价值可能的最大值
    solution = {(i, w):[] for i in range(len(treasureList) + 1)  #前i个宝物中，最大重量为w时装入宝物价值最大时，装入的宝物
                     for w in range(maxWeight + 1)}      
    chosenList = []
    
    for i in range(1, len(treasureList) + 1):  
        for w in range(1, maxWeight + 1):
            
            if treasureList[i - 1]['w'] > w:  #第i个宝物本身（不算之前已经装入的）就太大，一定装不下
                MaxValue[(i, w)] = MaxValue[(i - 1, w)]
                solution[(i, w)] = solution[(i - 1, w)][:]
                #MaxValue, MinWeight, solution不变

            else:  #第i个宝物可以装下，比较装入与不装入两种情况对应的价值
                if MaxValue[(i - 1, w)] > MaxValue[(i - 1, w - treasureList[i - 1]['w'])] + treasureList[i - 1]['v']:
                    #不装入第i个宝物总价值更高
                    MaxValue[(i, w)] = MaxValue[(i - 1, w)]
                    solution[(i, w)] = solution[(i - 1, w)][:]
                    #MaxValue, MinWeight, solution不变

                else:
                    #装入第i个宝物时总价值更高
                    MaxValue[(i, w)] = MaxValue[(i - 1, w - treasureList[i - 1]['w'])] + treasureList[i - 1]['v']  
                    solution[(i, w)] = solution[(i - 1, w - treasureList[i - 1]['w'])][:]                    
                    solution[(i, w)].append(treasureList[i - 1])  #装入第i个宝物
                    #记录新的MaxValue, MinWeight, solution值
            
    maxValue = MaxValue[(len(treasureList), maxWeight)]  #maxValue是MaxValue的最后一个元素
    chosenList = solution[(len(treasureList), maxWeight)]  #chosenList是solution的最后一个元素
    return maxValue, chosenList

# 检验
print("=========== 1 博物馆大盗问题 ============")
treasureList = [[{'w':2, 'v':3}, {'w':3, 'v':4}, {'w':4, 'v':8}, {'w':5, 'v':8}, {'w':9, 'v':10}]]
treasureList.append([{'w':1, 'v':2}, {'w':2, 'v':2}, {'w':2, 'v':3}, {'w':4, 'v':5}, {'w':4, 'v':6}, {'w':4, 'v':7}, {'w':5, 'v':7},
                     {'w':5, 'v':8}, {'w':6, 'v':8}, {'w':6, 'v':10}, {'w':7, 'v':10}, {'w':7, 'v':12}, {'w':8, 'v':12}, {'w':8, 'v':13}, {'w':9, 'v':14}, {'w':9, 'v':16}])
treasureList.append([{'w':1, 'v':2}, {'w':2, 'v':2}, {'w':2, 'v':3}, {'w':3, 'v':4}, {'w':3, 'v':5}, {'w':4, 'v':6}, {'w':4, 'v':7},
                     {'w':5, 'v':7}, {'w':5, 'v':8}, {'w':6, 'v':8}, {'w':6, 'v':10}, {'w':7, 'v':11}, {'w':7, 'v':12}, {'w':8, 'v':13},
                     {'w':8, 'v':14}, {'w':9, 'v':15}, {'w':9, 'v':16}, {'w':9, 'v':17}, {'w':10, 'v':17}, {'w':10, 'v':18}, {'w':11, 'v':18}])
treasureList.append([{'w':1, 'v':2}, {'w':2, 'v':2}, {'w':2, 'v':3}, {'w':3, 'v':4}, {'w':3, 'v':5}, {'w':4, 'v':5}, {'w':4, 'v':6},
                     {'w':5, 'v':6}, {'w':5, 'v':7}, {'w':6, 'v':8}, {'w':6, 'v':9}, {'w':7, 'v':10}, {'w':7, 'v':11}, {'w':8, 'v':12},
                     {'w':8, 'v':13}, {'w':9, 'v':14}, {'w':9, 'v':15}, {'w':9, 'v':16}, {'w':10, 'v':16}, {'w':10, 'v':17}, {'w':11, 'v':18},
                     {'w': 12, 'v': 18}, {'w': 12, 'v': 19}, {'w': 13, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 21}, {'w': 14, 'v': 22}])
treasureList.append([{'w':1, 'v':2}, {'w':2, 'v':2}, {'w':2, 'v':3}, {'w':3, 'v':4}, {'w':3, 'v':5}, {'w':4, 'v':5}, {'w':4, 'v':6},
                     {'w':5, 'v':6}, {'w':5, 'v':7}, {'w':6, 'v':8}, {'w':6, 'v':9}, {'w':7, 'v':9}, {'w':7, 'v':10}, {'w':8, 'v':11},
                     {'w':8, 'v':12}, {'w':9, 'v':13}, {'w':9, 'v':14}, {'w':9, 'v':15}, {'w':10, 'v':16}, {'w':10, 'v':17}, {'w':11, 'v':18},
                     {'w': 11, 'v': 19}, {'w': 12, 'v': 20}, {'w': 13, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 21}, {'w': 14, 'v': 22},
                     {'w': 14, 'v': 23}, {'w': 15, 'v': 24},{'w': 15, 'v': 25}, {'w': 16, 'v': 26},{'w': 17, 'v': 27}, {'w': 18, 'v': 28}])

maxWeightList = [20, 50, 80, 100, 150]
for i in range(len(treasureList)):
    maxValue, choosenList = dpMuseumThief(treasureList[i], maxWeightList[i])
    print(maxValue)
    print(choosenList)
print('')

'''
# 可有多种取法，以下只给出一种符合条件的宝物列表
# 29
# [{'w':2, 'v':3}, {'w':4, 'v':8}, {'w':5, 'v':8}, {'w':9, 'v':10}]
# 83
# [{'w': 1, 'v': 2}, {'w': 2, 'v': 3}, {'w': 4, 'v': 7}, {'w': 5, 'v': 8}, {'w': 6, 'v': 10},
    {'w': 7, 'v': 12}, {'w': 8, 'v': 12}, {'w': 8, 'v': 13}, {'w': 9, 'v': 16}]
# 139
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 5}, {'w': 4, 'v': 6}, {'w': 4, 'v': 7}, {'w': 6, 'v': 10}, {'w': 7, 'v': 12},
    {'w': 8, 'v': 14}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 9, 'v': 17}, {'w': 10, 'v': 17}, {'w': 10, 'v': 18}]
# 164
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 5}, {'w': 8, 'v': 13}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16},
    {'w': 10, 'v': 16}, {'w': 10, 'v': 17}, {'w': 11, 'v': 18}, {'w': 12, 'v': 19}, {'w': 13, 'v': 21}, {'w': 14, 'v': 22}]
# 246
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 9, 'v': 15}, {'w': 10, 'v': 17},
    {'w': 11, 'v': 18}, {'w': 11, 'v': 19}, {'w': 12, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 23},
    {'w': 15, 'v': 24}, {'w': 15, 'v': 25}, {'w': 16, 'v': 26}, {'w': 17, 'v': 27}]
'''

# ========= 2 单词最小编辑距离问题 =========
# 实现一个函数，给定两个单词，得出从源单词变到目标单词所需要的最小编辑距离，返回总得分与编辑操作过程
# 可以进行的操作有：
# 从源单词复制一个字母到目标单词
# 从源单词删除一个字母
# 在目标单词插入一个字母
# 参数：两个字符串，即源单词original与目标单词target，以及不同操作对应的分值，即一个字典
# 返回值：一个整数与一个列表，最低的分数与操作过程，示例见检验
## 编辑操作过程不一定唯一，给出一种满足条件的操作过程即可

def dpWordEdit(original, target, oplist):
    score = 0
    operations = []

    def Insert(s):
        return oplist['insert']  #添加一个字母

    def Delete(t):             
        return oplist['delete']  #删除一个字母

    def Replace(m, n):
        if m == n:
            return oplist['copy']  #替换一个相同的字母 == 复制一个字母
        else:
            return oplist['insert'] + oplist['delete']  #替换一个不同的字母 == 添加一个字母，再删除一个字母

    originalList = list(original)  #源单词列表
    targetList = list(target)  #目标单词列表

    MinScore = {(i, j):0 for i in range(len(originalList) + 1)
                         for j in range(len(targetList) + 1)}
    #二维字典，储存由源单词中前i个字母变为目标单词中前j个字母所需要操作过程的分值
    
    solution = {(i, j):[] for i in range(len(originalList) + 1)
                          for j in range(len(targetList) + 1)}
    #二维字典，储存由源单词中前i个字母变为目标单词中前j个字母所需要的最少操作过程

    #填写两个表格的首行和首列
    for i in range(1, len(originalList) + 1):
        MinScore[(i, 0)] = i * oplist['delete']
        solution[(i, 0)] = solution[(i - 1, 0)][:]
        solution[(i, 0)].append('delete {0}'.format(originalList[i - 1]))

    for j in range(1, len(targetList) + 1):
        MinScore[(0, j)] = j * oplist['insert']
        solution[(0, j)] = solution[(0, j - 1)][:]
        solution[(0, j)].append('insert {0}'.format(targetList[j - 1]))

    #动态规划的核心：从一个局部最优解转化为下一个逐步最优解    
    for i in range(1, len(originalList) + 1):
        for j in range(1, len(targetList) + 1):
            MinScore[(i, j)] = min(MinScore[(i, j - 1)] + Insert(targetList[j - 1]),
                                   #源单词比目标单词少一个字母，添加该字母，记录分值
                                   MinScore[(i - 1, j - 1)] + Replace(originalList[i - 1], targetList[j - 1]),
                                   #源单词与目标单词同时增加一个字母，比较这两个字母是否相同，
                                   #选择是复制该字母或是添加目标字母，再删除原字母，记录相应分值
                                   MinScore[(i - 1, j)] + Delete(originalList[i - 1]))
                                   #源单词比目标单词多一个字母，删去该字母，记录分值

            if MinScore[(i, j)] == MinScore[(i, j - 1)] + Insert(targetList[j - 1]):
                solution[(i, j)] = solution[(i, j - 1)][:]
                solution[(i, j)].append('insert {0}'.format(targetList[j - 1]))
                #源单词比目标单词少一个字母，添加该字母，记录操作
            elif MinScore[(i, j)] == MinScore[(i - 1, j - 1)] + Replace(originalList[i - 1], targetList[j - 1]):
                solution[(i, j)] = solution[(i - 1, j - 1)][:]
                if originalList[i - 1] == targetList[j - 1]:
                    solution[(i, j)].append('copy {0}'.format(targetList[j - 1]))
                    #源单词与目标单词同时增加一个字母，两个字母相同，复制该字母，记录操作
                else:
                    solution[(i, j)].append('insert {0}'.format(targetList[j - 1]))
                    solution[(i, j)].append('delete {0}'.format(originalList[i - 1]))
                    #源单词与目标单词同时增加一个字母，两个字母不同，添加目标字母，再删除原字母，记录操作
            else:
                solution[(i, j)] = solution[(i - 1, j)][:]
                solution[(i, j)].append('delete {0}'.format(originalList[i - 1]))
                #源单词比目标单词多一个字母，删去该字母，记录操作
                
    score = MinScore[(len(originalList), len(targetList))]  #最终分值是MinScore表中的最后一个元素
    operations = solution[(len(originalList), len(targetList))]  #最终操作是solution表中的最后一个元素
    return score, operations

# 检验
print("========= 2 单词最小编辑距离问题 =========")
oplist = [{'copy': 5, 'delete': 20, 'insert': 20},
          {'copy':5, 'delete':10, 'insert':15},
          {'copy':10, 'delete':25, 'insert':20}]
originalWords = ["cane", "sheep", "algorithm", "debug", "difficult", "directory", "wonderful"]
targetWords = ["new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"]

for i in range(len(oplist)):  #可以同时对三种分值设置进行检验
    for j in range(len(originalWords)):
        score, operations = dpWordEdit(originalWords[j], targetWords[j], oplist[i])
        print(score)
        print(operations)
    print('')
    
'''    
# 70
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 60
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 185
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o',
    'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 205
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s',
    'insert e', 'delete b', 'delete u', 'delete g']
# 200
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n',
    'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 220
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w',
    'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 235
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r',
    'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']

# 45
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 45
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 125
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o',
    'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 135
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s',
    'insert e', 'delete b', 'delete u', 'delete g']
# 130
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n',
    'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 145
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w',
    'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 150
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r',
    'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']

# 90
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 85
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 230
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o',
    'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 230
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s',
    'insert e', 'delete b', 'delete u', 'delete g']
# 245
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n',
    'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 265
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w',
    'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 280
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r',
    'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
'''
