class Buffer:
    def __init__(self):
        self.spis = []

    def add(self, *a):
        sum = 0
        ip  = 0
        sp = []
        for i in range(len(a)):
            self.spis.append(a[i])
        if len(self.spis)>=5:
            for i in range(len(self.spis)):
                sum+=self.spis[i]
                if (i+1)%5==0:
                    print(sum)
                    sum = 0
                    ip = i+1
            if ip<len(self.spis):
                for i in range(ip,len(self.spis)):
                    sp.append(self.spis[i])
            self.spis = sp
    def get_current_part(self):
        return self.spis
x = Buffer()
x.add(1,2,3)
x.get_current_part()
x.add(4,5,6)
x.get_current_part()
x.add(7,8,9,10)
x.get_current_part()