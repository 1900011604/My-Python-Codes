a=input()
list=[]
for b in range(0,int(a),1):
    list += [int(input())]
for g in range(0,int(a),1):
    f=list[g]
    c,d=1,1
    for i in range(1,21,1):
        if i==f:
            print(c)
        c,d=d,c+d
