class Cls:
    def __init__(self):
        self.sl = {}

    def add(self,str):
        sp = []
        if len(str)>1:
            for i in range(len(str)):
                if str[i]!=":":
                    if i !=0:
                        sp.append(str[i])
            if self.sl.get(str[0])==None:
                self.sl[str[0]] = sp
        else:
            if self.sl.get(str[0])==None:
                sp.append('None')
                self.sl[str[0]] = sp
    def poisk(self,str):
        sp = []
        flag = False
        if self.sl.get(str[1])!=None:
            sp  = self.sl.get(str[1])
            for i in range(len(sp)):
                if sp[i] == str[0]:
                    flag = True
                    break
            if flag:
                print('Yes')
            else:
                if str[0]==str[1]:
                    print('Yes')
                else:
                    for i in range(len(sp)):
                        self.poisk(str[0]+sp[i])
        else:
            print('No')

n = int(input())
Cl = Cls()
for i in range(n):
    str = input()
    Cl.add(str.replace(' ',''))
n = int(input())
rez = ''
for i in range(n):
    str = input()
    Cl.poisk(str.replace(' ',''))
