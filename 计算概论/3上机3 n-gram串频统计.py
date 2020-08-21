n=int(input())
if n in range(2,5):
    a=input()
    b=''
    num=[]
    if len(a)>=n:
        for i in range(len(a)-n+1):
            for j in range(n):
                b+=a[i+j]
            b+=' '
        listb=b.split()
        for i in range(len(listb)):
            num.append(listb.count(listb[i]))  
        num2=sorted(num)   
        zuida=num2[len(num2)-1]
        if int(zuida)>1:
            print(zuida)  
            x=num2.count(zuida)
            y=int(x)/int(zuida)
            y=int(y)          
            z=0
            ddf=[]
      
            for i in range(len(a)-n+1):
                if b.count(str(listb[i]))==zuida:
                    ddf.append(listb[i])
            
            ddf2=[]
            for i in range(len(ddf)-1):
                if ddf[i] not in ddf2:
                    ddf2.append(ddf[i])
            
            for i in range(len(ddf2)):
                print(ddf2[i])
        elif int(zuida)==1:
            print('NO')
    else:
       print('NO')
