class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext
    def setPrev(self, newprev):
        self.prev = newprev

# ======== 5 双链无序表 ========
# 实现双向链表版本的UnorderedList，接口同ADT UnorderedList
# 包含如下方法：isEmpty, add, search, size, remove, append，index，pop，insert, __len__, __getitem__
# 用于列表字符串表示的__str__方法 (注：__str__里不要使用str(), 用repr()代替
# 用于切片的__getitem__方法
# 在节点Node中增加prev变量，引用前一个节点
# 在UnorderedList中增加tail变量与getTail方法，引用列表中最后一个节点
# 选做：DoublyLinkedList(iterable) -> new DoublyLinkedList initialized from iterable's items
# 选做：__eq__, __iter__

class DoublyLinkedList():

    #列表的本质属性和特殊方法

    def __init__(self, rng = None):  #列表的初始化
        self.head = None
        self.tail = None
        if rng is not None:  #rng是迭代器，输入range()参数的时候将其中元素逐个添加入列表
            for i in rng:
                self.append(i)
        
    def size(self):  #返回列表长度
        current = self.head
        i = 0
        while current != None:
            i = i + 1
            current = current.getNext()
        return i

    def __len__(self):  #返回列表长度
        return self.size()

    def getNode(self, index):  #查询列表中某位置对应的元素list[i]本身（即返回一个Node）
                               #这是个内置函数，不是题目要求的接口，但是会在许多接口定义中用到以简化代码
        current = self.head
        if index >= 0:  #i从0开始自左向右计数
            i = 0
            while current != None:
                if i == index:
                    return current
                    break
                else:
                    current = current.getNext()
                    i += 1
        else:  #i从-1开始自右向左计数
            i = 0
            while current != None:
                if i == self.size() + index:
                    return current
                    break
                else:
                    current = current.getNext()
                    i += 1

    def __getitem__(self, index):   #查询列表中某位置对应的元素list[i]的值或切片list[start:stop:step]

        if isinstance(index, int):  #查询列表的某位置对应的元素的值
            return self.getNode(index).getData()

        elif isinstance(index, slice):  #查询列表的切片list[start:stop:step]，返回一个双链无序表
            s = index
            t = DoublyLinkedList()
            n = self.size()

            step = 1 if s.step == None else s.step
            if s.start == None:
                start = 0 if step > 0 else n - 1  #正向搜索时start值默认为首端，反向搜索默认为尾端
            else:
                start = s.start
            if s.stop == None:
                stop = n - 1 if step > 0 else 0  #正向搜索时stop值默认为尾端，反向搜索默认为首端
            else:
                stop = s.stop  #处理没有输入start/stop/step的情况
            
            if start < -n:
                if stop < -n:
                    return t
                elif stop in range (-n, 0):
                    start = -n
                elif stop >= 0:
                    start = 0  #防止迭代过程跨过0
            elif start in range(-n, 0):
                if stop < -n:
                    stop = - n - 1
                elif stop in range(0, n):
                    stop = -n + stop  #start与stop异号，stop由正转负
                elif stop > n:
                    stop = 0
            elif start in range(0, n):
                if stop < -n:
                    stop = -1
                elif stop in range(-n, 0):
                    stop = n + stop  #start与stop异号，stop由负转正
                elif stop > n:
                    stop = n
            elif start >= n:
                if stop < 0:
                    start = -1  #防止迭代过程跨过0
                elif stop in range(0, n):
                    start = n - 1
                elif stop >= n:
                    return t  #处理start/stop越界（即在闭区间[-n, n - 1]以外）或异号的情况

            i = start
            if step > 0:
                while i < stop and self.getNode(i) != None:
                    t.append(self[i])
                    i += step
                return t  #正向搜索
            else:
                while i > stop and self.getNode(i) != None:
                    t.append(self[i])
                    i += step
                return t  #反向搜索

    def isEmpty(self):  #返回列表是否为空
        return self.head == None

    def __eq__(self, another):  #判断一个双链无序表和另一个数据结构是否相等
        if another is None or not isinstance(another, DoublyLinkedList):
            return False
        else:
            if len(self) != len(another):
                return False
            else:
                n = len(self)
                for i in range(n):
                    if self[i] != another[i]:
                        return False
                    else:
                        return True

    def __repr__(self):  #将列表转化为字符串
        if self.isEmpty() == False:
            s = '['
            for i in range(self.size()-1):
                s += '%r, '%(self[i])
            s += '%r]'%(self[-1])  #非空列表
        else:
            s = '[]'  #空列表
        return s

    #与添加元素有关的接口

    def add(self, item):  #在列表的[0]位置（首端）添加元素
        temp = Node(item)
        if self.isEmpty() == False:
            self.head.setPrev(temp)
            temp.setNext(self.head)
            self.head = temp
        else:
            self.head = self.tail = temp

    def append(self, item):  #在列表的[-1]位置（尾端）添加元素
        temp = Node(item)
        if self.isEmpty() == False:
            self.tail.setNext(temp)
            temp.setPrev(self.tail)
            self.tail = temp
        else:
            self.head = self.tail = temp

    def insert(self, index, item):  #在列表的任意指定位置[i]添加元素
        temp = Node(item)
        if index == 0:
            self.add(item)  #添加到第一个元素（用add()实现）
        elif index == -1 or index == self.size():
            self.append(item)  #添加到最后一个元素（用append()实现）
        else:
            temp.setNext(self.getNode(index))
            temp.setPrev(self.getNode(index - 1))
            self.getNode(index - 1).setNext(temp)
            self.getNode(index + 1).setPrev(temp)  #添加到中间某一个元素（需要连接好Prev和Next）

    #与删除元素有关的接口

    def remove(self, item):  #删除从0开始第一个出现的item元素
        i = 0
        n = self.size()
        for i in range(n):
            if self.getNode(i).getData() == item:
                self.pop(i)
                break
            i += 1
            
    def pop(self, i = -1):  #在列表的任意指定位置[i]删除元素，默认在列表的[-1]位置（尾端）删除
        a = self.getNode(i).getData()  #元素i的值
        n = self.size()
        if i == 0:
            self.head = self.getNode(i).getNext()  #删除第一个元素
        elif i == n - 1 or i == -1:
            self.tail = self.getNode(i).getPrev()
            if n == 1:
                self.head = None
            else:
                self.getNode(i - 1).setNext(None)  #删除最后一个元素
        else:
            self.getNode(i - 1).setNext(self.getNode(i + 1))
            self.getNode(i).setPrev(self.getNode(i - 1))  #删除中间某一个元素（需要连接好Prev和Next）
        return a

    #与查找元素有关的接口

    def search(self, item):  #判断列表中是否含有某个元素
        current = self.head
        found = False
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()        
        return found

    def getTail(self):  #查询列表中最后一个节点
        return self.getNode(-1)

    def index(self, item):  #查询列表中某元素的值对应的位置
        n = self.size()
        for i in range(n):
            if self[i] == item:
                return i

# 检验
print("======== 5-DoublyLinkedList ========")
mylist = DoublyLinkedList()
for i in range(0, 20, 2):
    mylist.append(i)
mylist.add(3)
mylist.remove(6)
print(mylist.getTail().getPrev().getData())  # 16
print(mylist.isEmpty())  # False
print(mylist.search(5))  # False
print(mylist.size())  # 10
print(mylist.index(2))  # 2
print(mylist.pop())  # 18
print(mylist.pop(2))  # 2
print(mylist)  # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))  # 9
print(mylist[4])  # 8
print(mylist[3:8:2])  # ['10', 10, 14]
