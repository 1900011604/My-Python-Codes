n=int(input())
if n>=100:
    a=n//100
    print(a)
    n=n-100*a
else:
    print(0)
if n>=50:
    b=n//50
    print(b)
    n=n-50*b
else:
    print(0)
if n>=20:
    c=n//20
    print(c)
    n=n-20*c
else:
    print(0)
if n>=10:
    d=n//10
    print(d)
    n=n-10*d
else:
    print(0)
if n>=5:
    e=n//5
    print(e)
    n=n-5*e
else:
    print(0)
if n>=1:
    print(n)
else:
    print(0)
