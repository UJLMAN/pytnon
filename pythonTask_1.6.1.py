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
        rez = ''
        flag = False
        if self.sl.get(str[1])!=None:
            sp  = self.sl.get(str[1])
            for i in range(len(sp)):
                if sp[i] == str[0]:
                    flag = True
                    break
            if flag:
                return 'Yes'
            else:
                if str[0]==str[1]:
                    return 'Yes'
                else:
                    for i in range(len(sp)):
                        if rez == 'Yes':
                            break
                        elif sp[i]=='None':
                            rez = 'No'
                        else:
                            rez = self.poisk(str[0]+sp[i])
                    return rez
        else:
            return  'No'


n = int(input())
Cl = Cls()
for i in range(n):
    str = input().split()
    Cl.add(str)
n = int(input())
rez = []

for i in range(n):
    str = input().split()
    rez.append(Cl.poisk(str))
for i in range(len(rez)):
    print(rez[i])
