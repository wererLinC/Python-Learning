# -*- coding: utf-8 -*-

# 现在比如我们需要呢，返回一个int类型且是大于零的tuple的元组
# 我们可以发现用__init__ 来进行操作是不行的，应次这里我们需要用到__new__()函数


class IntTuple(tuple):
    
    def __new__(cls, iterable):
        f_t = (e for e in iterable if isinstance(e, int) and e >= 0)
        return super().__new__(cls, f_t)


int_t = IntTuple([-1, 2, 3, 'abc'])
print(int_t)
