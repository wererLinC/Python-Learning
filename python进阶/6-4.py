'''
    构建xml文档
'''

import xml.etree.ElementTree as ET

data = ET.Element('Data')
book = ET.Element('Book')
author = ET.Element('作者')
book.set('x', 'abc')  # 给 book 添加属性
author.text = '陈伟林'
# 给数结构
data.append(book)  # 把book 给data作为儿子
book.append(author)

ET.dump(data)  # 打印出来就行了呀

# 还有一种方法来进行操作

book = ET.SubElement(data, 'Book')
author = ET.SubElement(data, '作者')
ET.dump(data)  # 输出的结果是一样的

et = ET.ElementTree(data)  # 做一个tree的元素

et.write('test.xml', encoding='utf8')  # 写进去test的文本文件




