n=int(input())
x=0
for i in range(1,n+1):
    if i%7!=0 and i not in [7,17,27,37,47,57,67,77,87,97,71,72,73,74,75,76,78,79]:
        x+= i**2
print(x)
