# -*- coding: utf-8 -*-
# https://docs.scipy.org/doc/numpy/reference/ufuncs.html
# http://www.tuicool.com/articles/r2yyei

import numpy as np
import matplotlib.pyplot as plt

# flatten将多维数组转换为一维数组
"""
order : {‘C’, ‘F’, ‘A’, ‘K’}, optionalThe default is ‘C’.
‘C’ means to flatten in row-major (C-style) order.
‘F’ means to flatten in column-major (Fortran- style) order.
‘A’ means to flatten in column-major order if a is Fortran contiguous in memory, row-major order otherwise.
‘K’ means to flatten a in the order the elements occur in memory.
"""
a = [[1,2,3],[4,5,6]]
# print(a.flatten())    # 此用法错误，需要将其先转换为数组，在进行拉平
print(np.array(a).flatten())        # [1 2 3 4 5 6]
print(np.array(a).flatten('F'))     # [1 4 2 5 3 6]
print(np.array(a).flatten('K'))     # [1 2 3 4 5 6]

# np.ptp()找出一组数据中的最大最小值只差

a = [1,2,3,1,4,5,1,2]
print(np.ptp(a))   # 4
## 下面程序实现对于随机生成的数据，找出异常值
x = abs(np.random.randn(500))
# print(x)
width = 20     # 每次检验数据的长度为50
delta = 5     # 设置步长
eps = 2        # 在width范围内，最大最小值之差大于1，则认为这段数据为异常值
N = len(x)
p = []
abnormal = []
for i in np.arange(0, N - width, delta):
    s = x[i:i + width]
    p.append(np.ptp(s))                      # np.ptp求出每段数据的最大最小值之差
    if np.ptp(s) > eps:
        abnormal.append(range(i, i + width))
abnormal = np.array(abnormal).flatten()
abnormal = np.unique(abnormal)                 # 去除重复的值
print(abnormal)
# 绘制图形

t = np.arange(N)
plt.plot(t, x, 'r-', lw=1, label=u'原始数据')
plt.plot(abnormal, x[abnormal], 'go', markeredgecolor='g', ms=3, label=u'异常值')   # 绘制异常值
plt.legend(loc='upper right')
plt.title(u'异常检测', fontsize=18)
plt.grid(b=True)
plt.show()

# 最大值的下标：argmax()、最小值的下标：argmin()
a = np.array([1,5,2,1,7,9])
print(np.argmax(a))     # 5
print(np.argmin(a))     # 0

# sort()函数返回一个新的排序后的数组而argsort()则返回排序后的下标数组
a = np.random.randint(0,10,size=(4,5))
print(a)
print(a.sort())
print(np.argsort(a))    # 返回排序后的下标

# unique()函数返回参数数组中所有不同的值，并按照从小到大排序
a = [2,1,3,4,2,1]
print(np.unique(a))   # [1 2 3 4]

# linspace用于生成等差数列，而logspace用于生成等比数列
print(np.linspace(0,10,6))    # [  0.   2.   4.   6.   8.  10.]
print(np.logspace(0,10,3))    # [1.00000000e+00   1.00000000e+05   1.00000000e+10]

# 数据的合并，vstack hstack  np.concatenate(tup, axis=0)
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
np.vstack((a,b))    # 行合并
a = np.array([[1], [2], [3]])
b = np.array([[2], [3], [4]])
np.vstack((a,b))    # 列合并

# 数组的分割
"""
array_split
Split an array into multiple sub-arrays of equal or near-equal size. Does not raise an exception if an equal division cannot be made.
hsplit
Split array into multiple sub-arrays horizontally (column-wise).
vsplit
Split array into multiple sub-arrays vertically (row wise).
dsplit
Split array into multiple sub-arrays along the 3rd axis (depth).
concatenate
Join a sequence of arrays along an existing axis.
stack
Join a sequence of arrays along a new axis.
hstack
Stack arrays in sequence horizontally (column wise).
vstack
Stack arrays in sequence vertically (row wise).
dstack
Stack arrays in sequence depth wise (along third dimension).
"""
x = np.arange(9.0)
# 将数据分割成每组几个
np.split(x, 3)     # [array([ 0.,  1.,  2.]), array([ 3.,  4.,  5.]), array([ 6.,  7.,  8.])]

# 将数据按照一个的数组进行分割
x = np.arange(8.0)
np.split(x, [3, 5, 6, 10])
# [array([ 0.,  1.,  2.]),
#  array([ 3.,  4.]),
#  array([ 5.]),
#  array([ 6.,  7.]),
#  array([], dtype=float64)]

# numpy.clip()
"""
numpy.clip(a,a_min,a_max,a=None)的运用：方法解释：Clip（limit）the values in the array.
这个方法会给出一个区间，在区间之外的数字将被剪除到区间的边缘，
例如给定一个区间[0,1]，则小于0的将变成0，大于1则变成1.
numpy.clip(a,a_min,a_max,a=None)方法的举例运用。
"""
a = np.arange(10)
print(a)
print(np.clip(a,1,8))
print(np.clip(a,3,6,out=a))
print(np.clip(a,[3,4,1,1,1,4,4,4,4,4],8)) # 对于每一个数建立规则
print(np.clip(a,[3,4,5,6,6,4,4,9,4,4],5))
# [0 1 2 3 4 5 6 7 8 9]
# [1 1 2 3 4 5 6 7 8 8]
# [3 3 3 3 4 5 6 6 6 6]
# [3 4 3 3 4 5 6 6 6 6]
# [3 4 5 6 6 5 5 9 5 5]

print(np.fabs([-1.2,1.3]))

# numpy.conj
np.conjugate(1+2j)
# (1-2j)
x = np.eye(2) + 1j * np.eye(2)
np.conjugate(x)
# array([[ 1.-1.j,  0.-0.j],
#        [ 0.-0.j,  1.-1.j]])
