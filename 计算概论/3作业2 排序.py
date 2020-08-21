A=int(input())                   
list=[]                         
for i in range(A):
    list+=[input().split()]      
for i in range(len(list)):
    list[i][0],list[i][1]=list[i][1],list[i][0]
    list[i][0]=int(list[i][0])
    if list[i][1]=='monster':
        list[i][1]='a'
    elif list[i][1]=='witcher':
        list[i][1]='b'
    else:
        list[i][1]='c'
list2=sorted(list)
for i in range(len(list2)):
    list2[i][0],list2[i][1]=list2[i][1],list2[i][0]
    list2[i][1]=str(list2[i][1])
    if list2[i][0]=='a':
        list2[i][0]='monster'
    elif list2[i][0]=='b':
        list2[i][0]='witcher'
    else:
        list2[i][0]='pitchfork'
for i in range(len(list2)):
    print(str(list2[i][0]),str(list2[i][1]))
