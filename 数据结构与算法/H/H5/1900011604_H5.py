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