n=int(input())
m=input().split()
b=[]
for i in range(n):
    b.append(m.count(m[i]))
b=sorted(b)
print(b[-1])