def f(n,m):
    if n==1:
        return 0
    elif n>1:
        return (f(n-1,m)+m)%n

from sys import stdin
for line in stdin:
    n,m=int(line.split()[0]),int(line.split()[1])
    if n>0 or m>0:
        print(f(n,m)+1)
    else:
        print('')
