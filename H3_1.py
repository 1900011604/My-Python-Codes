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
