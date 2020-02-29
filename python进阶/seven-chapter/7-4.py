# -*- coding: utf-8 -*-

import math

# 我们访问类的成员变量，我们用点的不方便进行操作，我们应该用get_radius 和 set_radius 来进操作
# 但是如果我们还是要进行.radius 或着 area 来进行操作的话，那我们就需要用property来进行操作的呀
#我们的property有两种实现方式，我们就可以一一来进行操作

class Cricle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        if not isinstance(self.radius, (int, float)):
            raise TypeError("wrong type")
        return self.radius

    def set_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("wrong type")
        self.radius = radius

    @property
    def S(self):
        return self.radius**2 * math.pi

    @S.setter
    def S(self, s):
        self.radius = math.sqrt(s/math.pi)

    R = property(get_radius, set_radius)


c = Cricle(5.1)
print(c.S)

