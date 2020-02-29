'''
    解析xml文档
'''

from xml.etree import ElementTree

et = ElementTree.parse('demo.xml')  # 从文件中打开
ElementTree.fromstring()  # 从大字符串中打开

root = et.getroot()  # 获取根元素
root.tag  # 获取标签
root.attrib  # 获取到属性，例如里面有name属性或者啥的
root.getchildren()  # 获取到子元素，不推荐这样，是一个可迭代的
list(root)  # 变成一个列表，可以用索引进行查找的
list(root)[1].text  # 可以获取到里面的文本

year = list(root)[1]
year.tail  # 可以获取到后面的文本的呀

c1.find('元素')  # 找到子元素
list(c1.iter('元素'))  # 返回所有树中的元素

c1.itertext()  # 可以得到所有的文本文件












