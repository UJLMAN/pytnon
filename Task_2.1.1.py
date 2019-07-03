def fill():
    spis = []
    if len(z) == 1:
        if cl.get(z[0])==None:
            cl[z[0]] = [None]
    else:
        znach = z[0]
        for  i in range(1,len(z)):
            if z[i]!=":":
                spis.append(z[i])
        if cl.get(znach)==None:
            cl[znach] = spis
        else:
            for i in range(cl.get(znach)):
                spis.append(cl.get(znach)[i])
                cl[znach] = spis
cl = {}
n = int(input())
for i in range(n):
    z = input().split()
    fill()