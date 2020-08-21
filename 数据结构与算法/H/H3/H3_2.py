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

    def __repr__(self):
        if len(self.items) != 0:
            s='['
            for i in range(len(self.items)-1):
                a=self.items[i]
                s+='%s '%a
            s+='%s]'%self.items[len(self.items) - 1]
        else:
            s='[]'
        return s

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
