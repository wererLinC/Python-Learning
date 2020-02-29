'''
    python3 处理二进制文件
    我们呢的需求是采集头部信息，然后对音频信息进行处理
'''
#
import struct
# # with open('J:/BaiduNetdiskDownload/01 光辉岁月.wav', 'rb') as f:
# #     f.read()
#
# f = open('J:\BaiduNetdiskDownload\光辉岁月.wav', 'rb')
# f_info = f.read()
# head_info = f_info[0: 242]
# f.seek(0) # 指完我们先跳回去到开始的地方
# data = f_info[242:]
#
# size = struct.unpack('h', data)
# print(size)

# 因为每个文件得到的data的偏移量是不一样的，所以我们需要进行函数的编程来查找的
def find_subchunk(f, name):
    f.seek(12)  # 表头是确定的12个
    while True:
        chunk_name = f.read(4)
        chunk_size, = struct.unpack('i', f.read(4))  # , 作用进行拆包呀

        if chunk_name == name:
            return f.tell(), chunk_size  # 如果找到了，我们就返回偏移量和chunk_size的大小

        f.seek(chunk_size, 1)  # 如果不是我们要找的data，我们文件的指针就当前往前跳chunk_size个大小的字节

import numpy as np

with open('J:\BaiduNetdiskDownload\光辉岁月.wav', 'rb') as f:
    offset, size = find_subchunk(f, b'data') # 找到data已经进行了偏移了
    print(offset, size)
    buf = np.zeros(size//2, dtype=np.short)
    f.readinto(buf)  # 把文件写进去buf当中去
    buf //= 8
    f2 = open('J:\BaiduNetdiskDownload\光out.wav', 'wb')
    f.seek(0) # 重新跳回首部
    f2.write(f.read(offset))
    # 现在我们来进行写数据啦
    buf.tofile(f2) # 我们直接写进去文件当中去
    f2.close()


