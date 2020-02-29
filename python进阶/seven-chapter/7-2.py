# -*- coding: utf-8 -*-

# 现在比如我们需要进行N个用户的实例，那我们怎么进行来空间的节省呢
# 这样我们就可以用__slots__ 来进行操作的呀

# 现在这个要求可以进行动态添加属性
class Player1:
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name= name
        self.level = level


# 这个就不能进行动态添加属性
class Player2:
    __slots__ = ['uid', 'name', 'level']
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name= name
        self.level = level

# 现在进行测试，到底两种有啥区别的呢
# 现在引进tracemalloc来跟踪一下内存的事情

import tracemalloc
tracemalloc.start()
#la = [Player1(1, 2, 3) for _ in range(100000)]
lb = [Player2(1, 2, 3) for _ in range(100000)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')
for stat in top_stats:
    print(stat)

