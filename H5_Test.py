#uuid_share# 2ab430a7-276d-4893-85d0-38d92bc77a65 #
# SESSDSA20课程上机作业
# 【H5】AVL树作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中指定部位编写代码
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业代码部分在4月29日18:00之前提交到PyLn编程学习系统，班级码见Canvas系统

# ---- 用AVL树实现字典类型 ----
# 用AVL树来实现字典类型，使得其put/get/in/del操作均达到对数性能
# 采用如下的类定义，至少实现下列的方法
# key至少支持整数、浮点数、字符串
# 请调用hash(key)来作为AVL树的节点key
# 【注意】涉及到输出的__str__, keys, values这些方法的输出次序是AVL树中序遍历次序
#    也就是按照hash(key)来排序的，这个跟Python 3.7中的dict输出次序不一样。


'''
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    二叉树结点
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''


class TreeNode:

    def __init__(self, key, val=None, L=None, R=None, P=None, B=0):  # 初始化方法
        self.k = key    # k = key
        self.v = val    # v = value
        self.L = L      # L = LeftChild
        self.R = R      # R = RightChild
        self.P = P      # P = Parent
        self.B = B      # B = BalanceFactor

    def getLeft(self):  # 获取左子树 (不存在时返回None)
        if self.L:
            return self.L
        else:
            return None

    def getRight(self):  # 获取右子树 (不存在时返回None)
        if self.R:
            return self.R
        else:
            return None

    def isLeft(self):   # 判断是否为父节点的左节点
        return self.P and self.P.L == self

    def isRight(self):  # 判断是否为父节点的右节点
        return self.P and self.P.R == self

    def isRoot(self):   # 判断是否为根节点
        return not self.P

    def height(self):
        # 计算以该节点为根节点的子树高度，若只有一个根节点，则高度为1
        def _height(t):
            if not t:
                return 0
            return 1 + max(_height(t.L), _height(t.R))
        return _height(self)

    def __iter__(self):
        if self:
            if self.L:
                for elements in self.L:
                    yield elements
            yield self.k
            if self.R:
                for elements in self.R:
                    yield elements

    def replace(self, key, val, left, right):
        # 把它的key、value、左子节点、右子节点都更换一遍
        self.k = key
        self.v = val
        self.L = left
        self.R = right
        if self.L:
            self.L.P = self
        if self.R:
            self.R.P = self

    def findNext(self):     # 寻找后继
        def findMin(self):  # 向（被删除节点右子树的）左下角
            current = self
            while current.getLeft():
                current = current.L
            return current  # 这个后继本身是叶节点，或仅有一个右子树
        next = None
        if self.getRight():     # 被删除节点有右子树
            next = findMin(self.R)  # 注意这里已经是self.R，往右下角开始
        else:   # 没有右子树
            if self.P:
                if self.isLeft():
                    next = self.P   # 向右上方找（self是其父节点的左子节点）
                else:   # self是其父节点的右子节点
                    self.P.R = None
                    next = self.P.findNext()
                    self.P.R = self  # 跳过self找另一条支路（父节点的左子树）
        return next

    def out(self):  # 删除某节点
        if not (self.L or self.R):  # 叶节点，结束递归，直接删除（赋值为None）
            if self.isLeft():
                self.P.L = None
            else:
                self.P.R = None
        elif self.L or self.R:      # 非叶节点，继续
            if self.getLeft():
                if self.isLeft():
                    self.P.L = self.L   # self是左节点，且自己有左节点
                else:
                    self.P.R = self.L   # self是右节点，且自己有左节点
                self.L.P = self.P
            else:     # 自己有右子树，删除
                if self.isLeft():
                    self.P.L = self.R   # self是左节点，且自己有右节点
                else:
                    self.P.R = self.R   # self是右节点，且自己有右节点
                self.R.P = self.P


'''
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    AVL树的实现
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''


