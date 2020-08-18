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
