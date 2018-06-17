from mergesort import mergesort
import pynput, sys, pickle, os.path
from key import getanswer
from readmatches import maclar, getmacname, getmacnamek
from bitarray import bitarray
from settings import totalmac, catikupon

times = 0
import random

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
if os.path.exists("bin\\teklisquare.bin") and os.path.exists("bin\\teklimarked.bin"):
    with open("bin\\teklisquare.bin", "rb") as f:
        teklisquare = pickle.load(f)
    with open("bin\\teklimarked.bin", "rb") as f:
        teklimarked = pickle.load(f)
else:
    teklisquare = bitarray((totalmac * 3) * (totalmac * 3))
    teklimarked = bitarray((totalmac * 3) * (totalmac * 3))
    teklisquare.setall(False)
    teklimarked.setall(False)


class teklimac:
    __slots__ = {"sira"}

    def __init__(self, x):
        self.sira = x

    def __lt__(self, other):
        return teklimac.compare(self, other)

    def __repr__(self):
        val1 = divmod(self.sira, 3)
        # print(val1)
        ms1 = {"mac": val1[0], "sonuc": val1[1]}
        m11 = getmacname(ms1["mac"])[0]
        m12 = getmacname(ms1["mac"])[1]
        return m11 + " - " + str(ms1["sonuc"]) + " - " + m12

    def getdictfromnumber(self):
        val1 = divmod(self.sira, 3)
        ms1 = {"mac": val1[0], "sonuc": val1[1]}
        return ms1


def complement(x: int):
    if x == 0:
        return "1 - 2"
    if x == 1:
        return "0 - 2"
    if x == 2:
        return "1 - 0"
    pass


def askquestion(first, second):
    ms1 = teklimac(first).getdictfromnumber()
    ms2 = teklimac(second).getdictfromnumber()
    m11 = getmacname(ms1["mac"])[0]
    m12 = getmacname(ms1["mac"])[1]
    m21 = getmacname(ms2["mac"])[0]
    m22 = getmacname(ms2["mac"])[1]
    skor1 = complement(ms1["sonuc"])
    skor2 = complement(ms2["sonuc"])
    whattoprint = teklifstring.format(" ", m11, m12, skor1, skor2, "-" * 20, "<<<-----", "----->>>", m21, m22)
    answer = getanswer(whattoprint)
    return answer


def returnplace(mac, sonuc):
    sira = (mac) * 3 + sonuc
    return teklimaclarsira[sira]


def save(finished=True):
    with open("bin\\teklisquare.bin", "wb") as f:
        pickle.dump(teklisquare, f)
    with open("bin\\teklimarked.bin", "wb") as f:
        pickle.dump(teklimarked, f)
    if finished:
        print("Finished")
    if "__name__" == "__main__":
        print("Exiting...")
        sys.exit()


def compare(o1: teklimac, o2: teklimac):
    if o1.sira > o2.sira:
        return not compare(o2, o1)
    """
    mac1=o1.getdictfromnumber()["mac"]
    sonuc1=o1.getdictfromnumber()["sonuc"]
    mac2=o2.getdictfromnumber()["mac"]
    sonuc2=o2.getdictfromnumber()["sonuc"]
    if catikupon[mac1+1].find(str(sonuc1))==-1 or catikupon[mac2 + 1]==str(sonuc2):
        print("found")
        return True
    if catikupon[mac2 + 1].find(str(sonuc2)) or catikupon[mac1 + 1]==str(sonuc1):
        print("found")
        return False
    """
    place = o1.sira * totalmac * 3 + o2.sira
    if teklimarked[place]:
        return teklisquare[place]
    else:
        answer = askquestion(o1.sira, o2.sira)
        if answer == "quit":
            save(False)
        else:
            teklimarked[place] = True
            teklisquare[place] = answer
            return answer
    return True


teklimac.compare = compare
teklimaclar = []
teklimaclarsira = list(range(totalmac * 3))
for i in range(totalmac * 3):
    ms = teklimac(i).getdictfromnumber()
    mac = ms["mac"]
    sonuc = ms["sonuc"]
    if catikupon[mac + 1].find(str(sonuc)) == -1:
        continue
    teklimaclar.append(teklimac(i))
# random.shuffle(teklimaclar)
mergesort(teklimaclar)
for a, k in enumerate(teklimaclar):
    teklimaclarsira[k.sira] = a

for a in teklimaclar:
    print(a)
save(True)
