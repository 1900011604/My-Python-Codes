path='C:/Users/19000/Desktop/PKU Courses/计算概论/作业/4作业1 学科等级统计 score.txt'
with open(path,encoding='utf-8') as f:
    score = f.readlines()
f.close()
sis=''        #score[i] in string
sil=[]      #score[i] in list
lis=''          #level[i] in string
lil=[]       #level[i] in list
for i in range(1,len(score)):
    sis=str(score[i])
    sil=sis.split()
    if int(sil[1])>=85 and int(sil[2])>=85 and int(sil[3])>=85 \
       and int(sil[1])+int(sil[2])+int(sil[3])>=260:
        lil.append(sil[0])
        lil.append('优秀')
    elif int(sil[1])<60 or int(sil[2])<60 or int(sil[3])<60 \
       or int(sil[1])+int(sil[2])+int(sil[3])<180:
        lil.append(sil[0])
        lil.append('不及格')
    else:
        lil.append(sil[0])
        lil.append('及格')
a=open('C:/Users/19000/Desktop/PKU Courses/计算概论/作业/4作业1 学科等级统计 level.txt','w')
j=0
while j<len(lil):
    lis=lis+str(lil[j])+'\t'
    lis=lis+str(lil[j+1])+'\n'
    a.write(lis)
    lis=''
    j+=2
a.close()


    
    
        
    
   

