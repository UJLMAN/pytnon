def bindev(koren,num,mas):
    flag = False
    spis = []
    rez = num+1
    for i in range(len(mas)):
        if mas[i]==koren:
            flag = True
            spis.append(i)
    if flag:
        rez = num+1
        for j in range(len(spis)):
            rez = bindev(spis[j],num+1,mas)
    return rez
n = int(input())
mas = []
num = 1
koren = 0
for i in range(n):
    x = int(input())
    mas.append(x)
    if x==-1:
        koren = i
rez = bindev(koren,num,mas)
print(rez)