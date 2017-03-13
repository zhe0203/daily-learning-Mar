# -*- coding: utf-8 -*-
import textwrap

# textwrap.fill(text,width=70,**kwargs)
## 包装一段文字，使其每行不超过width参数所规定的字符数
## 相当于'\n'.join(wrap(text))

text = 'module provides some convenience functions'
print(textwrap.fill(text,width=10))

text = u'这是 python 基础库 textwrap的学习'
print(textwrap.fill(text,width=10))

# textwrap.shorten(text,width,**kwargs)
## 以一定的长度截取一段内容的文字
## 在截取时会依据单词进行分割，所以这个函数对于中文的支持比较差，无法正确截取：它会把不带空格的中文当做一整个单词来处理。

text = 'module provides some convenience functions'
print(textwrap.shorten(text,20))
print(textwrap.shorten(text,30,placeholder='...')) # 使用palceholder参数来修改结尾形式
print(textwrap.shorten(text,30,placeholder='___'))
print(textwrap.shorten('hello world!',width=12))

# text.dedent(text)
## 将多行文字统一去除缩进
## 去除掉每行开始都共同含有的多余空格
# end first line with \ to avoid the empty line!
text = '''\
    hello,
      world
'''
print(textwrap.dedent(text))
print(repr(text))
print(repr(textwrap.dedent(text)))

# textwrap.indent(text,prefix,predicate=None)
## 在文本每一行的开头添加词头,prefix参数为词头，predicate参数控制选中行，默认为除了空行之外的所有行
text = 'hello,\nworld'
print(textwrap.indent(text,'+'))
print(textwrap.indent(text,'+',lambda line:True))

# 更加方便的使用，使用TextWrapper类
text = 'The module provides some convenience functions'
## 初始化“包装器”
wrapper = textwrap.TextWrapper()
# 每行最大长度
wrapper.width = 20
# 第一行词头
wrapper.initial_indent = '+'
# 非首行词头
wrapper.subsequent_indent = '*'
# 最后填充文本
result = wrapper.fill(text)
print(result)

# 再举一个栗子
text = '''\
    hello,
      world
'''
wrapper = textwrap.TextWrapper()  # 初始化包装器
wrapper.expand_tabs = True
wrapper.width = 10
wrapper.drop_whitespace = True
result = wrapper.wrap(text)
print(result)

sample_text = '''
   The textwrap module can beusedto format text for output in
   situations where pretty-printing is desired.  It offers
   program matic functionality similar to the paragraph wrapping
   or filling features found in many text editors.
'''
wrapper = textwrap.TextWrapper()
wrapper.width = 50
wrapper.drop_whitespace = True
wrapper.initial_indent = '+'
wrapper.subsequent_indent = ' '*4
result = wrapper.fill(sample_text)
print(result)
