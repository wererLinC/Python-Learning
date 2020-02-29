'''
    excel文件的操作
    需要先引进xlrd xlwt 对应读和写
'''

import xlrd
import xlwt


book = xlrd.open_workbook('文件')  # 打开某个文件
sheet = book.sheet_by_index(0)  # 获取到第一sheet的对象

sheet.nrows  # 多少行
c = sheet.cell(0, 0)  # 第一行第一列的对象
sheet.cell_value()  # 得到value的值
c.type  # c的类型
c.value  # c的值
sheet.row(0)  # 取整行，第0行
sheet.row_values(1, 1)  # 取第一行的值,第二个参数表示从第几列开始
sheet.put_cell(0, ncols, xlrd.XL_CELL_TEXT, '总分', None)  # 添加新的元素，参数对应：行，列，类型


# 写操作
import xlwt

wbook = xlwt.Workbook()  # 创建一个工作区间
wsheet = wbook.add_sheet('test')  # 与上面想对应，我们添加sheet
wsheet.write(0, 0, 'abc')  # 在第0行第一列写进去abc
wsheet.write(0, 1, 100)
wbook.save('test.xlsx')  # 保存为test名的文件

