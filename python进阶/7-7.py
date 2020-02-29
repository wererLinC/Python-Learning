# # 现在我们来进行一下函数的删除的虚构函数
#
# class A:
#     def __del__(self):
#         print("in __del__")
#
#
# a = A()
# b = a
# b = None
# a =1 # 现在我们没有引用A的类型，现在应该就是del的方法里面了，正如我们所料，现在我们来进行下一次的测试吧
# weakref 弱引用类型，来进行删除的操作的啦

import weakref

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self._left = None

    @property
    def left(self):
        return self._left()

    def add_right(self, node):
        self.right = node
        node._left = weakref.ref(self)

    def __str__(self):
        return 'Node<%s>' % self.data

    def __del__(self):
        return 'in __del__: delete %s' % self


def create_linklist(n):
    head = current = Node(1)
    for i in range(2, n+1):
        node = Node(i)
        current.add_right(node)
        current = node
    return head


head = create_linklist(10000)
print(head.right, head.right.left)
head = None

# 我们来测试一下看是否会进行到del的方法内来进行操作的呀
import time

for _ in range(1000):
    time.sleep(1)
    print("run……")
input("wait……")
