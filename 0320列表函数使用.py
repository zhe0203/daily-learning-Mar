# -*- coding: utf-8 -*-
#　生成元组
print(((x, y) for x in range(3) for y in range(x)))

# for if 结合使用
print([x for x in range(10) if x % 2 == 0])

# 使用列表函数生成多维数组
print([[0 for i in range(5)] for i in range(5)])
## [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print([[i*j for i in range(1,10)] for j in range(1,10)])

# 对于python3无has_key这个函数，可以使用in代替
a = [{'a':2,'b':3},{'a':2,'c':1}]
print(['b' in a[i] for i in range(len(a))])    # 判断每一个字典中是否包'b'这个键

# 对于a总的每一个字典，如果存在b键，则返回其对应的值，如果不存在，则返回None值
print([a[i]['b'] if 'b' in a[i] else None for i in range(len(a))])
print([i['b'] if 'b' in i else None for i in a])        # 可以简写成这样

# Python里字符串有replace方法，但是List没有replace的方法，可以用列表解析的方法实现元素替换
lst = ['1','2','3']
print(['4' if x=='1' else x for x in lst])    # 把lst中的1替换为4
## ['4', '2', '3']

## 批量替换
lst = ['1','2','3','4','5']
pattern = ['3','4']
rep = ['d' if x in pattern else x for x in lst]
print(rep)   # ['1', '2', 'd', 'd', '5']

## 映射替换，根据一个字典的映射关系替换
lst = ['1','2','3','4','5']
pattern = {'3':'three','4':'four'}
rep = [pattern[x] if x in pattern else x for x in lst]
print(rep)  # ['1', '2', 'three', 'four', '5']

# 将dataframe形式转换为dict形式
# https://stackoverflow.com/questions/41277130/convert-pandas-dataframe-to-dictionary
import pandas as pd
df = pd.DataFrame({'created':pd.date_range('2016-12-16',periods=7),
                   'moans':[0,0,0,0,6,0,0],
                   'thanks':[0,0,0,2,0,0,2]})
print({k:[[x,y] for x,y in v.items()] for k,v in df.set_index('created').items()})

# list.append(obj) 在列列表末尾添加新的对象
# list.count(obj) 统计某个元素在列表中出现的次数
# list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值
# list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
lts = [1,2,3,4,5,6]
print(lst.index('3'))  # 2
# list.insert(index,obj) 将对象插入列表
print(lst.insert(2,'5'))
# list.pop() 移除列表中的一个元素，默认为最后一个元素，并且返回该元素的值
# list.remove(obj) 移除列表中某个值的第一个匹配项
# list.reverse() 反向列表中元素
# list.sort() 对原列表进行排序
# list.clear() 清空列表
# list.copy() 复制列表


# Python字典包含了以下内置方法
a = {'A':2,'B':1}
# dict.clear() 删除字典的所有内容
print(a.clear())  # None
# dict.fromkeys() 创建一个新字典，以序列seq中的元素作为字典的键，val为字典所有键对应的初始值
# dict.get(key,default=None) 返回指定键的值，如果值不存在字典中返回default值
# key in dict 如果键在字典dict里返回true,否则返回false
# dict.items() 以列表返回可遍历的（键，值）元组的数组
# dict.keys() 以列表返回一个字典的所有的键
# dict.setdefault(key,default=None) 如果键不存在字典中，将会添加键并将值设置为defalute
# dict.update(dict2) 把字典dict2的键/值对更新大dict里面
# dict.values() 以列表返回字典中的所有值
