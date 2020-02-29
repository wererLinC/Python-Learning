'''
    正则表达式入门第一步
'''

import re

# 现在我们的需求是要找到所有的数字,下面两个都可以的，建议取看一下正则表达式的匹配规则
s = '01cdsfd'
digits = re.findall('\d', s)
digits = re.findall('[0-9]', s)
# print(digits)

# 字符集，中间有一个字母是c或者f的字符串
s = 'abc, acd, afd'
r = re.findall('a[cf]d', s)
# print(r)


# 数量词
st = 'python 111java C++ php'
st = re.findall('[a-z]{3,6}', st)  # {}是匹配的数量词，表示我们可以匹配几次，
# print(st)

# 贪婪和非贪婪【python中re默认是贪婪的， 如果要非贪婪的要加上?】
st = 'python 111java C++ php'
st = re.findall('[a-z]{3,6}?', st)  # {}是匹配的数量词，表示我们可以匹配几次，
# print(st)

# 数量词，匹配0次或者无线多次
# * 匹配0次或者无限多次
# + 匹配一次或者无限多次
# ？匹配0次或者1次
s = 'pytho1python2pythonn3'
# stt = re.findall('python*', s)  # 现在我们* 可以匹配0次或者无限多次
stt = re.findall('python+', s)  # 只能匹配1次或者无限多次的
# print(stt)

# 边界的匹配 [^ : 表示从开始进行匹配 $ : 表示从末尾进行匹配] => 这样我们就可以匹配所有的东西了，是不是很神奇呀
qq = '1661590912'
r = re.findall('^\d{7,11}$', qq)
# if(len(r) > 0):
#     print('qq登录成功')

# 组的概念
s = 'abcabcabcabc'
r = re.findall('(abc){3}', s)  # 表示abc是为一组的，且出现3次
# print(r)

# 匹配模式下参数 re.I : 表示忽略大小写 re.S 改变.的行为
# . 表示出了空白字符之外的其他字符都可以进行匹配

lanuage = 'pythonC#\nJava'
r = re.findall('c#.{1}', lanuage, re.I | re.S)
# print(r)

# sub 正则替换
lanuage = 'pythonC#\nJava'
res = re.sub('C#', 'GO', lanuage, 0)  # 最后一个参数表示，0代表全部， 1代表1个，以此类推
# print(res)

# 函数作为参数传进去sub中去
lanuage = 'pythonC#JavaC#phpC#'

def convert(value):
    matched = value.group()  # 可以获取到所有的value的值
    return '!!' + matched + '!!'


res = re.sub('C#', convert, lanuage, 0)  # 全部替换
# print(res)

# 进一步进行探索, 现在我们要对id进行处理，如果数字大于等于6的替换成9， 小于6的替换成1
id = '112sds3467878'
def convert_one(value):
    marthed = value.group()  # 需要特别注意，我们的返回的必须是字符串类行的，这点我们需要注意一下的额
    if int(marthed) > 6:
        return '1'
    else:
        return '9'

res = re.sub('\d', convert_one, id, 0)
# print(res)

# re 里面的match 和 search 匹配到就会马上停下，不会进行下一次的操作
# match 从开始就进行匹配，没有则返回None
# search 则全部进行匹配， 且返回遇到一次就会退出的

#
















