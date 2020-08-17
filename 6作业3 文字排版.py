n=int(input())
text=input()
list1=text.split()
line=''
i=0
while i<n:
    if len(line)+len(list1[i])<=80:
        line+=list1[i]
        line+=' '
        i+=1
        if i==n-1:
            line+=list1[i]
            line+=' '
            line2=line.rstrip(' ')
            print(line2)
            line=''
    else:
        line2=line.rstrip(' ')
        print(line2)
        line=''
   
