### 1900011604 张植竣 H3 ###

# ======= 1 中缀表达式求值 =======

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __repr__(self):
        if len(self.items) != 0:
            s='['
            for i in range(len(self.items)-1):
                a=self.items[i]
                s+='%s '%a
            s+='%s'%self.items[len(self.items) - 1]
        else:
            s='['
        return s

def calculate(s) -> float:
    
    def calc(num0, op, num1):  #计算表达式
        if op == '+':
            return num0 + num1
        elif op == '-':
            return num0 - num1
        elif op == '*':
            return num0 * num1
        elif op == '/':
            return num0 / num1  #除法定义为真除
        else:
            return num0 ** num1

    pre = {'^':3, '*':2, '/':2, '+':1, '-':1, '(':0}  #优先级
    opStack, numStack = Stack(), Stack()  #两个栈，opStack储存操作符，numStack储存操作数
    x = s.split()
    n = len(x)

    for i in range(n):
        if x[i] not in '+-*/^()':
            numStack.push(float(x[i]))  #扫描到数字，直接入操作数栈
        elif x[i] == '(':
            opStack.push(x[i])  #扫描到左括号，直接入操作符栈
        elif x[i] == ')':
            op = opStack.pop()
            while op != '(':
                num1 = numStack.pop()
                num0 = numStack.pop()
                ans = calc(num0, op, num1)
                numStack.push(ans)
                op = opStack.pop()  #扫描到右括号，计算括号内表达式直到遇到左括号为止
        else:
            while opStack.size() != 0 and pre[opStack.peek()] >= pre[x[i]]:
                op = opStack.pop()
                num1 = numStack.pop()
                num0 = numStack.pop()
                ans = calc(num0, op, num1)
                numStack.push(ans)
            opStack.push(x[i])  #扫描到操作符，计算表达式直到遇到优先级更低的操作符

    while opStack.size() != 0:
        op = opStack.pop()
        num1 = numStack.pop()
        num0 = numStack.pop()
        ans = calc(num0, op, num1)
        numStack.push(ans)    #如果最后还有操作符（即表达式），继续计算直到得出最终结果

    return numStack.pop()  #最终计算结果

# ======= 2 基数排序 =======

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def radix_sort(s) -> list:
    
    q0, q1, q2, q3, q4, q5 = Queue(), Queue(), Queue(), Queue(), Queue(), Queue()
    q6, q7, q8, q9, main = Queue(), Queue(), Queue(), Queue(), Queue()
    index = {0:q0, 1:q1, 2:q2, 3:q3, 4:q4, 5:q5, 6:q6, 7:q7, 8:q8, 9:q9}  #用字典建立队列与数字的一一映射
    m = max([len(str(i)) for i in s])  #最多的位数
    
    t=[]
    for j in range(m):
        for i in range(len(s)):  #把所有数的位数统一
            t.append(str(s[-1-i]))
            t[i] = t[i].zfill(m)
        for i in range(len(s)):
            main.enqueue(t[-i-1])  #把t中数转成的字符串导入main
        while main.size() != 0:
            i = main.dequeue()
            index[int(i[-1-j])].enqueue(i)  #把main中数转成的字符串导入q0~q9
        for i in range(10):
            while index[i].size() != 0:
                main.enqueue(index[i].dequeue())  #把q0~q9中数导入main
        s, t=[], []
        for i in range(main.size()):
            s.append(main.dequeue())
    for i in range(len(s)):
        s[i] = int(s[i])
    return s  #显示排序后结果

# ======= 3 HTML标记匹配 =======

def HTMLMatch(s) -> bool:
    
    import re
    
    def close(s):  #将s中开标记<tag>部分转化为闭标记</tag>
        t = list(s)  #将字符串拆解转化为列表
        t.insert(1,'/')  #插入“/”，转化为闭标记
        i = 0
        b = ''
        while t[i] != '>':
            b += t[i]
            i += 1
        b += t[i]
        return b  #将列表重新合并转化为字符串
            
    def match(i, j):  #判断两个字符串是否匹配，若匹配则返回True
        return re.findall('<[^/].*>', i) != [] and re.findall(close(i), j) != []

    def Match_pop():  #两个字符串匹配且两个表都不空（防止从空栈移除报错）则可以移除出栈
        if a.isEmpty() == False and b.isEmpty() == False and match(a.peek(), b.peek()) == True:
            b.pop()
            return True
        else:
            return False
            
    a, b = Stack(), Stack()
    j = 0
    s = s.replace(' ','')  #删去所有空格
    
    for i in range(len(s)):
        if s[i] == '<':  #遇到'<'开始截取
            for j in range(i,len(s)):
                if s[j] == '>':  #遇到'<'结束截取
                    a.push(s[i:j+1])
                    break  #截取s中的<tag>部分
                
    while a.isEmpty() == False:
        b.push(a.pop())
        while Match_pop() == True:
            a.pop()  #匹配成功，可以移除出栈

    if b.isEmpty() == True:
        return True  
    else:
        return False  #最后应该将b清空，否则HTML匹配失败，返回False

# ======== 4 5 双向节点 ========

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

# ======== 4 链表实现栈和队列 ========

class LinkStack():  #链表实现栈
    
    def __init__(self):  #栈的初始化
        self.head = None
    
    def isEmpty(self):  #判断栈是否为空
        return self.head == None
    
    def push(self, item):  #压入栈顶（以head一端为栈顶）
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def pop(self):  #从栈顶弹出（以head一端为栈顶）
        a = self.head.getData()
        self.head = self.head.getNext()
        return a
    
    def peek(self):  #返回栈顶元素的值
        if self.isEmpty() == False:
            return self.head.getData()
        else:
            return None
    
    def size(self):  #返回栈内元素个数
        current = self.head
        i = 0
        while current != None:
            i += 1
            current = current.getNext()
        return i

class LinkQueue():  #链表实现队列
    
    def __init__(self):  #队列的初始化
        self.head = None

    def isEmpty(self):  #判断队列是否为空
        return self.head == None
    
    def enqueue(self, item):  #从队首加入（以head一端为队首）
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp  

    def dequeue(self):  #从队尾移除
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()  #用previous和current两个追踪器扫描整条队尾
        a = current.getData()  #队尾元素的值

        if previous != None:
            previous.setNext(current.getNext())  #队列长度大于1时，previous的Next值跨过current
        else:
            self.head = current.getNext()  #队列长度为1时，移除队尾元素则变成空队列，调整head即可
        return a

    def size(self):  #返回队列内元素个数
        current = self.head
        i = 0
        while current != None:
            i = i + 1
            current = current.getNext()
        return i

# ======== 5 双链无序表 ========

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
