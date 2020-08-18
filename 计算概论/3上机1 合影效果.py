a=int(input())                   
list=[] 
strm=''
strf=''
for i in range(a):
    list+=[input().split(' ')] 
for i in range(a):
    if list[i][0]=='male':
        strm += str(list[i][1])+' '
listm=strm.split()
listm2=sorted(listm)
for i in range(a):
    if list[i][0]=='female':
        strf += str(list[i][1])+' '
listf=strf.split()
listf2=sorted(listf,reverse=True)
sigma=listm2+listf2
for i in range(len(sigma)):
    print(str(sigma[i]),end=' ')
