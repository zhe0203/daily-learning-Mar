# -*- coding: utf-8 -*-

# StringIO 在内存中读写str
from io import StringIO
f = StringIO()
f.write('hello')
f.write('\n')
f.write('world!')
print(f.getvalue())   # getvalue方法用于获得写入后的str

## 读取
f = StringIO('hello\nhi!\ngoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# 如果要操作二进制数据，就需要使用BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())    # 此处写入的不是str，而是经过UTF-8编码的bytes
## 和stringIO类似，可以用一个bytes初始化BytesIO然后想读取文件一样读取
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# 操作文件和目录
import os
print(os.name)    # 操作系统类型  nt表示windows
# print(os.uname())   # 获取详细的系统信息，注在Windows上不提供该函数
print(os.environ)     # 在操作系统中定义的环境变量
print(os.environ.get('PATH'))   # 获取某个环境变量的值

# 操作文件和目录
## 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
print(os.path.abspath('.'))   # 查看当前目录的绝对路径

# 在某一个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.path.join('C:/Users/jk/Desktop/Python学习','testdir')
# 然后创建一个目录
# os.mkdir('C:/Users/jk/Desktop/Python学习/testdir')
# os.rmdir('C:/Users/jk/Desktop/Python学习/testdir')   # 删掉一个目录

# 要把两个路径合并成一个时，不要直接拼字符串，使用os.path.join函数
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
print(os.path.split('/Users/michael/testdir/file.txt'))
# splitext函数可以直接让你得到文件扩展名
print(os.path.splitext('/Users/michael/testdir/file.txt'))

# os.rename('test.txt','test.py')   # 对文件进行重命名
# os.remove('test.py')              # 删除文件

# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

# 列出当前目录下所有的文件
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 要列出所有的.py文件，也只需一行代码
# print([x for x in os.path.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# os.getcwd()    # 返回当前python脚本的目录路径
# os.listdir()   # 返回指定目录下的所有文件和目录名
# os.remove()  # 用来删除一个文件
# os.path.isfile()   # 判断是否为文件
# os.path.isdir()   # 判断是否为目录
# os.listdir(dirname)   # 列出dirname下的目录和目录
# os.psth.getsize()   # 返回文件的大小

# 序列化 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
import pickle
d = dict(name='Bob',age=20,score=88)
print(pickle.dumps(d))        # 把任意对象序列化成一个bytes
f = open('dump.txt','wb')
pickle.dump(d,f)     # 直接把对象序列化写入一个文件
f.close()

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)

# json
import json
d = dict(name='bob',age=20,score=88)
# dump()方法可以直接把JSON写入一个file-like Object
print(json.dumps(d))    # dumps是将字典数据转换为json标准的数据格式

# 要把json反序列化为python对象，用loads或者对应的load方法
# 前者把json的字符串反序列化，后者从file-like object 中读取字符串反序列化
json_str = '{"age":20,"score":88,"name":"bob"}'
print(json.loads(json_str))
