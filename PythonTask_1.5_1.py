class MoneyBox:
    def __init__(self,capacity=0):
        self.money = 0
        self.capacity = capacity
    def can_add(self,v):
        if self.money+v>self.capacity:
            return False
        else:
            return True
    def add(self,v):
        if self.can_add(v):
            self.money+=v
x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)
print(x.money)