# -*- coding: utf-8 -*-

'''
    现在我们来重载一下运算符的操作
    因为我们不想实现所有的[>,< ==,<=,<=]所以我们引进total_ordering
    来进行辅助一下，那我们现在的需求还有就是对于不同类之间也要进行操作
    那我们还需要引进ABCMeta和abstractclassmethod来进行操作
'''

import math
from functools import total_ordering
from abc import ABCMeta, abstractclassmethod

@total_ordering
class shape:
    @abstractclassmethod
    def area(self):
        pass

    def __lt__(self, obj):
        return self.area() < obj.area()
    def __eq__(self, obj):
        return self.area() == obj.area()


class Rect(shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

    def __str__(self):
        return 'Rect:(%s, %s)' % (self.w, self.h)

class Cricle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius**2 * math.pi 


rect1 = Rect(6, 9)
rect2 = Rect(8, 9)
cricle = Cricle(6)

print(rect1 < rect2)
print(cricle > rect2)
