from mergesort import mergesort
import pynput, sys, pickle, os.path
from key import getanswer
from readmatches import maclar, getmacname, getmacnamek
from bitarray import bitarray
from settings import totalmac
from tekliyeni import teklimaclar
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

def getdictfromnumber(first,second):
    m1 = divmod(first, 45)
    val1 = divmod(m1[0], 3)
    val2 = divmod(m1[1], 3)
    ms11 = {"mac": val1[0] + 1, "sonuc": val1[1]}
    ms12 = {"mac": val2[0] + 1, "sonuc": val2[1]}
    m2 = divmod(second, 45)
    val1 = divmod(m2[0], 3)
    val2 = divmod(m2[1], 3)
    ms21 = {"mac": val1[0] + 1, "sonuc": val1[1]}
    ms22 = {"mac": val2[0] + 1, "sonuc": val2[1]}
    ms11["takim1"] = getmacname(ms11["mac"])[0]
    ms11["takim2"] = getmacname(ms11["mac"])[1]
    ms12["takim1"] = getmacname(ms12["mac"])[0]
    ms12["takim2"] = getmacname(ms12["mac"])[1]
    ms21["takim1"] = getmacname(ms21["mac"])[0]
    ms21["takim2"] = getmacname(ms21["mac"])[1]
    ms22["takim1"] = getmacname(ms22["mac"])[0]
    ms22["takim2"] = getmacname(ms22["mac"])[1]
    return ms11,ms12,ms21,ms22
class ciftlimac:
    __slots__ = {"sira"}
    def __init__(self, sira):
        self.sira=sira
    def __lt__(self, other):
        return ciftlimac.compare(self, other)
    def __repr__(self):
        m1 = divmod(self.sira, 45)
        val1 = divmod(m1[0], 3)
        val2 = divmod(m1[1], 3)
        ms11 = {"mac": val1[0] + 1, "sonuc": val1[1]}
        ms12 = {"mac": val2[0] + 1, "sonuc": val2[1]}
        ms11["takim1"] = getmacnamek(ms11["mac"])[0]
        ms11["takim2"] = getmacnamek(ms11["mac"])[1]
        ms12["takim1"] = getmacnamek(ms12["mac"])[0]
        ms12["takim2"] = getmacnamek(ms12["mac"])[1]
        temp="""
        {0}-{1}->{2}
        {3}-{4}->{5}
        """
        return temp.format(ms11["takim1"],ms11["takim2"],ms11["sonuc"],ms12["takim1"],ms12["takim2"],ms12["sonuc"])
def askquestion(ms11,ms12,ms21,ms22):
    global times
    times = times + 1

    print(ms11,"\t\t",ms21)
    print(ms12, "\t\t", ms22)
    #whattoprint = teklifstring.format(" ", m11, m12, skor1, skor2, "-" * 20, "<<<-----", "----->>>", m21, m22)
    answer = getanswer("ilşkjlşj")
    return answer
def save(finished=True):
    with open("bin\\ciftlisquare.bin", "wb") as f:
        pickle.dump(ciftlisquare, f)
    with open("bin\\ciftlimarked.bin", "wb") as f:
        pickle.dump(ciftlimarked, f)
        if finished:
            print("Finished")
        print("Exiting...")
    sys.exit()
def compare(o1: ciftlimac, o2: ciftlimac):
    if o1.sira>o2.sira:
        return compare(o2,o1)
    place = o1.sira * (totalmac * 3)**2 + o2.sira
    if ciftlimarked[place]:
        return ciftlisquare[place]
    else:
        maclarsonuclar=getdictfromnumber(o1.sira,o2.sira)
        answer = askquestion(*maclarsonuclar)
        if answer == "quit":
            save(False)
        else:
            ciftlimarked[place] = True
            ciftlisquare[place] = answer
            return answer
ciftlimac.compare = compare
ciftlimaclar = []
for i in range(totalmac*3):
    deg=(int(i/3)+1)*3
    for a in range(deg,totalmac*3):
        if i!=a:
            ciftlimaclar.append(ciftlimac((i*totalmac*3)+a))
mergesort(ciftlimaclar)
print(ciftlimaclar)
save()
