a = input()
b = []
for i in range(len(a)):
    b.append(a.count(a[i]))

b = sorted(b)
c = max(b)-min(b)
if c in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 /
         53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
    print("Lucky Word")
    print(c)
else:
    print("No Answer")
    print('0')
