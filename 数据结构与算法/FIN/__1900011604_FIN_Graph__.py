class Queue:  # 队列

    def __init__(self):  # 初始化队列
        self.items = []

    def isEmpty(self):  # 判断队列是否为空
        return self.items == []

    def enqueue(self, item):  # 将item加入队列
        self.items.insert(0, item)

    def dequeue(self):  # 将item移出队列
        return self.items.pop()


class Vertex:  # 顶点

    def __init__(self, _id):  # 初始化顶点
        self.id = _id
        self.connectedTo = {}  # 与该顶点相邻的顶点
        # 以顶点（Vertex类）为key，顶点的附带属性为value的字典
        self.color = 0
        self.dist = 0  # 顶点距离初始设置为0
        self.attribute = set()  # 顶点附带属性是其出演的电影列表

    def addNeighbor(self, v, Attribute):  # 将v添加到与self相邻的顶点中
        self.connectedTo[v] = set()
        self.connectedTo[v].add(Attribute)


class Graph:  # 图

    def __init__(self):  # 创建一个空图
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):  # 将顶点selfkey加入图中
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):  # 查找编号为n的顶点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, i, j, Attribute):  # 添加从i到j的无权无向（双向）边
        i = self.getVertex(i)
        j = self.getVertex(j)
        i.addNeighbor(j, Attribute)
        j.addNeighbor(i, Attribute)

    def getEdge(self, i, j):  # 边附带属性是共同出演的电影列表
        i = self.getVertex(i)
        j = self.getVertex(j)
        coFilm_ij = []
        for i_film in i.attribute:
            if i_film in j.attribute:
                coFilm_ij.append(i_film)
        return coFilm_ij

    def __iter__(self):  # 对图的顶点进行迭代
        return iter(self.vertList.values())

    def bfs_CC(self, startKey):  # 计算连通分支所用的BFS算法
        start = self.getVertex(startKey)  # 遍历的起始顶点
        q = Queue()
        q.enqueue(start)  # 1 创建一个队列，遍历的起始顶点放入队列
        vertSet = set()  # 记录连通分支规模（顶点数量）的集合
        while not q.isEmpty():  # 2 从队列中取出一个元素，并将其未访问过的顶点放到队列中
            current = q.dequeue()
            vertSet.add(current.id)  # 连通分支规模 + 1
            for v in current.connectedTo.keys():  # 3 重复步骤2，直至队列空
                if v.color == 0:
                    v.color = 1
                    q.enqueue(v)
            current.color = 2
        vertSet = sorted(vertSet)
        return vertSet

    def bfs_dist(self, startKey):  # 计算一个连通分支直径所用的BFS算法
        start = self.getVertex(startKey)  # 遍历的起始顶点
        start.dist = 0
        q = Queue()
        q.enqueue(start)  # 1 创建一个队列，遍历的起始顶点放入队列
        while not q.isEmpty():  # 2 从队列中取出一个元素，并将其未访问过的顶点放到队列中
            current = q.dequeue()
            for v in current.connectedTo.keys():  # 3 重复2，直至队列空
                if v.color == 0:
                    v.color = 1
                    v.dist = current.dist + 1  # 顶点距离 + 1
                    q.enqueue(v)
            current.color = 2
        for i in self:  # 顶点颜色全部重置为0
            i.color = 0

    def CC(self):  # 对一个图计算其所有连通分支（CC = connected components）的函数
        CC_list = []
        for v in self:
            if v.color == 0:
                # 只有颜色为0的顶点才会被遍历到，实际上是对每一个连通分支调用一次BFS算法
                b = self.bfs_CC(v.id)
                CC_list.append(b)
        return CC_list