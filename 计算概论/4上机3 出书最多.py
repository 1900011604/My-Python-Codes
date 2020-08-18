m=int(input())
book=[]
for i in range(m):
    book+=[input().split()]
author=''
for i in range(m):
    author+=book[i][1]

maxauthor=[]
for i in range(len(author)-1):
    maxauthor+=[author.count(author[i])]

maxauthor2=sorted(maxauthor)

max=maxauthor.index(maxauthor2[-1])
print(author[max])
print(maxauthor2[-1])
for i in range(m):
    if author[max] in book[i][1]:
        print(book[i][0])
