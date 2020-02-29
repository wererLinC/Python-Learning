'''
    例如我们现在要求一个斐波那契数列 1 1 2 3 5 8
    求数列第n项的值
    但是我们发现我们所求的重复的值是很多的
    所以我们可以设置一个缓存来处理一下，来加快一下速度
'''
import time

# 那么现在我们来构建一个装饰器来进行操作,下面会形成一个闭包
def memo(func):
    cache = {}
    def swap(*args):  # 这里我们不局限于只有一个参数，我们可以接收多参数的
        res = cache.get(args)
        if not res:
            res = cache[args] = func(*args)
        return res
    return swap

@memo
def fabonacci(n):
    if n <= 1:
        return 1
    return fabonacci(n-1) + fabonacci(n-2)

if __name__ == '__main__':

    begin = time.time()
    res = fabonacci(40)
    end = time.time()
    print("法1 total time : ", (end-begin))
    print('\n', res)

