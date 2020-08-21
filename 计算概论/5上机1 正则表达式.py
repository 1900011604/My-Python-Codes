from sys import stdin
for line in stdin:
    c=line.count('_')
    import re
    m=re.match("[a-z]+_{1}[a-z]+",line)
    if m!=None and c==1:
        print('Yes')
    else:
        print('No')
