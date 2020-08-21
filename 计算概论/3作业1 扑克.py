a=int(input())                   
list=[]                          
for i in range(a):
    list+=[input().split()]      
for i in range(len(list)):
    j=int(list[i][0])
    if j in range(1,2):
        print('spadeA')
    elif j in range(2,11):
        print('spade'+str(j))
    elif j in range(11,12):
        print('spadeJ')
    elif j in range(12,13):
        print('spadeQ')
    elif j in range(13,14):
        print('spadeK')
    if j in range(14,15):
        print('heartA')
    elif j in range(15,24):
        print('heart'+str(j-13))
    elif j in range(24,25):
        print('heartJ')
    elif j in range(25,26):
        print('heartQ')
    elif j in range(26,27):
        print('heartK')
    if j in range(27,28):
        print('diamondA')
    elif j in range(28,37):
        print('diamond'+str(j-26))
    elif j in range(37,38):
        print('diamondJ')
    elif j in range(38,39):
        print('diamondQ')
    elif j in range(39,40):
        print('diamondK')
    if j in range(40,41):
        print('clubA')
    elif j in range(41,50):
        print('club'+str(j-39))
    elif j in range(50,51):
        print('clubJ')
    elif j in range(51,52):
        print('clubQ')
    elif j in range(52,53):
        print('clubK')
