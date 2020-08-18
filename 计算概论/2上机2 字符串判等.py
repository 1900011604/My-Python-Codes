A=input()
B=input()
a=A.lower()
b=B.lower()
a2=a.split()

na=len(a2)
a3=''
for i in range(na):
    a3=a3+str(a2[i])

b2=b.split()

nb=len(b2)
b3=''
for i in range(nb):
    b3=b3+str(b2[i])

if a3==b3:
    print('YES')
else:
    print('NO')
