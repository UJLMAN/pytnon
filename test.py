import sys
def bindev(koren,num,mas):
    flag = False
    spis = []
    for i in range(len(koren)):
        for j in range(len(mas)):
            if koren[i]==mas[j]:
                spis.append(j)
    if len(spis)!=0:
        num+=1
        num = bindev(spis,num,mas)
    return num
n = int(input())
mas = []
num = 1
koren = []
sys.setrecursionlimit(10000)
x = input().split()
for i in range(n):
    mas.append(int(x[i]))
    if int(x[i])==-1:
        koren.append(i)
rez = bindev(koren,num,mas)
print(rez)




