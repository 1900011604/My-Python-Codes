class BT:
    def __init__(self, root):
        self.key = root
        self.L = None
        self.R = None

    def insertL(self,new):
        if self.L == None:
            self.L = BT(new)
        else:
            t = BT(new)
            t.L = self.L
            self.L = t

    def insertR(self,new):
        if self.R == None:
            self.R = BT(new)
        else:
            t = BT(new)
            t.R = self.R
            self.R = t

    def getL(self):
        return self.L

    def getR(self):
        return self.R

    def set(self,obj):
        self.key = obj

    def get(self):
        return self.key

    def all(self):
        print(self.key)
        if self.L:
            self.L.all()
        if self.R:
            self.R.all()
            
    def __str__(self):
        def getStr(t):
            if not t:
                return []
            return [t.get(), getStr(t.L), getStr(t.R)]
        return str(getStr(self))

    def height(self):
        def getHeight(t):
            if not t:
                return 0
            return 1 + max(getHeight(t.L), getHeight(t.R))
        return getHeight(self)

        
def buildTree():
    myBT = BT('a')
    myBT.insertL('b')
    myBT.insertR('c')
    myBT.getL().insertR('d')
    myBT.getR().insertL('e')
    myBT.getR().insertR('f')
    return myBT

myBT = buildTree()
print(myBT)
print(myBT.height())
