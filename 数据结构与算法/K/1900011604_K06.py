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

    MinScore = {}
    #字典，储存递归过程中的中间步骤
    solution = {(i, j):[] for i in range(len(originalList) + 1)
                          for j in range(len(targetList) + 1)}
    #二维字典，储存由源单词中前i个字母变为目标单词中前j个字母所需要的最少操作过程

    def minscore(i, j):  #双重递归，在MinScore中填写一个二维递归字典
        
        if i == 0 and j != 0:
            sco = j * oplist['insert']
            MinScore[(i, j)] = sco
            solution[(i, j)] = solution[(i, j - 1)][:]
            solution[(i, j)].append('insert {0}'.format(targetList[j - 1]))
            return sco
        #递归字典的首行
        
        elif j == 0 and i != 0:
            sco = i * oplist['delete']
            MinScore[(i, j)] = sco
            solution[(i, j)] = solution[(i - 1, j)][:]
            solution[(i, j)].append('delete {0}'.format(originalList[i - 1]))
            return sco
        #递归字典的首列
        
        elif i == 0 and j == 0:
            sco = 0
            MinScore[(i, j)] = sco
            solution[(i, j)] = []
            return sco
        #递归字典的第一个元素
        
        elif (i, j) in MinScore:  #(i, j)元的值已经被储存在MinScore中，则直接返回
            sco = MinScore[(i, j)]
            return sco
        
        else:
            sco = min(minscore(i, j - 1) + Insert(targetList[j - 1]),
                                   #源单词比目标单词少一个字母，添加该字母，记录分值
                                   minscore(i - 1, j - 1) + Replace(originalList[i - 1], targetList[j - 1]),
                                   #源单词与目标单词同时增加一个字母，比较这两个字母是否相同，
                                   #选择是复制该字母或是添加目标字母，再删除原字母，记录相应分值
                                   minscore(i - 1, j) + Delete(originalList[i - 1]))
                                   #源单词比目标单词多一个字母，删去该字母，记录分值
            
            if sco == minscore(i, j - 1) + Insert(targetList[j - 1]):
                solution[(i, j)] = solution[(i, j - 1)][:]
                solution[(i, j)].append('insert {0}'.format(targetList[j - 1]))
                #源单词比目标单词少一个字母，添加该字母，记录操作
                
            elif sco == minscore(i - 1, j - 1) + Replace(originalList[i - 1], targetList[j - 1]):
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
                
            MinScore[(i, j)] = sco
            return sco
        
    score = minscore(len(originalList), len(targetList))  #最终分值
    operations = solution[(len(originalList), len(targetList))]  #最终操作，即solution表中的最后一个元素
    return score, operations

# 检验
print("========= 单词最小编辑距离问题 =========")
oplist = [{'copy': 5, 'delete': 20, 'insert': 20},
          {'copy':5, 'delete':10, 'insert':15},
          {'copy':10, 'delete':25, 'insert':20}]
originalWords = ["cane", "sheep", "algorithm", "debug", "difficult", "directory", "wonderful"]
targetWords = ["new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"]

import time
a = time.time()
for i in range(len(oplist)):  #可以同时对三种分值设置进行检验
    for j in range(len(originalWords)):
        score, operations = dpWordEdit(originalWords[j], targetWords[j], oplist[i])
        print(score)
        print(operations)
    print('')
b = time.time()
print('Total time used: %.4fs'%(b-a))  #计时程序

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
