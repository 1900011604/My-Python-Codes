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
