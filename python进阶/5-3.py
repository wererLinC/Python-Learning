'''
    文件的缓冲啦
    【全缓冲、行缓冲、无缓冲】
    我们可以在Linux里面用tail来和跟踪一下
'''

open('test', 'w', buffering=4096)  # 自己设置缓冲
open('test', 'w', buffering=0)  # 无缓冲
open('test', 'w', buffering=1)  # 行缓冲 => 只能用在txt文本中




