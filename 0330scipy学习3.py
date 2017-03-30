# -*- coding: utf-8 -*-
# 积分
# 符号运算可以用sympy模块完成
# 先导入init_printing模块方便其显示

from sympy import init_printing
init_printing()
from sympy import symbols,integrate
import sympy
# 产生x和y两个符号变量，并进行运算
x,y = symbols('x y')
print(sympy.sqrt(x ** 2 + y ** 2))
# 对于生成的符号变量z,我们将其中的x利用subs方法替换为3
z = sympy.sqrt(x **2 + y ** 2)
print(z.subs(x,3))
# 再替换y
print(z.subs(x,3).subs(y,4))

# 还可以从sympy.abc中导入现成的符号变量
from sympy.abc import theta
y = sympy.sin(theta) ** 2
print(y)

# 对y进行积分
Y = integrate(y)
print(Y)

# 计算 Y(π)−Y(0)Y(π)−Y(0)
import numpy as np
np.set_printoptions(precision=3)
print(Y.subs(theta,np.pi) - Y.subs(theta,0))
print(integrate(y,(theta,0,sympy.pi)))
# 显示的是字符表达式，查看具体数值可以使用evalf方法，或者传入np.pi而不是sympy.pi
print(integrate(y,(theta,0,sympy.pi)).evalf())
integrate(y,(theta,0,np.pi))

# 根据牛顿莱布尼兹公式，这两个数值应该相等
# 产生不定积分对象
Y_indef = sympy.Integral(y)
print(Y_indef)

# 定积分
Y_def = sympy.Integral(y,(theta,0,sympy.pi))
print(Y_def)

Y_raw = lambda x:integrate(y,(theta,0,x))
Y = np.vectorize(Y_raw)
print(Y)

import matplotlib.pyplot as plt
x = np.linspace(0,2*np.pi)
p = plt.plot(x,Y(x))
# plt.show()

# 数值积分
from scipy.special import jv
def f(x):
    return jv(2.5,x)
x = np.linspace(0,10)
p = plt.plot(x,f(x),'k-')

# quad函数
from scipy.integrate import quad
interval = [0,6.5]
value,max_err = quad(f,*interval)
# 积分值
print(value)
# 最大误差
print(max_err)

# 积分区间图示，蓝色为正，红色为负
print('integral = {:.9f}'.format(value))
print('upper bound on error:{:.2e}'.format(max_err))
x = np.linspace(0,10,100)
p = plt.plot(x,f(x),'k-')
x = np.linspace(0,6.5,45)
p = plt.fill_between(x,f(x),where=f(x)>0,color='blue')
p = plt.fill_between(x,f(x),where=f(x)<0,color='red',interpolate=True)

# 积分到无穷
from numpy import inf
interval = [0,inf]
def g(x):
    return np.exp(-x ** 1/2)
value,max_err = quad(g,*interval)
x = np.linspace(0, 10, 50)
fig = plt.figure(figsize=(10,3))
p = plt.plot(x, g(x), 'k-')
p = plt.fill_between(x, g(x))
plt.annotate(r"$\int_0^{\infty}e^{-x^1/2}dx = $" + "{}".format(value), (4, 0.6),
         fontsize=16)
print("upper bound on error: {:.1e}".format(max_err))
# 双重积分
def h(x,t,n):
    return np.exp(-x * t) / (t ** n)
# 一种方法是调用quad函数，不过这里quad的返回值不能向量化，所以使用了修饰符vectorize将其向量化
from numpy import vectorize
@vectorize
def int_h_dx(t,n):
    return quad(h,0,np.inf,args=(t,n))[0]
@vectorize
def I_n(n):
    return quad(int_h_dx, 1, np.inf, args=(n))
from scipy.integrate import dblquad
@vectorize
def I(n):
    """Same as I_n, but using the built-in dblquad"""
    x_lower = 0
    x_upper = np.inf
    return dblquad(h,
                   lambda t_lower: 1, lambda t_upper: np.inf,
                   x_lower, x_upper, args=(n,))
I_n([0.5, 1.0, 2.0, 5])
