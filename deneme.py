ikili=[]
num=0
tot=0
totalmac=9
for i in range(1,totalmac+1):
    for a in range(i+1,totalmac+1):
        ikili.append((i,a))

for i in range(len(ikili)):
    for a in range(i+1,len(ikili)):
        deg1=ikili[i][0]-ikili[a][0]
        deg2 = ikili[i][1] - ikili[a][1]
        tot=tot+1

        if (deg1>0 and deg2<0) or (deg1<0 and deg2>0):
            num=num+1
            print(ikili[i],ikili[a])


print(num,tot)