import sys
def bindev(koren):
    heigth = 1
    sps = sl.get(koren)
    if sps!=None:
        for i in range(len(sps)):
            a = 1+bindev(sps[i])
            if heigth<a:
                heigth = a
    return heigth
n = int(input())
if 1<=n<=10**5:
    mas = []
    koren = 0
    x = input().split()
    sl = {}
    sys.setrecursionlimit(20000)
    for i in range(n):
        mas = []
        if sl.get(int(x[i]))!=None:
            mas = sl.get(int(x[i]))
            mas.append(i)
            sl[int(x[i])] = mas
        else:
            mas.append(i)
            sl[int(x[i])] = mas
        if int(x[i])==-1:
            koren=i
    rez = bindev(koren)
    print(rez)
else:
    print("Error")









