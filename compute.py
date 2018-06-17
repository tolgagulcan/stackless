import random
from settings import totalmac, catikupon
from ciftliyeni import ciftlimac, ciftlimaclar


def hesapla(hlist: list, hatamax: int, howmany: int):
    hatalar = {}
    for i in range(howmany):
        hatalar["-".join((str(x) for x in hlist[i].getdictfromnumber()))] = True
    return start(hatalar, hatamax, level=0, sonuc=0, hata=0) + start(hatalar, hatamax, level=0, sonuc=1,
                                                                     hata=0) + start(hatalar, hatamax, level=0, sonuc=2,
                                                                                     hata=0)


hlist = list(range(10))
currmac = list(range(totalmac))


def start(hatalar: dict, hatamax, level=0, sonuc=0, hata=0):
    if catikupon[level + 1].find(str(sonuc)) == -1:
        return 0
    currmac[level] = sonuc
    for i in range(level):
        lookup = "-".join(str(x) for x in (str(i), currmac[i], str(level), str(sonuc)))
        if hatalar.get(lookup, False):
            hata = hata + 1
            if hata > hatamax:
                return 0
    if level == totalmac - 1 and hata <= hatamax:
        return 1
    return start(hatalar, hatamax, level=level + 1, sonuc=0, hata=hata) + start(hatalar, hatamax, level=level + 1,
                                                                                sonuc=1,
                                                                                hata=hata) + start(hatalar, hatamax,
                                                                                                   level=level + 1,
                                                                                                   sonuc=2,
                                                                                                   hata=hata)


print(hesapla(ciftlimaclar, hatamax=0, howmany=4))
