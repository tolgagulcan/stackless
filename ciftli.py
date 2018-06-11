from mergesort import mergesort
import pynput,sys
from key import getanswer
import pickle
from stackless import tasklet,run
from readmatches import getmacnamek,getmacname

from readmatches import maclar


ciftlimackod=[]
from settings import totalmac,usetekli
deg=0
class ciftli:
    __slots__ = ("mac1","sonuc1","mac2","sonuc2")
    def __init__(self,mac1,sonuc1,mac2,sonuc2):
        self.mac1=mac1
        self.sonuc1=sonuc1
        self.mac2 = mac2
        self.sonuc2 = sonuc2
    def __repr__(self):
        sy="{0} - {1} -> {2}\n{3} - {4} -> {5}".format(getmacnamek(self.mac1)[0],getmacnamek(self.mac1)[1],self.sonuc1,getmacnamek(self.mac2)[0],getmacnamek(self.mac2)[1],self.sonuc2)

        return sy
    def __lt__(self, other):
        return ciftli.sorting(self,other)
fstring="""
{bos:^40}|{tercih1:^20}|||{tercih2:^20}|{bos:^40}
{bos:^40}|{bos:^20}|||{bos:^20}|{bos:^40}
{mac11:^40}|{sonuc11:^20}|||{sonuc21:^20}|{mac21:^40}
{bos:^40}|{bos:^20}|||{bos:^20}|{bos:^40}
{mac12:^40}|{sonuc12:^20}|||{sonuc22:^20}|{mac22:^40}
"""

times=0
def compare(d1:ciftli,d2:ciftli):
    if usetekli:
        from tekli import teklimackod, getindex
        i1=getindex(d1.mac1,d1.sonuc1)
        i2 = getindex(d1.mac2, d1.sonuc2)
        i3 = getindex(d2.mac1, d2.sonuc1)
        i4 = getindex(d2.mac2, d2.sonuc2)

        deg1 = i1 - i3
        deg2 = i2 - i4

        if deg1==0:
            return deg2<0

        if deg2==0:
            return deg1<0



        if (deg1 > 0 and deg2 > 0):
            return False

        if (deg1 < 0 and deg2 < 0):
            return True

    #return True
    global times
    times=times+1
    mac11=str(getmacname(d1.mac1))
    mac12 = str(getmacname(d1.mac2))
    
    mac21=str(getmacname(d2.mac1))
    mac22 = str(getmacname(d2.mac2))
    
    sonuc11=d1.sonuc1
    sonuc12=d1.sonuc2
    
    sonuc21=d2.sonuc1
    sonuc22=d2.sonuc2

    adict={"bos":" ","tercih1":"Seçenek 1","tercih2":"Seçenek 2","mac11":mac11,"mac12":mac12,"mac21":mac21,"mac22":mac22,"sonuc11":sonuc11,"sonuc12":sonuc12,"sonuc21":sonuc21,"sonuc22":sonuc22}

    whattoprint = fstring.format(**adict)



    ans1=getanswer(whattoprint)
    #ans2=getanswer(whattoprint)
    #if ans1==ans2:
        #return ans1
    #return getanswer()
    return ans1
ciftli.sorting=compare
secondmackod=[]
for i in range(1,totalmac+1):
    for a in range(i+1,totalmac+1):
        o1 = ciftli(i, 1, a, 1)
        o2 = ciftli(i, 1, a, 0)
        o3 = ciftli(i, 1, a, 2)
        o4 = ciftli(i, 0, a, 1)
        o5 = ciftli(i, 0, a, 0)
        o6 = ciftli(i, 0, a, 2)
        o7 = ciftli(i, 2, a, 1)
        o8 = ciftli(i, 2, a, 0)
        o9 = ciftli(i, 2, a, 2)

        ciftlimackod.append(o1);ciftlimackod.append(o2);ciftlimackod.append(o3);
        ciftlimackod.append(o4);ciftlimackod.append(o5);ciftlimackod.append(o6);
        ciftlimackod.append(o7);ciftlimackod.append(o8);ciftlimackod.append(o9);





mergesort(ciftlimackod)

print(times)
print(len(ciftlimackod))

