from sys import stdin

for line in stdin:
    a=1
    b=1
    for i in range(1,int(line)):
        a,b=b,a+b
        i+=1
    print(b)
