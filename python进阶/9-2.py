'''
    为原函数保留元数据,就是我们需要进行保留数据
'''
from functools import wraps

def memo(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        '''
        haha
        :return:
        '''
        pass
    return wrap

@memo
def xxx_func(a, b):
    '''
    这是func函数，可以解决很多中的事情
    :return:
    '''
    pass

print(xxx_func.__name__)
print(xxx_func.__doc__)
