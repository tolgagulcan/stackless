from mergesort import mergesort
import pynput,sys,pickle,os.path
from key import getanswer
from readmatches import maclar
from bitarray import bitarray
from settings import totalmac

if os.path.exists("bin\\teklisquare.bin") and os.path.exists("bin\\teklimarked.bin"):
    with open("bin\\teklisquare.bin","rb") as f:
        teklisquare=pickle.load(f)
    with open("bin\\teklimarked.bin","rb") as f:
        teklimarked = pickle.load(f)
else:
    teklisquare=bitarray((totalmac*3)*(totalmac*3))
    teklimarked=bitarray((totalmac*3)*(totalmac*3))
    teklisquare.setall(False)
    teklimarked.setall(False)

class teklimac:
    __slots__ = {"sira"}
    def __init__(self,x):
        self.sira=x
    def __lt__(self, other):
        return teklimac.compare(self,other)
    def __repr__(self):
        return str(self.sira)

def askquestion(first,second):
    return False

def save(finished=True):
    with open("bin\\teklisquare.bin", "wb") as f:
        pickle.dump(teklisquare, f)
    with open("bin\\teklimarked.bin", "wb") as f:
        pickle.dump(teklimarked, f)
        if finished:
            print("Finished")
        print("Exiting...")
        sys.exit()


def compare(o1:teklimac,o2:teklimac):

    first=min(o1.sira,o2.sira)
    second=o1.sira+o2.sira-first

    place=first*45+second
    print(place)
    if teklimarked[place]:
        return teklisquare[place]
    else:
        answer=askquestion(first,second)
        if answer=="quit":
            save(False)

        else:
            return answer
    return True


teklimac.compare=compare
maclar=[]
for i in range(45):
    maclar.append(teklimac(i))

mergesort(maclar)

print(maclar)
print(teklisquare)
print(teklimarked)
save()