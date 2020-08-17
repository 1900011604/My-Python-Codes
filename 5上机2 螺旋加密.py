shuru=input()
import re
l1=re.findall('\d{1,2}',shuru)
R,C=int(l1[0]),int(l1[1])
str1=''
for q in range(len(l1)):
    str1+=l1[q]
    str1+=' '

string=shuru.lstrip(str1)
code1=[]
for y in range(len(string)):
    if string[y]==' ':
        code1+='00000'
    else:
        code1+="{0:0>5}".format(bin(ord(string[y])-64).lstrip("0b"))

code1=list(code1)
for k in range(len(code1),R*C):
    code1.append('0')

code=[]
for z in range(R*C):
    code.append('0')

a,b=0,0
i,j,n=0,0,0
r,c=R,C

while r>1 and c>1:
        a=0
        b=c-1
        while i in range(a,b):
            code[j]=code1[i+n]
            i+=1
            j+=1  #right
        
        a=c-1
        b=c+r-2
        while i in range(a,b):
            code[j]=code1[i+n]
            i+=1
            j+=C  #down
        
        a=c+r-2
        b=2*c+r-3
        while i in range(a,b):
            code[j]=code1[i+n]
            i+=1
            j-=1  #left
        
        a=2*c+r-3
        b=2*c+2*r-4
        while i in range(a,b):
            code[j]=code1[i+n]
            i+=1
            j-=C  #up

        n=n+(2*c+2*r-4)
        r=r-2
        c=c-2
        j+=C+1
        i=0

if r==1:  #right
    a=0
    b=c
    while i in range(a,b):
        code[j]=code1[i+n]
        i+=1
        j+=1
elif c==1:  #down
        a=0
        b=r
        while i in range(a,b):
            code[j]=code1[i+n]
            i+=1
            j+=C

q=''
for i in range(len(code)):
    q+=code[i]
print(q)
