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
