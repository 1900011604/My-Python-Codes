#uuid_share#  4e746bfe-8d2d-42ca-af59-cb654a86adee  #
# SESSDSA20课程上机作业
# 【H3】栈与队列编程作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的*函数体内*编写代码，每个题目的函数后有调用语句用于检验
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业在3月18日18:00之前提交到PyLn编程学习系统，班级码见Canvas系统


# ======= 1 中缀表达式求值 =======
# 通过把“中缀转后缀”和“后缀求值”两个算法功能集成在一起（非简单的顺序调用），
# 实现对中缀表达式直接求值，新算法还是从左到右扫描中缀表达式，
# 但同时使用两个栈，一个暂存操作符，一个暂存操作数，来进行求值。
#
# 创建一个函数，接受参数为一个字符串，即一个中缀表达式，
# 其中每个数字或符号间由一个空格隔开；
# 返回一个浮点数，即求值的结果。（支持 + - * / ^ 五种运算）
#   其中“ / ”定义为真除True DIV，结果是浮点数类型
# 输入样例1：
# ( 2 + 3 ) * 6 + 4 / 2
# 输出样例1：
# 32.0
# 输入样例2：
# 2 ^ 3 + 4 * 5 - 16 / 2
# 输出样例2：
# 20.0
# 输入样例3：
# ( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6
# 输出样例3：
# 1.0

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

# 调用检验
print("======== 1-calculate ========")
print(calculate("( 2 + 3 ) * 6 + 4 / 2"))
print(calculate("2 ^ 3 + 4 * 5 - 16 / 2"))
print(calculate("( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6"))

# ======= 2 基数排序 =======
# 实现一个基数排序算法，用于10进制的正整数从小到大的排序。
#
# 思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
# 第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第三趟放百位，再合并；第四趟放千位，再合并。
# 直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。
#
# 创建一个函数，接受参数为一个列表，为需要排序的一系列正整数，
# 返回排序后的数字列表。
# 输入样例1：
# [1, 2, 4, 3, 5]
# 输出样例1：
# [1, 2, 3, 4, 5]
# 输入样例2：
# [8, 91, 34, 22, 65, 30, 4, 55, 18]
# 输出样例2：
# [4, 8, 18, 22, 30, 34, 55, 65, 91]


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


# 调用检验
print("======== 2-radix_sort ========")
print(radix_sort([1, 2, 4, 3, 5]))
print(radix_sort([8, 91, 34, 22, 65, 30, 4, 55, 18]))

# ======= 3 HTML标记匹配 =======
# 实现扩展括号匹配算法，用来检查HTML文档的标记是否匹配。
# HTML标记应该成对、嵌套出现，
# 开标记是<tag>这种形式，闭标记是</tag>这种形式。
#
# 创建一个函数，接受参数为一个字符串，为一个HTML文档中的内容，
# 返回True或False，表示该字符串中的标记是否匹配。
# 输入样例1：
# <html> <head> <title> Example </title> </head> <body> <h1>Hello, world</h1> </body> </html>
# 输出样例1：
# True
# 输入样例2：
# <html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>
# 输出样例2：
# False


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



# 调用检验
print("======== 3-HTMLMatch ========")
print(
    HTMLMatch(
        "<html> <head> <title>Example</title> </head> <body> <h1>Hello, world</h1> </body> </html>"
    ))
print(
    HTMLMatch(
        "<html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>"
    ))


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
# 用链表实现ADT Stack与ADT Queue的所有接口

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

# 检验
print("======== 4-Link Stack & Link Queue ========")
s = LinkStack()
q = LinkQueue()
for i in range(10):
    s.push(i)
    q.enqueue(i)
print(s.peek(), q.dequeue())  # 9 0
print(s.pop(), q.size())  # 9 9
while not s.isEmpty():
    s.pop()
print(s.size(), q.isEmpty())  # 0 False


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
