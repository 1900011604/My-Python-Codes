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

'''
----------------------------随机测试样例----------------------------
----------------------------随机测试样例----------------------------
----------------------------随机测试样例----------------------------
'''

#uuid_share#  b2215cc4-9ec0-4c44-b144-b65c061be00c  #
# SESSDSA20 H3 随机测试样例P1

from random import randrange, shuffle, choice
from sys import stderr, stdout
print_bak = globals().get('print_bak', print)  # 使用另行备份的print函数

from collections import Counter


class Node:  # 检测规范调用接口
    invalid_key = Counter()

    def __init__(self, initdata=None):
        self.__data = initdata
        self.__next = None
        self.__prev = None

    for k in ('data', 'next', 'prev'):
        exec(f'''@property
def {k}(self):
    self.invalid_key['get_'+'{k}']+=1
    return getattr(self,'get'+'{k.capitalize()}')()
@{k}.setter
def {k}(self,val):
    self.invalid_key['set_'+'{k}']+=1
    getattr(self,'set'+'{k.capitalize()}')(val)''', globals(), locals())

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def getPrev(self):
        return self.__prev

    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, newnext):
        self.__next = newnext

    def setPrev(self, newprev):
        self.__prev = newprev


# ======= 1 中缀表达式求值 =======
def gen_exp():
    pool = ['@']
    op_expand = randrange(7)
    op_group = randrange(4)
    ops = [''] * op_expand + ['()'] * op_group
    shuffle(ops)

    has_pow = False
    for op in ops:
        tmp = list(i for i, x in enumerate(pool) if x == '@')
        tmp = choice(tmp)
        if op:  # add brackets
            pool.insert(tmp + 1, ')')
            pool.insert(tmp, '(')
            tmp += 1
        # expand expr
        op = '+-*/^' [randrange(5)]
        if op == '^':
            if has_pow:
                op = '+-*/' [randrange(4)]
            else:
                has_pow = True
        pool.insert(tmp + 1, '@')
        pool.insert(tmp + 1, op)

    for i, x in enumerate(pool):
        if x == '@':
            pool[i] = str(randrange(12))

    expr = ' '.join(pool)

    try:  # 有效性检查
        res = eval(expr.replace('^', '**'))
        res1 = eval(expr.replace('/', '//').replace('^', '**'))
        ress = (res, res1)
        assert all(1e-8 < abs(x) < 1e8 and type(x).__name__ != 'complex'
                   and str(x) != 'nan' for x in ress)
        return expr, (res, res1)
    except:
        return gen_exp()


print_bak("======== 1 中缀表达式求值 ========")
try:
    cases = [
        ('114514', (114514, 114514)),
    ]
    for test in range(20):
        res1 = None
        if test < len(cases):
            expr, ress = cases[test]
        else:
            expr, ress = gen_exp()
        res1 = calculate(expr)
        if not any(
                abs((r - res1) / r) < 1e-6 if r else r == res1 for r in ress):
            raise AssertionError('参考答案: %s 或 %s' % ress)
    print_bak('>>> PASS')
except Exception as e:
    print_bak(f'''调用: calculate({repr(expr)})''', file=stderr)
    print_bak(f'输出: {repr(res1)}', file=stderr)
    print_bak(f'{type(e).__name__}: {e}', file=stderr)

# ======= 2 基数排序 =======
print_bak("======== 2 基数排序 ========")
try:
    cases = []
    for test in range(20):
        res1 = None
        if test < len(cases):
            lst = cases[test]
        else:
            lst = [randrange(1000) for i in range(randrange(10, 50))]
        res = sorted(lst)
        res1 = radix_sort(lst[:])
        assert res == res1, f'''参考答案: {res}'''
    print_bak('>>> PASS')
except Exception as e:
    print_bak(f'''调用: radix_sort({repr(lst).replace(' ','')})''', file=stderr)
    print_bak(f'输出: {repr(res1)}', file=stderr)
    print_bak(f'{type(e).__name__}: {e}', file=stderr)

# ======= 3 HTML =======


def gen_xml(make_invalid=False):
    pool = []
    n_pairs = randrange(1, 15)
    from string import ascii_letters, ascii_lowercase
    text_pool = ascii_letters + "0123546789" + ' ' * 50

    for i in range(n_pairs):
        tag = ''.join(choice(ascii_lowercase) for i in range(randrange(1, 5)))
        tmp = randrange(len(pool) + 1)
        pool.insert(tmp, f'</{tag}>')
        pool.insert(tmp, f'<{tag}>')

    if make_invalid:
        for i in range(3):
            if not pool:
                break
            pool.pop(randrange(len(pool)))
    pool.append('</html>')

    res = ['<html>']
    for node in pool:
        res.append(''.join(choice(text_pool) for i in range(randrange(10))))
        res.append(node)

    return ''.join(res)
