'''
    python3 对文本文件的读写
    python2 对文本进行读写，我们需要对编码解码对应的类型要一样的
'''

s = '我是weierlin'

with open('b.txt', 'r', encoding='utf8') as f:
    f.read()

