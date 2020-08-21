l1=input().split()
l2=input().split()
y1,m1,d1=int(l1[0]),int(l1[1]),int(l1[2])
y2,m2,d2=int(l2[0]),int(l2[1]),int(l2[2])
for i in range(1,y1):
    if i%4==0 and i%100 or i%400==0:
        d1+=366
    else:
        d1+=365
for i in range(y1,y1+1):
    if i%4==0 and i%100 or i%400==0:
        for i in range(1,m1):
            if i<=7 and i%2 or i>= 8 and i%2==0:
                d1+=31
            elif i==2:
                d1+=29
            else:
                d1+=30
    else:
        for i in range(1,m1):
            if i<=7 and i%2 or i>= 8 and i%2==0:
                d1+=31
            elif i==2:
                d1+=28
            else:
                d1+=30
for i in range(1,y2):
    if i%4==0 and i%100 or i%400==0:
        d2+=366
    else:
        d2+=365
for i in range(y2,y2+1):
        if i%4==0 and i%100 or i%400==0:
            for i in range(1,m2):
                if i<=7 and i%2 or i>= 8 and i%2==0:
                    d2+=31
                elif i==2:
                    d2+=29
                else:
                    d2+=30
        else:
             for i in range(1,m2):
                if i<=7 and i%2 or i>= 8 and i%2==0:
                    d2+=31
                elif i==2:
                    d2+=28
                else:
                    d2+=30
x=d2-d1
print(x)
