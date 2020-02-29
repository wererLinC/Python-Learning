'''
     使用单线程来进行下载任务
'''

import requests  # 现在我们都用这个来，而不是用urllib来做了
import base64
from io import StringIO  # 磁盘IO
import csv
from xml.etree.ElementTree import ElementTree, Element, SubElement  # 把csv 转化成xml

USERNAME = b'7f304a2df40829cd4f1b17d10cda0304'
PASSWORD = b'aff978c42479491f9541ace709081b99'

def download_csv(page_number):
    print('download csv data [page=%s]' % page_number)
    url = "http://api.intrinio.com/prices.csv?ticker=AAPL&hide_paging=true&page_size=200&page_number=%s" % page_number
    auth = b'Basic ' + base64.b64encode(b'%s:%s' % (USERNAME, PASSWORD))
    headers = {'Authorization': auth}
    response = requests.get(url, headers=headers)

    if response.ok:
        return StringIO(response.text)

def csv_to_xml(csv_file, xml_path):
    print('Convert csv data to %s' % xml_path)
    reader = csv.reader(csv_file)
    headers = next(reader)

    root = Element('Data')
    root.text = '\n\t'
    root.tail = '\n'

    for row in reader:
        book = SubElement(root, 'Row')
        book.text = '\n\t\t'
        book.tail = '\n\t'

        for tag, text in zip(headers, row):
            e = SubElement(book, tag)
            e.text = text
            e.tail = '\n\t\t'
        e.tail = '\n\t'

    ElementTree(root).write(xml_path, encoding='utf8')

def download_and_save(page_number, xml_path):
    # IO
    csv_file = None
    while not csv_file:
        csv_file = download_csv(page_number)
    # CPU
    csv_to_xml(csv_file, 'data%s.xml' % page_number)

# 写一个进程的class来进行多线程下载任务啦
from threading import Thread
class MyThread(Thread):
    def __init__(self, page_number, xml_path):  # 现在我们是class的对象，所以我们用init来初始化
        super().__init__()  # 调用父类的方法，但是不用传进去任何参数的啦
        self.page_number = page_number
        self.xml_path = xml_path

    def run(self):  # run方法来运行我们的方法啦
        download_and_save(self.page_number, self.xml_path)

if __name__ == '__main__':
    import time
    t0 = time.time()
    thread_list = []
    for i in range(1, 6):
        t = MyThread(i, 'data%s.xml' % i)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()
    # for i in range(1, 6):
    #      download_and_save(i, 'data%s.xml' % i)
    print(time.time() - t0)
    print('main thread end.')