class mydict:

    def __init__(self):  # 字典的初始化
        self.root = None    # 这里定义了树的根节点
        self.size = 0

    def getRoot(self):  # 返回AVL树内部根节点
        return self.root

    '''# 下面三个函数共同完成__setitem__()函数
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#'''

    def __setitem__(self, key, value):  # 加入某个元素
        self.put(key, value)

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, node):
        if hash(key) < hash(node.k):
            if node.L:  # node有左子树
                self._put(key, val, node.L)     # _put到左子树（向左下递归）
            else:
                node.L = TreeNode(key, val, P=node)     # node没有左子树，递归结束，成为左子树
                self.updateBalance1(node.L)      # 更新平衡因子
        elif hash(key) > hash(node.k):
            if node.R:  # node有右子树
                self._put(key, val, node.R)     # _put到右子树（向右下递归）
            else:
                node.R = TreeNode(key, val, P=node)     # node没有右子树，递归结束，成为右子树
                self.updateBalance1(node.R)      # 更新平衡因子
        elif hash(key) == hash(node.k):
            node.v = val
            self.size -= 1  # 避免self.size重复计算，put()方法最后一行 += 1 和本行 -= 1 抵消

    def updateBalance1(self, node):     # __setitem__()函数中更新平衡因子
        if node.B > 1 or node.B < -1:   # 平衡因子越界，需要重新平衡
            self.rebalance(node)
            return
        if node.P != None:
            if node.isLeft():
                node.P.B += 1
            elif node.isRight():
                node.P.B -= 1
            if node.P.B != 0:  # 如果不等于0
                self.updateBalance1(node.P)  # 向上递归
    '''#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#'''

    '''# 下面三个函数共同完成__getitem__()函数
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#'''

    def __getitem__(self, key):     # 查找某个元素
        return self._get(key, self.root).v  # 输出元素的value

    def _get(self, key, node):
        if not node:
            raise KeyError(key)  # 没有找到该节点，报错
        elif hash(key) == hash(node.k):
            return node
        elif hash(key) < hash(node.k):
            return self._get(key, node.L)   # 向左子树递归
        else:
            return self._get(key, node.R)   # 向右子树递归
    '''#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#'''

    '''# 下面四个函数共同完成__delitem__()函数
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#'''

    def __delitem__(self, key):     # 删除某个元素
        self.delete(key)

    def delete(self, key):
        if self.size > 1:
            delnode = self._get(key, self.root)
            if delnode:
                self.remove(delnode)    # 删除元素
                self.size -= 1
            else:
                raise KeyError(key)
        elif self.size == 1 and self.root.k == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError(key)

    def remove(self, node):
        if not (node.L or node.R):  # 没有子节点
            self.updateBalance2(node)
            if node.isLeft():
                node.P.L = None
            else:
                node.P.R = None
        elif node.L and node.R:     # 有两个子节点
            next = node.findNext()  # 寻找后继
            self.updateBalance2(next)
            next.out()  # 后继移出
            node.k = next.k
            node.v = next.v
        else:  # 有一个子节点
            '''
            左左节点：被删节点是其父节点的左子节点，它自己也有一个左子节点
            左右节点：被删节点是其父节点的左子节点，它自己有一个右子节点
            右左节点：被删节点是其父节点的右子节点，它自己有一个左子节点
            右右节点：被删节点是其父节点的右子节点，它自己也有一个右子节点
            '''
            self.updateBalance2(node)
            if node.getLeft():  # 被删节点有左子节点
                if node.isLeft():       # 左左节点删除
                    node.L.P = node.P
                    node.P.L = node.L
                elif node.isRight():    # 右左节点删除
                    node.L.P = node.P
                    node.P.R = node.L
                else:
                    node.replace(node.L.k, node.L.v, node.L.L, node.L.R)
            else:   # 被删节点有右子节点
                if node.isLeft():       # 左右节点删除
                    node.R.P = node.P
                    node.P.L = node.R
                elif node.isRight():    # 右右节点删除
                    node.R.P = node.P
                    node.P.R = node.R
                else:
                    node.replace(node.R.k, node.R.v, node.R.L, node.R.R)

    def updateBalance2(self, node):  # __delitem__()函数中更新平衡因子
        if node.B > 1 or node.B < -1:   # 平衡因子越界，需要重新平衡
            self.rebalance(node)
            # 重新平衡后若平衡因子变为0，影响继续向上传播
            if node.P.B == 0:
                self.updateBalance2(node.P)
        elif node.P != None:
            if node.isLeft():
                node.P.B -= 1
            elif node.isRight():
                node.P.B += 1
            # 递归，结束条件为根节点或某节点的父节点平衡因子由0变为±1
            if node.P.B != 1 and node.P.B != -1:  # 如果不是1也不是-1
                self.updateBalance2(node.P)  # 向上递归
        elif node.P == None:    # node为根节点，且为唯一节点
            node.B = 0
    '''#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#'''

    '''# 下面三个函数共同完成旋转再平衡函数
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#'''

    def rebalance(self, node):
        if node.B < 0:  # 右重需要左旋
            if node.R.B > 0:    # 右子节点左重，先右旋
                self.rotR(node.R)
                self.rotL(node)
            else:   # 直接左旋
                self.rotL(node)
        elif node.B > 0:  # 左重需要右旋
            if node.L.B < 0:    # 左子节点右重，先左旋
                self.rotL(node.L)
                self.rotR(node)
            else:   # 直接右旋
                self.rotR(node)

    def rotL(self, rotRoot):    # 向左旋转
        newRoot = rotRoot.R
        rotRoot.R = newRoot.L
        if newRoot.L != None:
            newRoot.L.P = rotRoot
        newRoot.P = rotRoot.P
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeft():
                rotRoot.P.L = newRoot
            else:
                rotRoot.P.R = newRoot
        newRoot.L = rotRoot
        rotRoot.P = newRoot
        rotRoot.B = rotRoot.B + 1 - min(newRoot.B, 0)  # 更新平衡因子
        newRoot.B = newRoot.B + 1 + max(rotRoot.B, 0)  # 更新平衡因子

    def rotR(self, rotRoot):    # 向右旋转
        newRoot = rotRoot.L
        rotRoot.L = newRoot.R
        if newRoot.R != None:
            newRoot.R.P = rotRoot
        newRoot.P = rotRoot.P
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRight():
                rotRoot.P.R = newRoot
            else:
                rotRoot.P.L = newRoot
        newRoot.R = rotRoot
        rotRoot.P = newRoot
        rotRoot.B = rotRoot.B - 1 - max(newRoot.B, 0)  # 更新平衡因子
        newRoot.B = newRoot.B - 1 + min(rotRoot.B, 0)  # 更新平衡因子
    '''#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#'''

    def __len__(self):  # 字典的大小（元素个数）
        return self.size

    def __contains__(self, key):  # 判断某元素是否在字典中
        try:
            v = self[key]   # Unused variable 'v'
        except KeyError:
            return False
        return True

    def clear(self):  # 清除字典
        self.__init__()

    def __str__(self):
        # 输出字符串形式，参照内置dict类型，输出按照AVL树中序遍历次序
        # 格式类似：{'name': 'sessdsa', 'hello': 'world'}
        string = '{'
        if self.size == 0:
            string += '}'
        else:
            for i in range(self.size - 1):
                string = string + \
                    repr(self.keys()[i]) + ': ' + \
                    repr(self.values()[i]) + ', '
            string = string + \
                repr(self.keys()[-1]) + ': ' + \
                repr(self.values()[-1]) + '}'
        return string

    __repr__ = __str__

    def keys(self):  # 返回所有的key，类型是列表，按照AVL树中序遍历次序
        keys = []
        for key in self:
            keys.append(key)
        return keys

    def values(self):  # 返回所有的value，类型是列表，按照AVL树中序遍历次序
        values = []
        for key in self:
            values.append(self[key])
        return values

    def __iter__(self):     # 迭代器
        if self.root:
            return iter(self.root)
        else:
            return iter({})  # 若树为空，则迭代空字典

    def getNode(self, key):  # 查找某个节点，返回一个TreeNode类
        if self.root:
            node = self._get(key, self.root)
            if node:
                return node
            else:
                return None
        else:
            return None

    def structure(self):    # 输出树的结构（key，value，balanceFactor和左右节点连接情况）
        print('\n<Tree>')
        for key in self:
            print('key = '+str(key)+', value = ' +
                  str(self[key])+', balanceFactor = '+str(self.getNode(key).B), end=', ')
            if self.getNode(key).L != None and self.getNode(key).R == None:
                print('LeftKey: ' + str(self.getNode(key).L.k), end='\n')
            elif self.getNode(key).R != None and self.getNode(key).L == None:
                print('RightKey: ' + str(self.getNode(key).R.k), end='\n')
            elif self.getNode(key).L != None and self.getNode(key).R != None:
                print('LeftKey: ' + str(self.getNode(key).L.k) +
                      ', RightKey: ' + str(self.getNode(key).R.k), end='\n')
            else:
                print('')
        print('</Tree>\n')

    def treeHeight(self):   # 整棵树的高度
        print(self.root.height())


