from itertools import islice

#用自己写的方法进行玩耍
def iterator_slice(iterable, start, end, step=1):
    temp = 0
    for i, x in enumerate(iterable):
        if i >= end:
            break
        if i >= start:
            if temp == 0:
                temp = step
                yield x
            temp -= 1

print(list(islice(range(1, 100), 5, 10, 2)))
print(list(iterator_slice(range(1, 100), 5, 10, 2)))
