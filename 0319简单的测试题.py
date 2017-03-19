# -*- coding: utf-8 -*-
# http://python.jobbole.com/83641/

# 1. 编写代码, 打印1-1万之内的偶数
print([x for x in range(1,10001) if x % 2 == 0])

# 2. 写一个函数, 用正则表达式清除字符串中[]和其中的内容。
s = '[lol]你好，帮我把这些markup清掉，[smile]。谢谢![as]，不客气！[231]'
'''
    对于字符串s，如果在匹配的过程中设置匹配规则为'\[.+\]'  会返回[lol]你好，帮我把这些markup清掉，[smile]。谢谢![as]
    是因为返回值的最开始为[结尾为]，满足给定的条件，这时候我们注意点返回值之间有]所以，我们要去除这个]
    选用这种格式进行匹配\[([^\]]*?)\]
'''
import re
def remove(s):
  pattern = re.compile(r'\[([^\]]*?)\]')  # 在匹配中要注意，[]字符应该为除去]符号的所有字符，这样才能全部匹配
  get_match = re.findall(pattern,s)
  for i in get_match:
    i = '\[' + i + '\]'
    s = re.sub(i,'',s)
   print(s)
remove(s)

# 3. 请使用python, 对下面的函数进行处理，
import datetime
def hello(name):
    begin = datetime.datetime.now()
    print("hello, %s" % name)
    end = datetime.datetime.now()
    print(end - begin)
hello('my_name')

# 4. 写一个函数, 将驼峰命名法字符串转成下划线命名字符串(需考虑各类编码中常见的命名)
'''
    GetItem -> get_item
    getItem -> get_item
'''
name = 'GetItem'
def camel_to_underline(s):
    '''
        驼峰命名格式转下划线命名格式
    '''
    underline_format = ''
    for i in s:
        underline_format += i if i.islower() else '_'+i.lower()
    if s[0].islower():
        print(underline_format)
    else:
        print(underline_format.replace('_', '', 1))
camel_to_underline(name)

def underline_to_camel(s):
    '''''
        下划线命名格式驼峰命名格式
    '''
    camel_format = ''
    for i in s.split('_'):
        camel_format += i.capitalize()   # 将首字母转换为大写形式
    print(camel_format)
underline_to_camel('get_item')

# 5. 有一个列表：[1, 2, 3, 4…n]，n=20；请编写代码打印如下规律的输出：
'''
    1 [1*, 2, 3, 4, 5]
    2 [1, 2*, 3, 4, 5]
    3 [1, 2, 3*, 4, 5]
    4 [2, 3, 4*, 5, 6]
    5 [3, 4, 5*, 6, 7]
    6 [4, 5, 6*, 7, 8]
    ...

    20 [16, 17, 18, 19, 20*]
'''
nrow = 20 # 行数
ncol = 5  # 列数
num = list(range(1,nrow+1))
i,j,m = 1,1,1
for k in range(nrow):
  if i <= ncol-2:
    print(m,[str(m)+'*' if x==m else x for x in num[0:ncol]])
    i += 1
  elif j > nrow-ncol-1:
    print(m,[str(m)+'*' if x==m else x for x in num[-ncol:]])
    j += 1
  else:
    print(m,[str(m)+'*' if x==m else x for x in num[j:j+ncol]])
  m += 1
