'''
    将文件映射到内存中去
'''

import mmap  # 有个同名的函数来进行操作
m = mmap.mmap(f.fileno(), 0)  # 0 表示全文件都要
