from mergesort import mergesort
import pynput,sys
from key import getanswer
import pickle
from stackless import tasklet,run
from readmatches import maclar

teklimackod=[]
from settings import totalmac
deg=0
class tekli:
    __slots__ = ("mac","sonuc")
    def __init__(self,mac,sonuc):
        self.mac=mac
        self.sonuc=sonuc
    def __repr__(self):
        return str((self.mac,self.sonuc))
    def __lt__(self, other):
        return tekli.sorting(self,other)
fstring="""
{0:^40}|{1:^20}|{2:^20}
{3:^40}|{4:^20}|{5:^20}
{6:^40}|{7:^20}|{8:^20}
{9:^40}|{10:^20}|{11:^20}
{12:^40}|{13:^20}|{14:^20}
"""
fstring2="""
{0:^40}|{1:^20}|{2:^20}
{3:^40}|{4:^20}|{5:^20}
{6:^40}|{7:^20}|{8:^20}
"""
def compare(d1:tekli,d2:tekli):
    mac1=maclar[d1.mac-1][0]+" - "+maclar[d1.mac-1][1]
    mac2 = maclar[d2.mac - 1][0]+" - "+maclar[d2.mac-1][1]
    s1=d1.sonuc
    s2=d2.sonuc
    t1=""
    if s1==0:
        t1="1-2"
    elif s1==1:
        t1="0-2"
    else:
        t1="1-0"
    t2=""
    if s2==0:
        t2="1-2"
    elif s2==1:
        t2="0-2"
    else:
        t2="1-0"

    if d1.mac!=d2.mac:
        whattoprint=fstring.format(" ","Secenek 1","Secenek 2"," "," "," ",mac1,s1,t1," "," "," ",mac2,t2,s2)
    else:
        whattoprint = fstring2.format(" ", "Secenek 1", "Secenek 2", " ", " ", " ", mac1, s1, s2)
    whattoprint = fstring2.format(" ", "Secenek 1", "Secenek 2", " ", " ", " ", mac1, s1, s2)
    whattoprint = fstring.format(" ", "Secenek 1", "Secenek 2", " ", " ", " ", mac1, s1, t1, " ", " ", " ", mac2, t2,
                                 s2)


    #ans1=getanswer(whattoprint)
    #ans2=getanswer(whattoprint)
    #if ans1==ans2:
        #return ans1
    return getanswer(whattoprint)
tekli.sorting=compare
secondmackod=[]
for i in range(1,totalmac+1):
    o1=tekli(i,1)
    o2=tekli(i,0)
    o3=tekli(i,2)
    teklimackod.append(o1)
    teklimackod.append(o2)
    teklimackod.append(o3)

    secondmackod.append(o1)
    secondmackod.append(o2)
    secondmackod.append(o3)


mergesort(teklimackod)

def findobject(kod,sonuc):
    deg=0
    if sonuc==0:
        deg=1
    elif sonuc==2:
        deg=2
    return secondmackod[(kod-1)*3+deg]

def getindex(kod,sonuc):
    return teklimackod.index(findobject(kod,sonuc))
if __name__=="__main__":
    print(teklimackod)

    print("")