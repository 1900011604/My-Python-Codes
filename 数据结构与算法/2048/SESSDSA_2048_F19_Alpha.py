class Player:
    def __init__(self,isFirst,array):
        self.isFirst = isFirst
        self.array = array

    #主函数
    def output(self,currentRound,board,mode):
        if mode == 'position':
            return self.addHelper(board,currentRound)
        elif mode == 'direction':
            return self.moveHelper(board,currentRound)
    
    #落子
    def addHelper(self,board,currentRound):
        another = board.getNext(self.isFirst,currentRound)
        available = board.getNone(not self.isFirst)
        #获取所有可落子位置
        if another != ():
            available.append(another)
        initMyScore = self._sumMyScore(board)
        initOpScore = self._sumOpScore(board)
        #搜索落子后在对方走一步的情况下（不计先后都让对方走）我方可获得的最大收益
        d = {}
        for loc in available:
            copy1 = board.copy()
            copy1.add(self.isFirst,loc)
            lst = [0 for i in range(4)]
            for i in range(4):
                copy2 = copy1.copy()
                copy2.move(not self.isFirst,i)
                #采用普通的估值函数，如果采用加权的反而会出问题，不停在对面下
                lst[i] = self._sumOpScore(copy2) - initOpScore -\
                         (self._sumMyScore(copy2) - initMyScore)
            d[loc] = max(lst)
        return min(d,key=d.get)
    
    #移动
    def moveHelper(self,board,currentRound):
        if not self.easyCanMove(board,'me'):
            return None
        #前三十轮采用增值较快的贪心算法，只搜索两层
        elif currentRound < 30:
            initMyScore = self._sumMyScore(board)
            lst = [[0 for j in range(4)] for i in range(4)]
            for i in range(4):
                copy1 = board.copy()
                if copy1.move(self.isFirst,i):
                    for j in range(4):
                        copy2 = copy1.copy()
                        copy2.move(not self.isFirst,j)
                        lst[i][j] = self._sumMyScore(copy2) - initMyScore
                else:
                    for j in range(4):
                        lst[i][j] = -256*1024**2
                lst[i] = min(lst[i])
            return lst.index(max(lst))
        #采用三层的minimax搜索树
        else:
            initMyScore = self.sumMyScore(board)
            initOpScore = self.sumOpScore(board)
            lst = [[[0 for k in range(4)] for j in range(4)] for i in range(4)]
            mylst = [[[0 for k in range(4)] for j in range(4)] for i in range(4)]
            #在最后两轮为了防止报错不考虑落子，在时间不够的情况下也不考虑落子
            if currentRound >= 498 or board.getTime(self.isFirst)<1:
                for i in range(4):
                    copy1 = board.copy()
                    if copy1.move(self.isFirst,i):
                        for j in range(4):
                            copy2 = copy1.copy()
                            copy2.move(not self.isFirst,j)
                            for k in range(4):
                                copy3 = copy2.copy()
                                copy3.move(self.isFirst,k)
                                #采用专门设定的估值函数
                                lst[i][j][k] = self.sumMyScore(copy3) - initMyScore -\
                                               (self.sumOpScore(copy3) - initOpScore)
                                mylst[i][j][k] = self.sumMyScore(copy3) - initMyScore
                    else:
                        for j in range(4):
                            for k in range(4):
                                lst[i][j][k] = -256*1024**2
                                mylst[i][j][k] = -256*1024**2
            #正常情况下考虑落子
            else:
                if self.isFirst:
                    for i in range(4):
                        copy1 = board.copy()
                        if copy1.move(self.isFirst,i):
                            for j in range(4):
                                copy2 = copy1.copy()
                                copy2.move(not self.isFirst,j)
                                copy2.add(self.isFirst,self.addHelper(copy2,currentRound+1))
                                for k in range(4):
                                    copy3 = copy2.copy()
                                    copy3.move(self.isFirst,k)
                                    lst[i][j][k] = self.sumMyScore(copy3) - initMyScore -\
                                                   (self.sumOpScore(copy3) - initOpScore)
                                    mylst[i][j][k] = self.sumMyScore(copy3) - initMyScore
                        else:
                            for j in range(4):
                                for k in range(4):
                                    lst[i][j][k] = -256*1024**2
                                    mylst[i][j][k] = -256*1024**2
                else:
                    for i in range(4):
                        copy1 = board.copy()
                        if copy1.move(self.isFirst,i):
                            copy1.add(self.isFirst,self.addHelper(copy1,currentRound+1))
                            for j in range(4):
                                copy2 = copy1.copy()
                                copy2.move(not self.isFirst,j)
                                for k in range(4):
                                    copy3 = copy2.copy()
                                    copy3.move(self.isFirst,k)
                                    lst[i][j][k] = self.sumMyScore(copy3) - initMyScore -\
                                                   (self.sumOpScore(copy3) - initOpScore)
                                    mylst[i][j][k] = self.sumMyScore(copy3) - initMyScore
                        else:    
                            for j in range(4):
                                for k in range(4):
                                    lst[i][j][k] = -256*1024**2
                                    mylst[i][j][k] = -256*1024**2
            for i in range(4):
                for j in range(4):
                    lst[i][j] = max(lst[i][j])
                    mylst[i][j] = max(mylst[i][j])
                lst[i] = min(lst[i])
                mylst[i] = min(mylst[i])
            #设定防撤回功能，以免陷入局部最优丧失优势局面
            #但如果不撤回损失太大还是得撤回
            if self.getBoarder(board):
                i = 2 if self.isFirst else 3
                if lst[i] != -256*1024**2:
                    lst[i] -= 64*1024**2
                    mylst[i] -= 64*1024**2
                    if max(mylst)<0:
                        lst[i] += 64*1024**2
            return lst.index(max(lst))
        
    #加权算分
    #估值函数采用对方分数比己方多数倍的形式，增强侵略性，便于控场
    #曾经采用过己方靠边界数层也分数稍高的形式
    #但反而破坏了正常的搜索功能，有副作用，取消
    def sumMyScore(self,board):
        sums = 0
        for n in range(8):
            weight = self.weight(n,self.isFirst)
            for m in range(4):
                if board.getBelong((m,n)) == self.isFirst:
                    a = weight*4**board.getValue((m,n))
                    sums += a
        return sums

    def sumOpScore(self,board):
        sums = 0
        for n in range(8):
            weight = self.weight(n,not self.isFirst)
            for m in range(4):
                if board.getBelong((m,n)) != self.isFirst:
                    a = weight*4**board.getValue((m,n))
                    sums += a
        return sums

    #权重函数，尝试多种形式后采用此种
    def weight(self,n,p):
        if p:
            if n > 3:
                return 3
            else:
                return 1
        else:
            if n < 4:
                return 3
            else:
                return 1
            
    #算分
    #正常的不加权算分，特殊情况下使用
    def _sumMyScore(self,board):
        lst = board.getScore(self.isFirst)
        sums = 0
        for rank in lst:
            sums += 4**rank
        return sums
    
    def _sumOpScore(self,board):
        lst = board.getScore(not self.isFirst)
        sums = 0
        for rank in lst:
            sums += 4**rank
        return sums
    
    #判断能否移动
    def easyCanMove(self,board,belong):
        if belong == 'me':
            for i in range(4):
                copy = board.copy()
                if copy.move(self.isFirst,i):
                    return i+1
        if belong == 'op':
            for i in range(4):
                copy = board.copy()
                if copy.move(not self.isFirst,i):
                    return i+1

    #得到边线归属
    #防撤回功能的辅助函数
    def getBoarder(self,board):
        boarder = False
        i = 4 if self.isFirst else 3
        for j in range(4):
            if board.getBelong((j,i)) == self.isFirst:
                boarder = True
                break
        return boarder

    #以下为部分试过但最终未采用的功能
    
    #连招，尝试使用某种战法，构建一种“局势”，避免陷入局部最优
    #曾是算分函数的辅助函数
    #但因没什么用放弃
    '''def getTheSame(self,board,m,n):
        num = 0
        if n-1 >= 0 and board.getBelong((m,n-1))==self.isFirst\
           and board.getValue((m,n-1))==board.getValue((m,n)):
            num += 1
        if n+1 <= 3 and board.getBelong((m,n+1))==self.isFirst\
           and board.getValue((m,n+1))==board.getValue((m,n)):
            num += 1
        return num'''

    #得到周围一圈是否有对方2，本为辅助添子堵对方的函数使用
    '''def getAround(self,board,m,n):
        if m-1 >= 0 and board.getBelong((m-1,n)) != self.isFirst\
        and (board.getValue((m-1,n)) == 1 or board.getValue((m-1,n)) == 0):
            return True
        if m+1 <= 3 and board.getBelong((m+1,n)) != self.isFirst\
        and (board.getValue((m+1,n)) == 1 or board.getValue((m+1,n)) == 0):
            return True
        delta = 1 if self.isFirst else -1
        if board.getBelong((m,n+delta)) != self.isFirst\
        and (board.getValue((m,n+delta)) == 1 or board.getValue((m,n+delta)) == 0):
            return True
        return False'''

    #移动函数的一部分，带alpha-beta剪枝的五层搜索
    #效果并没有想象中那么好，并且耗时过多
    def moveHelper2(self,board,currentRound):
        if not self.easyCanMove(board,'me'):
            return None
        elif currentRound<50:
            initMyScore = self._sumMyScore(board)
            initOpScore = self._sumOpScore(board)
            #剪枝搜索,普通赋分
            lst = [[[[[256*1024**2 for m in range(4)] for l in range(4)] for k in range(4)]\
                    for j in range(4)] for i in range(4)]
            #根节点下界
            inf0 = -256*1024**2
            for i in range(4):
                #第一层上界
                sup1 = 256*1024**2
                copy1 = board.copy()
                if copy1.move(self.isFirst,i):
                    for j in range(4):
                        #第二层下界
                        inf2 = -256*1024**2
                        copy2 = copy1.copy()
                        copy2.move(not self.isFirst,j)
                        for k in range(4):
                            #第三层上界
                            sup3 = 256*1024**2
                            copy3 = copy2.copy()
                            copy3.move(self.isFirst,k)
                            for l in range(4):
                                copy4 = copy3.copy()
                                copy4.move(not self.isFirst,l)
                                for m in range(4):
                                    copy5 = copy4.copy()
                                    copy5.move(self.isFirst,m)
                                    #计算收益
                                    lst[i][j][k][l][m] = self._sumMyScore(copy5) - initMyScore \
                                    - self._sumOpScore(copy5) + initOpScore
                                    #如果无必要继续搜索，剪枝
                                    if lst[i][j][k][l][m] > sup3:
                                        lst[i][j][k][l] = lst[i][j][k][l][m]
                                        break
                                #取叶节点最大值
                                if isinstance(lst[i][j][k][l],list):
                                    lst[i][j][k][l] = max(lst[i][j][k][l])
                                #重设上界
                                if sup3 > lst[i][j][k][l]:
                                    sup3 = lst[i][j][k][l]
                                #剪枝
                                if lst[i][j][k][l] < inf2:
                                    lst[i][j][k] = lst[i][j][k][l]
                                    break
                            #取下层节点最小值，重设下界，剪枝，下同
                            if isinstance(lst[i][j][k],list):
                                lst[i][j][k] = min(lst[i][j][k])
                            if inf2 < lst[i][j][k]:
                                inf2 = lst[i][j][k]
                            if lst[i][j][k] > sup1:    
                                lst[i][j] = lst[i][j][k]
                                break
                        #同上
                        if isinstance(lst[i][j],list):
                            lst[i][j] = max(lst[i][j])
                        if sup1 > lst[i][j]:
                            sup1 = lst[i][j]
                        if inf0 > lst[i][j]:    
                            lst[i] = lst[i][j]
                            break
                    #取下层节点最小值，重设下界
                    if isinstance(lst[i],list):
                        lst[i] = min(lst[i])
                    if inf0 < lst[i]:
                        inf0 = lst[i]
                else:
                    lst[i] = -256*1024**2
            #防撤回
            if currentRound>100 and self.getBoarder(board):
                i = 2 if self.isFirst else 3
                if lst[i] != -256*1024**2:
                    lst[i] -= 64*1024**2
                    if max(lst)<-64**2:
                        lst[i] += 64*1024**2
            #根节点取最大值
            return lst.index(max(lst))
        elif currentRound < 125:
            initMyScore = self.sumMyScore(board)
            initOpScore = self.sumOpScore(board)
            #剪枝搜索，加权赋分
            lst = [[[[[256*1024**2 for m in range(4)] for l in range(4)] for k in range(4)]\
                    for j in range(4)] for i in range(4)]
            #根节点下界
            inf0 = -256*1024**2
            for i in range(4):
                #第一层上界
                sup1 = 256*1024**2
                copy1 = board.copy()
                if copy1.move(self.isFirst,i):
                    for j in range(4):
                        #第二层下界
                        inf2 = -256*1024**2
                        copy2 = copy1.copy()
                        copy2.move(not self.isFirst,j)
                        for k in range(4):
                            #第三层上界
                            sup3 = 256*1024**2
                            copy3 = copy2.copy()
                            copy3.move(self.isFirst,k)
                            for l in range(4):
                                copy4 = copy3.copy()
                                copy4.move(not self.isFirst,l)
                                for m in range(4):
                                    copy5 = copy4.copy()
                                    copy5.move(self.isFirst,m)
                                    #计算收益
                                    lst[i][j][k][l][m] = self.sumMyScore(copy5) - initMyScore \
                                    - self.sumOpScore(copy5) + initOpScore
                                    #如果无必要继续搜索，剪枝
                                    if lst[i][j][k][l][m] > sup3:
                                        lst[i][j][k][l] = lst[i][j][k][l][m]
                                        break
                                #取叶节点最大值
                                if isinstance(lst[i][j][k][l],list):
                                    lst[i][j][k][l] = max(lst[i][j][k][l])
                                #重设上界
                                if sup3 > lst[i][j][k][l]:
                                    sup3 = lst[i][j][k][l]
                                #剪枝
                                if lst[i][j][k][l] < inf2:
                                    lst[i][j][k] = lst[i][j][k][l]
                                    break
                            #取下层节点最小值，重设下界，剪枝，下同
                            if isinstance(lst[i][j][k],list):
                                lst[i][j][k] = min(lst[i][j][k])
                            if inf2 < lst[i][j][k]:
                                inf2 = lst[i][j][k]
                            if lst[i][j][k] > sup1:    
                                lst[i][j] = lst[i][j][k]
                                break
                        #同上
                        if isinstance(lst[i][j],list):
                            lst[i][j] = max(lst[i][j])
                        if sup1 > lst[i][j]:
                            sup1 = lst[i][j]
                        if inf0 > lst[i][j]:    
                            lst[i] = lst[i][j]
                            break
                    #取下层节点最小值，重设下界
                    if isinstance(lst[i],list):
                        lst[i] = min(lst[i])
                    if inf0 < lst[i]:
                        inf0 = lst[i]
                else:
                    lst[i] = -256*1024**2
            #防撤回
            if currentRound>100 and self.getBoarder(board):
                i = 2 if self.isFirst else 3
                if lst[i] != -256*1024**2:
                    lst[i] -= 64*1024**2
                    if max(lst)<-64**2:
                        lst[i] += 64*1024**2
            #根节点取最大值
            return lst.index(max(lst))
        else:
            initMyScore = self.sumMyScore(board)
            initOpScore = self.sumOpScore(board)
            #普通三层搜索
            lst = [[[0 for k in range(4)] for j in range(4)] for i in range(4)]
            for i in range(4):
                copy1 = board.copy()
                if copy1.move(self.isFirst,i):
                    for j in range(4):
                        copy2 = copy1.copy()
                        copy2.move(not self.isFirst,j)
                        for k in range(4):
                            copy3 = copy2.copy()
                            copy3.move(self.isFirst,k)
                            lst[i][j][k] = self.sumMyScore(copy3) - initMyScore -\
                                           (self.sumOpScore(copy3) - initOpScore)
                else:
                    for j in range(4):
                        for k in range(4):
                            lst[i][j][k] = -256*1024**2
            for i in range(4):
                for j in range(4):
                    lst[i][j] = max(lst[i][j])
                lst[i] = min(lst[i])
            if self.getBoarder(board):
                i = 2 if self.isFirst else 3
                if lst[i] != -256*1024**2:
                    lst[i] -= 64*1024**2
                    if max(lst)<-64**2:
                        lst[i] += 64*1024**2
            return lst.index(max(lst))

    #带alpha-beta剪枝的四层搜索，效果并没有想象中那么好
    lst = [[[[256*1024**2 for l in range(4)] for k in range(4)]\
                for j in range(4)] for i in range(4)]
    #根节点下界
    inf0 = -256*1024**2
    for i in range(4):
        #第一层上界
        sup1 = 256*1024**2
        copy1 = board.copy()
        if copy1.move(self.isFirst,i):
            for j in range(4):
                #第二层下界
                inf2 = -256*1024**2
                copy2 = copy1.copy()
                copy2.move(not self.isFirst,j)
                for k in range(4):
                    copy3 = copy2.copy()
                    copy3.move(self.isFirst,k)
                    for l in range(4):
                        copy4 = copy3.copy()
                        copy4.move(not self.isFirst,l)
                        #计算收益
                        lst[i][j][k][l] = self._sumMyScore(copy) - initMyScore \
                                          - self._sumOpScore(copy) + initOpScore
                        #如无必要继续搜索，剪枝
                        if lst[i][j][k][l] < inf2:
                            lst[i][j][k] = lst[i][j][k][l]
                            break
                    #取叶节点最小值
                    if isinstance(lst[i][j][k],list):
                        lst[i][j][k] = min(lst[i][j][k])
                    #重设下界
                    if inf2 < lst[i][j][k]:
                        inf2 = lst[i][j][k]
                    #剪枝
                    if lst[i][j][k] > sup1:    
                        lst[i][j] = lst[i][j][k]
                        break
                #取下层最大值，重设上界，剪枝
                if isinstance(lst[i][j],list):
                    lst[i][j] = max(lst[i][j])
                if sup1 > lst[i][j]:
                    sup1 = lst[i][j]
                if inf0 > lst[i][j]:    
                    lst[i] = lst[i][j]
                    break
            #取下层最小值，重设下界
            if isinstance(lst[i],list):
                lst[i] = min(lst[i])
            if inf0 < lst[i]:
                inf0 = lst[i]
        else:
            lst[i] = -256*1024**2
    #根节点取最大值
    return lst.index(max(lst))
