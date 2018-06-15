from mergesort import mergesort
import pynput, sys, pickle, os.path
from key import getanswer
from readmatches import maclar, getmacname, getmacnamek
from bitarray import bitarray
from settings import totalmac
from tekliyeni import returnplace
times = 0
teklifstring = """
{0:^40}|{6:^20}||{7:^20}|
{0:^40}|{5}||{5}|
{0:^40}|{1:^20}||{8:^20}|
{0:^40}|{0:^20}||{0:^20}|
{0:^40}|{2:^20}||{9:^20}|
{0:^40}|{5}||{5}|
{0:^40}|{0:^20}||{0:^20}|
{0:^40}|{3:^20}||{4:^20}|
{0:^40}|{0:^20}||{0:^20}|
{0:^40}|{5}||{5}|
{0:^40}|{6:^20}||{7:^20}|
"""
if os.path.exists("bin\\ciftlisquare.bin") and os.path.exists("bin\\ciftlimarked.bin"):
    with open("bin\\ciftlisquare.bin", "rb") as f:
        ciftlisquare = pickle.load(f)
    with open("bin\\ciftlimarked.bin", "rb") as f:
        ciftlimarked = pickle.load(f)
else:
    hesap=((totalmac*3)**2)**2
    ciftlisquare = bitarray(hesap)
    ciftlimarked = bitarray(hesap)
    ciftlisquare.setall(False)
    ciftlimarked.setall(False)

class ciftlimac:
    __slots__ = {"sira"}
    def __init__(self, sira):
        self.sira=sira
    def __lt__(self, other):
        return ciftlimac.compare(self, other)
    def __repr__(self):
        mdict=self.getdictfromnumber()
        m1t1=getmacnamek(mdict[0])[0]
        m1t2 = getmacnamek(mdict[0])[1]
        m1s=mdict[1]

        m2t1 = getmacnamek(mdict[2])[0]
        m2t2 = getmacnamek(mdict[2])[1]
        m2s = mdict[3]


        temp="""
        {0}-{1}->{2}
        {3}-{4}->{5}
        """
        return temp.format(m1t1,m1t2,m1s,m2t1,m2t2,m2s)

    def getdictfromnumber(self):
        a = divmod(self.sira, totalmac*3*3)
        mac1 = a[0]

        b = divmod(a[1], totalmac*3)
        mac1sonuc = b[0]

        c = divmod(b[1], 3)
        mac2 = c[0]
        mac2sonuc = c[1]
        return mac1,mac1sonuc,mac2,mac2sonuc


def askquestion(o1,o2):
    global times
    times = times + 1

    print(o1)
    print(o2)

    #whattoprint = teklifstring.format(" ", m11, m12, skor1, skor2, "-" * 20, "<<<-----", "----->>>", m21, m22)
    answer = getanswer("*"*40)
    return answer
def save(finished=True):
    with open("bin\\ciftlisquare.bin", "wb") as f:
        pickle.dump(ciftlisquare, f)
    with open("bin\\ciftlimarked.bin", "wb") as f:
        pickle.dump(ciftlimarked, f)
        if finished:
            print("Finished")

    sys.exit()
def compare(o1: ciftlimac, o2: ciftlimac):
    if o1.sira>o2.sira:
        return not compare(o2,o1)
    place = o1.sira * (totalmac * 3)**2 + o2.sira
    if ciftlimarked[place]:
        return ciftlisquare[place]
    else:
        mac1=o1.getdictfromnumber()
        mac2=o2.getdictfromnumber()


        p1=returnplace(mac1[0],mac1[1])
        p2 = returnplace(mac1[2], mac1[3])

        p3 = returnplace(mac2[0], mac2[1])
        p4 = returnplace(mac2[2], mac2[3])



        max1=max(p1,p2);max2=max(p3,p4);min1=min(p1,p2);min2=min(p3,p4)
        if max1>=max2 and min1>=min2:
            return False

        if max1<=max2 and min1<=min2:
            return True


        answer = askquestion(o1,o2)
        if answer == "quit":
            save(False)
        else:
            ciftlimarked[place] = True
            ciftlisquare[place] = answer
            return answer
ciftlimac.compare = compare
ciftlimaclar = []
for i in range(totalmac*3):
    for a in range(i+1,totalmac*3):
        if divmod(i,3)[0]!=divmod(a,3)[0]:
            ciftlimaclar.append(ciftlimac((i*totalmac*3)+a))
mergesort(ciftlimaclar)

for a in ciftlimaclar:
    print(a)

save()