ref_match=lambda s:(lambda l:not any(map(lambda t:t[1]!=l.pop()[1] if t[0] else l.append(t),__import__('re').findall('<(/?)(.*?)>', s))) and not l)([])

print_bak("======== 3 HTML MATCH ========")
try:
    cases = [
        ('<html></html>', True),
        ('<html>', False),
        ('</html>', False),
    ]
    for test in range(20):
        res1 = None
        if test < len(cases):
            expr, res = cases[test]
        else:
            expr = gen_xml(test % 2)
            res = ref_match(expr)
        res1 = HTMLMatch(expr)
        assert res == res1, f'''参考答案: {res}'''
    print_bak('>>> PASS')
except Exception as e:
    print_bak(f'''调用: HTMLMatch({repr(expr)})''', file=stderr)
    print_bak(f'输出: {repr(res1)}', file=stderr)
    print_bak(f'{type(e).__name__}: {e}', file=stderr)

# SESSDSA20 H3 随机测试样例P2
LINE_WIDTH = 50
N_TESTS = 10
N_OPS = 20

from collections import deque
from random import randrange, choice
from sys import stderr

if 'ref ds':

    class ref_node:
        def __init__(self, lst, ind):
            self.lst = lst
            self.ind = ind

        def getData(self):
            return self.lst[self.ind]

        def getNext(self):
            return ref_node(self.lst, self.ind + 1)

        def getPrev(self):
            return ref_node(self.lst, self.ind - 1)

        def setData(self, newdata):
            self.lst[self.ind] = newdata

        def __eq__(self, other):
            try:
                return self.getData() == other.getData()
            except:
                return False

    ref_node.__str__ = lambda self: 'Node(%r)' % self.getData()
    Node.__str__ = Node.__repr__ = ref_node.__repr__ = ref_node.__str__

    class ref_list:
        isEmpty = lambda self: not self.lst
        add = lambda self, item: self.lst.insert(0, item)
        search = lambda self, item: item in self.lst
        size = __len__ = lambda self: len(self.lst)

        def __init__(self, ref_type, it=None):
            self.ref_type = ref_type
            self.lst = []
            if it:
                for i in it:
                    self.lst.append(i)

        def getTail(self):
            assert self.size() > 0
            return ref_node(self.lst, len(self) - 1)

        def __getitem__(self, arg):
            res = self.lst[arg]
            if isinstance(arg, slice):
                res = ref_list(self.ref_type, res)
            return res

        def __eq__(self, other):
            try:
                if len(self) != len(other):
                    return False
                tmp = [(self[i], other[i]) for i in range(len(self))]
                return all(i == j for i, j in tmp)
            except:
                return False

        __str__ = __repr__ = lambda self: f'{self.ref_type.__name__}({self.lst})'

    class ref_deque(deque):
        push = deque.append
        peek = lambda self: self[-1]
        enqueue = deque.append
        dequeue = deque.popleft
        isEmpty = lambda self: not bool(self)
        size = deque.__len__


def test(i, t_lst, r_lst, op_write, op_read):
    print_bak('TEST #%d' % i, end='')
    _SIZE = 0
    passed = True
    ops = []
    params = []

    def get(param):
        if param == 'num':
            return randrange(N_OPS)
        elif param == 'numstr':
            if randrange(2):
                return randrange(N_OPS)
            return str(randrange(10))
        elif param == 'len':
            return randrange(_SIZE)
        elif param == '-len':
            return randrange(_SIZE) - _SIZE
        elif param == 'slice':
            a = randrange(_SIZE - 1)
            b = randrange(a, _SIZE + 1)
            return slice(a, b, randrange(1, 10))

    def one_check(op):
        ref_exec = True
        op = op.split()

        try:
            params.clear()
            params.extend(map(get, op[1:]))
            r_ref = getattr(r_lst, op[0])(*params)
        except:
            ref_exec = False

        if ref_exec:
            r_test = getattr(t_lst, op[0])(*params)
            if r_ref != None:
                assert r_ref == r_test, '输出: %r;\n应该输出: %r' % (r_test, r_ref)
                if isinstance(r_ref, ref_list):
                    assert type(
                        r_test) == r_ref.ref_type, '输出类型错误: %s;\n应为: %s' % (
                            type(r_test).__name__, r_ref.ref_type.__name__)

            ops.append((op[0], *params))

    def output(op):
        func = op[0]
        params = ','.join(map(repr, op[1:]))
        return '%s(%s)' % (func, params)

    try:
        for i in range(N_OPS):
            # write one
            curr_op = choice(op_write)
            one_check(curr_op)

            # update size
            _SIZE = len(r_lst)

            # read one
            curr_op = choice(op_read)
            one_check(curr_op)

        print_bak(' PASS')
    except Exception as e:
        print_bak('\n出错的操作:', output((curr_op.split()[0], *params)))
        print_bak('历史操作:', ','.join(map(output, ops)))
        print_bak('报错: (%s: %s)' % (type(e).__name__, str(e)), file=stderr)
        try:
            print_bak('LAST LISTS'.center(LINE_WIDTH, '.'))
            print_bak('参考列表:', r_lst)
            print_bak('测试列表:', t_lst)
        except Exception as e:
            print_bak(
                '打印报错 (%s: %s)' % (type(e).__name__, str(e)), file=stderr)
        print_bak('END'.center(LINE_WIDTH, '.'))


