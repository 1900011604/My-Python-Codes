txt=''
a=[]
for i in range(4):
    txt+=input()
for i in range(65,91):
    a.append(txt.count(chr(i)))

import copy
b=copy.deepcopy(a)
c = copy.deepcopy(a)

empty=[]
for i in range(26):
    empty+=[' ']
emptystr=''

m=max(b)
for i in range(m):
    for i in range(26):
        a[i]=a[i]-m+1
        if a[i]<=0:
            a[i]=0
    #print(a) 真正要用到的
    for i in range(26):
        if a[i]==1:
            empty[i]='* '
        else:
            empty[i]='  '
        emptystr+=empty[i]
    print(emptystr)
    emptystr=''
    for i in range(26):
        a[i]=c[i]-a[i]
    c = copy.deepcopy(a)
    m-=1

print('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ')
