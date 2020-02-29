'''
    临时文件来进行操作
'''

from tempfile import TemporaryFile, NamedTemporaryFile
tf = TemporaryFile(dir='')  # 实例化出来就可以啦，在运行完之后就会释放，可以用dir来指定目录来进行操作

ntf = NamedTemporaryFile()  # 也可以添加前缀和后缀来进行指定吧
ntf.name()  # 可以指定目录