# SESSDSA20 H5

print_bak = globals().get('print_bak', print)  # 使用另行备份的print_bak函数
has_error = False

from collections import deque, Counter
from random import randrange, choice, shuffle
from sys import stderr

LINE_WIDTH = 50
N_TESTS = 10
N_OPS = 20
N_KEYERRORS = 5
POOL_SIZE = 10
TYPES = (int, float, str)
SCORES = Counter()
SCORES['b'] = SCORES['b1'] = SCORES['b2'] = SCORES['b3'] = SCORES[
    'e1'] = SCORES['e2'] = 0

# 恢复默认hash
if 'hash' in globals():
    globals()['hash'] = __builtins__.hash

if 'ref ds':

    class ref_dict(dict):
        def _ordered_items(self):
            return sorted(self.items(), key=lambda x: hash(x[0]))

        keys = lambda s: [x[0] for x in s._ordered_items()]
        values = lambda s: [x[1] for x in s._ordered_items()]

        def __repr__(self):
            tmp = ', '.join('%r: %r' % x for x in self._ordered_items())
            return f"{{{tmp}}}"

        __str__ = __repr__


def rand_type(x):
    return choice(TYPES)(x)


def gen_rand_pool(idx):
    """
    0-2: str/int/float
    3-5: exclude str/int/float
    else: all random
    """
    pool = list(range(POOL_SIZE))
    shuffle(pool)

    # 全随机
    if idx > 5:
        pool = [rand_type(x) for x in pool]
        return pool

    # 前半
    if idx in (0, 4, 5):
        pool[:POOL_SIZE // 2] = list(map(str, pool[:POOL_SIZE // 2]))
    if idx == 2:
        pool[:POOL_SIZE // 2] = list(map(float, pool[:POOL_SIZE // 2]))
    # 后半
    if idx == 0:
        pool[POOL_SIZE // 2:] = list(map(str, pool[POOL_SIZE // 2:]))
    if idx in (2, 3, 4):
        pool[POOL_SIZE // 2:] = list(map(float, pool[POOL_SIZE // 2:]))

    # 返回结果
    return pool


def check_AVL_iterative(root):
    """
    非递归检查AVL性
    非法情况将直接抛出异常
    返回树总节点数
    """
    if root is None:
        return 0

    _h_cache = {}

    def height(node):
        if node is None:
            return 0
        if not id(node) in _h_cache:
            _h_cache[id(node)] = 1 + max(
                height(node.getLeft()),
                height(node.getRight()),
            )
        return _h_cache[id(node)]

    # 1. 层次遍历节点+检测成环
    occurred = set()  # id(node)
    bfs = deque([root])
    node_list = []
    while bfs:
        node = bfs.popleft()
        assert isinstance(node, TreeNode), f'节点{node!r}非TreeNode类'
        assert id(node) not in occurred, f'成环节点: {node!r}'
        occurred.add(id(node))
        node_list.append(node)
        childs = [node.getLeft(), node.getRight()]
        bfs.extend(x for x in childs if x != None)
    node_list.reverse()  # 由低至高查找, 保证非缓存深度不大于2

    # 2. 判断AVL性
    for node in node_list:
        nl, nr = node.getLeft(), node.getRight()
        bF = abs(height(nl) - height(nr))
        assert bF <= 1, f'节点{node!r}不平衡: H(l)={height(nl)}; H(r)={height(nr)})'

    # 3. 返回总节点数
    return len(node_list)


def print_error(t_dict, r_dict, e):
    global has_error
    has_error = True

    print_bak('\n报错: (%s: %s)' % (type(e).__name__, str(e)), file=stderr)
    try:
        print_bak('LAST DICTS'.center(LINE_WIDTH, '.'))
        sr, st = str(r_dict), str(t_dict)
        print_bak('测试对象:', st)
        if st != sr:
            print_bak('参考对象:', sr)
    except Exception as e:
        print_bak('打印报错 (%s: %s)' % (type(e).__name__, str(e)), file=stderr)
    print_bak('END'.center(LINE_WIDTH, '.'))


def test(i, t_dict, r_dict, op_write, op_read):
    print_bak('TEST #%d...' % i, end=' ')
    _SIZE = 0
    passed = False
    ops = []
    params = []
    key_pool = gen_rand_pool(i)

    def get(param):
        return choice(key_pool)

    def one_check(op):
        ref_exec = True
        op = op.split()

        try:
            params.clear()
            params.extend(map(get, op[1:]))
            r_ref = getattr(r_dict, op[0])(*params)
        except:
            ref_exec = False

        if ref_exec:
            r_test = getattr(t_dict, op[0])(*params)
            if r_ref != None:
                assert r_ref == r_test, f'输出: {r_test!r};\n应该输出: {r_ref!r}'

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
            _SIZE = len(r_dict)

            # read one
            curr_op = choice(op_read)
            one_check(curr_op)

        passed = True
        SCORES['b'] += 1
    except Exception as e:
        print_bak('\n出错的操作:', output((curr_op.split()[0], *params)))
        print_bak('历史操作:', ','.join(map(output, ops)))
        print_error(t_dict, r_dict, e)

    if passed:
        test_extra(t_dict, r_dict, list(map(output, ops)))


def test_extra(t_dict, r_dict, ops):

    curr_op = None
    try:
        print_bak('检查树结构...', end=' ')
        curr_keys = set(r_dict.keys())  # 所有
        nkeys = len(curr_keys)
        nnodes = check_AVL_iterative(t_dict.getRoot())
        assert nkeys == nnodes, f'节点数({nnodes})与字典键数({nkeys})不相等'
        SCORES['b1'] += 1

        print_bak('检查KeyError...', end=' ')
        for i in range(N_KEYERRORS):
            # 生成不存在key
            while 1:
                k = rand_type(randrange(POOL_SIZE))
                if isinstance(k, str):
                    if k not in r_dict:
                        break
                elif int(k) not in r_dict and float(
                        k) not in r_dict:  # fuck brython
                    break

            # 捕捉异常
            try:
                try:
                    curr_op = f'try __getitem__({k!r})'
                    t_dict[k]
                except KeyError as e:
                    ops.append(curr_op)
                else:
                    assert 0, '未按要求抛出异常'
                try:
                    curr_op = f'try __delitem__({k!r})'
                    del t_dict[k]
                except KeyError as e:
                    ops.append(curr_op)
                else:
                    assert 0, '未按要求抛出异常'
            except AssertionError:
                raise
            except Exception as efail:
                raise AssertionError(
                    f'报错类型不正确({type(efail).__name__}: {efail})')
        SCORES['b2'] += 1

        print_bak('检查__str__...', end=' ')
        curr_op = None
        assert str(t_dict) == str(r_dict), '__str__结果不同'
        SCORES['b3'] += 1

        print_bak('PASS')
    except Exception as e:
        print_bak('\n出错的操作:', curr_op)
        print_bak('历史操作:', ','.join(ops))
        print_error(t_dict, r_dict, e)


# 常规随机样例
print_bak('\n' + "mydict".center(LINE_WIDTH, '='))
for i in range(N_TESTS):
    l1 = mydict()
    l2 = ref_dict()
    test(i, l1, l2, (
        '__setitem__ rand rand',
        '__setitem__ rand rand',
        '__setitem__ rand rand',
        '__delitem__ rand',
    ) * 3 + ('clear', ), (
        'keys',
        'values',
        '__len__',
        '__getitem__ rand',
        '__contains__ rand',
    ))

# 特殊样例
print_bak('=' * LINE_WIDTH)
cases = [
    ('range(20)', 'range(10)'),
    ('reversed(range(20))', 'range(14,20)'),
    ('list(range(20))+list(range(20))', 'range(14,20)'),
    ('(0,-4,4,2,6,-6,-2,1,3,5,7,-7,-5,-3)', '(1,3,5,7,2,6,4)'),
]
for i, case in enumerate(cases):
    try:
        t_dict = mydict()
        r_dict = ref_dict()
        data_add = list(eval(case[0]))
        data_del = list(eval(case[1]))

        # 添加
        print_bak(f'TEST #{i+N_TESTS}... insert {case[0]}...', end=' ')
        for i in data_add:
            t_dict[i] = i
            r_dict[i] = i
        nnodes = check_AVL_iterative(t_dict.getRoot())
        size, e_size = len(t_dict), len(r_dict)
        assert nnodes == len(
            t_dict) == e_size, f'树节点数({nnodes})/长度({size})与预期({e_size}) 不符'
        SCORES['e1'] += 1

        # 删除
        print_bak(f'remove {case[1]}...', end=' ')
        e_size -= len(data_del)
        for i in data_del:
            del t_dict[i]
            del r_dict[i]
        nnodes = check_AVL_iterative(t_dict.getRoot())
        size, e_size = len(t_dict), len(r_dict)
        assert nnodes == len(
            t_dict) == e_size, f'树节点数({nnodes})/长度({size})与预期({e_size}) 不符'
        SCORES['e2'] += 1

        print_bak('PASS')

    except Exception as e:
        print_error(t_dict, r_dict, e)

# 输出得分
print_bak('\n' + "SCORES".center(LINE_WIDTH, '='))
SCORES['B'], SCORES['E'] = N_TESTS, len(cases)
print_bak('随机样例：{b3}/{B} (基础：{b}/{B} 树结构：{b1}/{B} 异常处理：{b2}/{B} str：{b3}/{B})'.
          format(**SCORES))
print_bak('特殊样例：{e2}/{E} (插入：{e1}/{E} 删除：{e2}/{E})'.format(**SCORES))

if has_error:
    comment = [
        '如果测评机给出了错误样例，',
        '首先',
        '在本地使用该输入运行自己',
        '提交的作业中',
        '的代码，并在',
        '批改结果有误',
        '或',
        '运行结果与在线不一致',
        '时联系助教',
    ]
    try:
        from browser import document
        target, buffer = document['py_stdout'], '\n\n'
        formats = [
            '%s',
            '<b style="color:red">%s</b>',
        ]
        buffer += '<h2 style="display:inline-block">'
        for i, c in enumerate(comment):
            buffer += formats[i % 2] % c
        target.innerHTML += buffer + '</h2> (注: 不包括报错信息不一致的情况)'
    except ImportError:
        print_bak(''.join(comment), file=stderr)
