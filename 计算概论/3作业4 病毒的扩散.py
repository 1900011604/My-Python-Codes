Python 3.7.5 (tags/v3.7.5: 5c02a39a0b, Oct 15 2019, 01: 31: 54)[MSC v.1916 64 bit(AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>> > mn = input()
m, n = mn.split()[0], mn.split()[1]
list = []
for i in range(9):
    list += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
if int(n) == 1:
    list[3] = [0, 0, 0, 1, 1, 1, 0, 0, 0]
    list[4] = [0, 0, 0, 1, 2, 1, 0, 0, 0]
    list[5] = list[3]
elif int(n) == 2:
    list[2] = [0, 0, 1, 2, 3, 2, 1, 0, 0]
    list[3] = [0, 0, 2, 6, 8, 6, 2, 0, 0]
    list[4] = [0, 0, 3, 8, 12, 8, 3, 0, 0]
    list[5] = list[3]
    list[6] = list[2]
elif int(n) == 3:
    list[1] = [0, 1, 3, 6, 7, 6, 3, 1, 0]
    list[2] = [0, 3, 12, 24, 30, 24, 12, 3, 0]
    list[3] = [0, 6, 24, 51, 63, 51, 24, 6, 0]
    list[4] = [0, 7, 30, 63, 80, 63, 30, 7, 0]
    list[5] = list[3]
    list[6] = list[2]
    list[7] = list[1]
elif int(n) == 4:
    list[0] = [1, 4, 10, 16, 19, 16, 10, 4, 1]
    list[1] = [4, 20, 52, 88, 104, 88, 52, 20, 4]
    list[2] = [10, 52, 142, 244, 292, 244, 142, 52, 10]
    list[3] = [16, 88, 244, 428, 512, 428, 244, 88, 16]
    list[4] = [19, 104, 292, 512, 616, 512, 292, 104, 19]
    list[5] = list[3]
    list[6] = list[2]
    list[7] = list[1]
    list[8] = list[0]
list1 = []
for i in range(9):
    list1 += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(9):
    list1[i][0] = int(m)*list[i][0]
    list1[i][1] = int(m)*list[i][1]
    list1[i][2] = int(m)*list[i][2]
    list1[i][3] = int(m)*list[i][3]
    list1[i][4] = int(m)*list[i][4]
    list1[i][5] = int(m)*list[i][5]
    list1[i][6] = int(m)*list[i][6]
    list1[i][7] = int(m)*list[i][7]
    list1[i][8] = int(m)*list[i][8]
for i in range(9):
    for j in range(9):
        print(list1[i][j], end=' ')
    print()
