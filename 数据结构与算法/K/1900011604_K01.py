#第一题
n=int(input())
if n%2==1:
    for i in range(n):
        if i==0:
            s=" "*(n-i-1)+'#'  #最右边不需要额外加空格，因为本身就是空白，下同。
        elif i==(n-1):
            s='#'*(2*n-1)
        else:
            s=' '*(n-i-1)+'#'+' '*(2*i-1)+'#'
        print(s)

#第二题
n=int(input())
if n%2==1:
    m=int((n-1)/2)
    j=m
    while j>0:
        i=m-j
        y=((m+0.5)**2-j**2)**0.5-0.5  #考虑中心到边缘的0.5个‘#’的长度
        if y-int(y)>=0.5:  #这个分支结构是四舍五入用的，下同
            y=int(y)+1
        else:
            y=int(y)
        print(' '*(m-y)+'#'*(2*y+1))
        j-=1
    print('#'*n)
    for i in range(0,m):
        y=((m+0.5)**2-(i+1)**2)**0.5-0.5
        if y-int(y)>=0.5:
            y=int(y)+1
        else:
            y=int(y)
        print(' '*(m-y)+'#'*(2*y+1))  #输出n行的‘#’

#第三题
s=input()
s=s.replace('E','e')
s=s.replace('ee','E3')
s=s.replace('e','3')
print(s)

#第四题
s=input()
s=s.replace('E','e')
s=s.replace('ee','E3')
s=s.replace('e','3')
print(s)