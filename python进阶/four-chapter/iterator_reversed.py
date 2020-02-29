from decimal import Decimal
class FloatRange:
    #进行初始化的操作
    def __init__(self, a, b, step=1):
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))
        self.step = Decimal(str(step))

    #进行正向迭代
    def __iter__(self):
        t = self.a
        while t <= self.b:
            yield t
            t += self.step

    #进行反向迭代
    def __reversed__(self):
        t = self.b
        while t >= self.a:
            yield t
            t -= self.step

fr = FloatRange(3.0, 4.0, 0.2)
for x in fr:
    print(x)

print('*' * 20)

for x in reversed(fr):
    print(x)

