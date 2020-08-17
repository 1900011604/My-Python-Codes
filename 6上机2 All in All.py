from sys import stdin
for L in stdin:
    P=L.split()
    s,t=str(P[0]),str(P[1])#判断s是不是t的子串
    sub='.*'
    for i in range(len(s)):
        sub+=s[i]
        sub+='.*'
    
    import re
    m=re.match(sub,t)
    if m!=None:
        print('Yes')
    else:
        print('No')
