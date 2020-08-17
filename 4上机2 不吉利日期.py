w=int(input())
d=13
for i in range(0,12):
        
        if i==0:
                d+=0
        elif 1<=i and i<=7 and i%2 or i>= 8 and i%2==0:
                d+=31
        elif i==2:
                d+=28
        else:
                d+=30
       
        if (d-1+w)%7==5:
            print(i+1)
