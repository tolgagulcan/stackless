compnumber = [0]


def mergesort(ls):
    if (len(ls) < 2):
        return ls
    else:
        k = len(ls) // 2
        ls1 = mergesort(ls[0:k])
        ls2 = mergesort(ls[k:len(ls)])
        merge(ls1, ls2, ls)
        return ls


def merge(ls1, ls2, ls):
    total = len(ls1) + len(ls2)
    f1 = 0
    f2 = 0
    for i in range(total):
        if (f1 == len(ls1)):
            ls[i] = ls2[f2]
            f2 = f2 + 1
            continue
        if (f2 == len(ls2)):
            ls[i] = ls1[f1]
            f1 = f1 + 1
            continue
        compnumber[0] = compnumber[0] + 1
        if ls1[f1] < ls2[f2]:
            ls[i] = ls1[f1]
            f1 = f1 + 1
        else:
            ls[i] = ls2[f2]
            f2 = f2 + 1
