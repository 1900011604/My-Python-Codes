a = input().split()

def public(x, y):  # 公共字符串
    lx = len(x)
    ly = len(y)
    if lx < ly:
        x, y = y, x  # x为长字符串，y为短字符串
    maxstr = x
    maxlen = lx
    for sublen in range(int(len(y)/2), 0, -1):  # 从大到小，保证最长的子串最先输出
        for i in range(maxlen-sublen+1):  # 从第i个字符开始切片
            if maxstr[i:i+sublen] in y:  # 字符串切片，子串长度为sublen
                return maxstr[i:i+sublen]
    else:
        return[]

x = a[0]
y = a[1]
x += x  # x成环
y += y  # y成环
b = len(public(x, y))  # 公共字符串的长度
if b <= len(y)/2:  # 现在y的长度是原来的两倍，所以len(y)要除以2
    print(b)
else:
    print(int(len(y)/2))