def test_code(title, code):
    print_bak(title, end=':\n')
    # print_bak('Code'.center(LINE_WIDTH, '.'))
    # print_bak(code)
    try:
        exec(code, globals())
    except Exception as e:
        print_bak('报错 (%s: %s)' % (type(e).__name__, str(e)), file=stderr)


def prev_iter(lst):
    node = lst.getTail()
    res = []
    for i in range(len(lst)):
        res.append(node.getData())
        node = node.getPrev()
    return res


def safe_iter(lst):
    lst_iter = iter(lst)
    for i in range(len(lst)):
        yield next(lst_iter)
    try:
        not_end = next(lst_iter)
        yield 'NOT END'
    except:
        pass


# push pop peek
print_bak('\n' + "1 LinkStack".center(LINE_WIDTH, '='))
for i in range(N_TESTS):
    test(i, LinkStack(), ref_deque(), (
        'push num',
        'pop',
    ), (
        'isEmpty',
        'peek',
        'size',
    ))

# enqueue dequeue
print_bak('\n' + "2 LinkQueue".center(LINE_WIDTH, '='))
for i in range(N_TESTS):
    test(i, LinkQueue(), ref_deque(), (
        'enqueue num',
        'dequeue',
    ), (
        'isEmpty',
        'size',
    ))

# getTail
print_bak('\n' + "3 DoublyLinkedList".center(LINE_WIDTH, '='))
for i in range(N_TESTS):
    l1 = DoublyLinkedList()
    l2 = ref_list(DoublyLinkedList)
    test(i, l1, l2, (
        'append numstr',
        'add numstr',
        'insert len numstr',
        'pop len',
        'pop',
        'remove numstr',
    ), (
        'isEmpty',
        'search numstr',
        'size',
        '__len__',
        'index numstr',
        '__getitem__ len',
        '__getitem__ slice',
        'getTail',
    ))
    test_code('prev link test', r'''r1=prev_iter(l1)
r2=l2[::-1]
if r1==r2:
    print_bak('PASS')
else:
    print_bak('双链表倒序结果: ',r1,file=stderr)
    print_bak('参考结果: ',r2,file=stderr)''')

comment = '''
注：prev link test用于测试双链表反向连接情况
以上为必做内容，以下为选做内容
'''
try:
    from browser import document
    target = document['py_stdout']
    target.innerHTML += f'<span style="color:blue">{comment}</span>'
except ImportError:
    print_bak(comment, file=stderr)

# Additional


def print_helper(text, cond):
    print_bak(text, end=' ')
    print_bak(cond, file=stdout if cond else stderr)


print_bak('\n' + "Ex DoublyLinkedList".center(LINE_WIDTH, '='))
test_code('__eq__+__iter__ test', '''lst=DoublyLinkedList(range(5))
print_bak('lst:',lst)
print_helper('lst==DoublyLinkedList(range(5)) -> T:',lst==DoublyLinkedList(range(5)))
print_helper('lst!=DoublyLinkedList(range(6)) -> T:',lst!=DoublyLinkedList(range(6)))
print_helper('lst!=list(range(5)) -> T:',lst!=list(range(5)))
print_helper('lst!=None -> T:',lst!=None)
print_helper('lst==DoublyLinkedList(lst) -> T:',lst==DoublyLinkedList(safe_iter(lst)))
mtest=[(x,y) for x in safe_iter(lst) for y in safe_iter(lst)]
print_helper('多iter测试 -> T:',mtest==[(x,y) for x in range(5) for y in range(5)])'''
          )
test_code('-slice test', '''lst='DoublyLinkedList(range(50))'
print_bak('list:',lst)
lst=eval(lst)
all_pass=1
for i in range(20):
    sli=slice(randrange(-100,100),randrange(-100,100),randrange(1,10)*(randrange(2)*2-1))
    l1=list(lst[sli])
    l2=list(range(50)[sli])
    if l1!=l2:
        all_pass=0
        print_bak('FAIL:',sli,l1,l2,file=stderr)
        print_bak('RESULT:',l1,file=stderr)
        print_bak('SHOULD BE:',l2,file=stderr)
if all_pass:
    print_bak('PASS')''')

if Node.invalid_key:
    print_bak('非法调用:', dict(Node.invalid_key), file=stderr)
