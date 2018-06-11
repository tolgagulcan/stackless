class iki9:
    __slots__ = {"ls"}
    def __init__(self):
        self.ls=[0,0,0,0,0,0,0,0,0]

    def mark(self,snc1,snc2):
        where=snc1*3+snc2
        self.ls[where]=1

    def unmark(self, snc1, snc2):
        where = snc1 * 3 + snc2
        self.ls[where] = 0
    def __repr__(self):
        return str(self.ls)

hepsi=[]

for i in range(15):
    hepsi.append([])
    for a in range(15):
        if a>i:
            hepsi[i].append(iki9())
        else:
            hepsi[i].append(None)


def markall(ls:list,isaretli:int):
    for i in range(isaretli):
        d=ls[len-i-1]
        mark(d.mac1,d.sonuc1,d.mac2,d.sonuc2)

def hesapla(hata:int):
    pass
def mark(mac1,sonuc1,mac2,sonuc2):
    if mac1>mac2:
        mark(mac2,sonuc2,mac1,sonuc1)
        return

    hepsi[mac1-1][mac2-1].mark(sonuc1,sonuc2)

mark(15,2,14,2)
if __name__=="__main__":
    for i in range(len(hepsi)):
        print(hepsi[i])