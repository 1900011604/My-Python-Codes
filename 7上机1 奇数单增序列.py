n=int(input())
num=input().split()
odd=[]
for i in range(n):
    num[i]=int(num[i])
    if num[i]%2==1:
        odd.append(num[i])
odd=sorted(odd)
odd2=''
for i in range(len(odd)):
    odd2+=str(odd[i])
    odd2+=','
print(odd2.rstrip(','))