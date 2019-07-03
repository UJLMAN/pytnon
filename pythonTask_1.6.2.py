class ExtendedStack(list):
    def op(self):
        if len(self)>=2:
            return True
        else:
            return False

    def sum(self):
        if self.op:
            a = self.pop()
            b = self.pop()
            self.append(a+b)


    def sub(self):
    # операция вычитания
        if self.op:
            a = self.pop()
            b = self.pop()
            self.append(a-b)

    def mul(self):
    # операция умножения
        if self.op:
            a = self.pop()
            b = self.pop()
            self.append(a*b)

    def div(self):
# операция целочисленного деления
        if self.op:
            a = self.pop()
            b = self.pop()
            self.append(a//b)



ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
ex_stack.div()
ex_stack.sub()
ex_stack.sum()
ex_stack.mul()
print(*ex_stack)
