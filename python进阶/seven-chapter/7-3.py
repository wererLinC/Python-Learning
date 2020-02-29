# -*- coding: utf-8 -*-

# 根据上下文来管理
'''
    with tf.Session() as sess:
        sess.run()
    类似于这样的，我们会很经常看到，就是在里面，我们运行完就会进行close
'''

from sys import stdin, stdout #引进输入输出
import getpass 
import telnetlib
from collections import deque # 引进双端队列

class TelnetClient:
    def __init__(self, host, port=23):
        self.host = host
        self.port = port
    
    def __enter__(self):
        self.tn = telnetlib.Telnet(self.host, self.port)
        self.history = deque([])
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('IN__exit__', exc_type, exc_value, exc_tb)
        self.tn.close()
        self.tn = None

        with open('history.txt', 'a') as f:
            f.writelines(self.history)


    def login():
         #user
        self.tn.read_until(b"login:")
        user = input("Enter your remote account : ")
        self.tn.write(user.encode('utf8') + b'\n')

        #password
        self.tn.read_unitl(b"Password: ")
        password = getpass.getpass()
        self.tn.write(password.encode('utf8') + b'\n')
        out = self.tn.read_until(b'$')
        stdout.write(out.decode('utf8'))

    def interact(self):
        while True:
            cmd = stdin.readline()
            if not cmd:
                break

            self.history.append(cmd)
            self.tn.write(cmd.encode('utf8'))
            out = self.tn.read_until(b'$').decode('utf8')

            stdout.write(out[len(cmd) + 1:])
            stdout.flush()


with TelnetClient('127.0.0.1') as client:
    #raise Exception('Test')
    client.login()
    client.interact()

print('END')

            
            
