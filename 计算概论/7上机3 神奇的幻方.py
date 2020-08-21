N = int(input())
n = 2*N-1
mat = []
DDF = []
for i in range(n):
    for j in range(n):
        DDF.append(0)
    mat += [DDF]
    DDF = []

a, x, y = 1, 0, N-1
while a < n**2:
    mat[x][y] = a
    if x == 0 and y != n-1:
        a, x, y = a+1, n-1, y+1
        mat[x][y] = a
    elif y == n-1 and x != 0:
        a, x, y = a+1, x-1, 0
        mat[x][y] = a
    elif x == 0 and y == n-1:
        a, x, y = a+1, 1, n-1
        mat[x][y] = a
    elif mat[x-1][y+1] != 0:
        a, x, y = a+1, x+1, y
        mat[x][y] = a
    else:
        a, x, y = a+1, x-1, y+1
        mat[x][y] = a

if N == 1:
    print('1')
else:
    VAN = ''
    for i in range(n):
        for j in range(n):
            VAN += str(mat[i][j])
            VAN += ' '
        print(VAN, end='\n')
        VAN = ''
