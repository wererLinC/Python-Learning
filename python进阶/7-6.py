'''
    我们需要对输入的类型进行判断，因此我们需要在传进去参数时要进行字符判断
'''
class Attr:
    def __init__(self, key, type_):
        self.key = key
        self.type_ = type_

    def __set__(self, instance, value):
        print("in __set__")
        if not isinstance(value, self.type_):
            raise TypeError('must be %s' % self.type_)
        instance.__dict__[self.key] = value

    def __get__(self, instance, cls):
        print("in __get__")
        return instance.__dict__[self.key]

    def __del__(self, instance):
        print("in __del__")
        del instance.__dict__[self.key]

class Person:
    name = Attr('name', str)
    age = Attr('age', int)

p = Person()
p.name = 'weierlin'
p.age = '12'
