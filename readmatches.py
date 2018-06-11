maclar=[]


with open("maclar.txt") as f:
    for line in f:
        line=line.strip()
        tk=line.split()
        tup=(tk[0].strip(),tk[1].strip())
        maclar.append(tup)

def getmacname(kod:int):
    return (maclar[kod-1][0],maclar[kod-1][1])

def getmacnamek(kod:int,i:int=5):
    a=getmacname(kod)
    return (a[0][0:i],a[1][0:i])

if __name__=="__main__":
    for a in range(1,16):
        print(getmacnamek(a))
