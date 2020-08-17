a=input().split()
s=int(a[0])   
r=int(a[1])   
mat=[]
t=[]
for i in range(0,s):
    mat.append(input().split())
abcd=input()
for i in range(0,len(abcd)):
    if abcd[i]=='A':
        mat2=[]
        for j in range(0,r):
            for k in range(0,s):
                t.append(mat[r-1-k][j])
            mat2.append(t)
            t=[]
        mat=mat2
        x=s
        s=r
        r=x
    elif abcd[i]=='B':
        mat2=[]
        for j in range(0,s):
            for k in range(0,r):
                t.append(mat[k][r-1-j])
            mat2.append(t)
            t=[]
        mat=mat2
        x=s
        s=r
        r=x
    elif abcd[i]=='C':
        mat2=[]
        for j in range(0,s):
            for k in range(0,r):
                t.append(mat[j][r-1-k])
            mat2.append(t)
            t=[]
        mat=mat2
        
    elif abcd[i]=='D':
        mat2=[]
        for j in range(0,s):
            mat2.append(mat[s-1-j])
        mat=mat2
        
for i in range(0,s):
    for j in range(0,r):
        print(mat[i][j],end=' ')
    print('')
