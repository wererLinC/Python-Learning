'''
    读写csv的格式数据
'''

import csv
 # 进行数据的读
rf = open("books.csv")
reader = csv.reader(rf, delimiter=';')  # 传进去可迭代对对象，并且是以分号来进行分割
# 那我们拿到的也是可迭代对象，也就是有next的方法喽

# 那我们来进行数据的写

wf = open("demo.csv", 'w')
writer = csv.writer(wf, delimiter=' ')  # 以空格进行分割
writer.writerow(['x', 'y', 'z'])
writer.writerow([1, 2, 3])

