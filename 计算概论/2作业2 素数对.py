def IsPrime(n):
    if n==2:
        return True
    else:
        for i in range (2,n):
            if n%i==0:
                 return False
                 break
            elif i*i>n:
                return True
                break
a=int(input())
for i in range(1,a+1):
    if IsPrime(i) and IsPrime(i-2):
        print(i-2,i)
    elif a<5:
        print("empty")
        break
