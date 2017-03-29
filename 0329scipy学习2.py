# -*- coding: utf-8 -*-
# 曲线拟合
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# 导入多项式拟合工具
from numpy import polyfit,poly1d

x = np.linspace(-5,5,100)
y = 4 * x + 1.5
noise_y = y + np.random.randn(y.shape[-1]) * 2.5
p = plt.plot(x,noise_y,'rx')
p = plt.plot(x,y,'b:')
# plt.show()

# 进行线性拟合，polyfit是多项式拟合函数，线性拟合即一阶多项式
coeff = polyfit(x,noise_y,1)   # 返回的是线性方程组的系数a,b
print(coeff)
p = plt.plot(x,noise_y,'rx')
p = plt.plot(x,coeff[0] * x + coeff[1],'k--')
p = plt.plot(x,y,'b-')
# plt.show()

# 还可以使用poly1d生成一个传入的coeff为参数的多项式函数
f = poly1d(coeff)   # 4.009 x + 0.8163
# print(f)         # 生成f(x)函数，带入x即产生y值
p = plt.plot(x,noise_y,'rx')
p = plt.plot(x,f(x))
# 还可以对他进行数学操作生成新的多项式
print(f + 2*f**2)   # 31.88 x + 35.28 x + 9.636

# 多项式拟合正弦函数
x = np.linspace(-np.pi,np.pi,100)
y = np.sin(x)
## 用一阶到九阶多项式拟合，类似泰勒展开
y1 = poly1d(polyfit(x,y,1))
y3 = poly1d(polyfit(x,y,3))
y5 = poly1d(polyfit(x,y,5))
y7 = poly1d(polyfit(x,y,7))
y9 = poly1d(polyfit(x,y,9))

x = np.linspace(-3*np.pi,3*np.pi,100)
p = plt.plot(x, np.sin(x), 'k')
p = plt.plot(x, y1(x))
p = plt.plot(x, y3(x))
p = plt.plot(x, y5(x))
p = plt.plot(x, y7(x))
p = plt.plot(x, y9(x))
a = plt.axis([-3 * np.pi, 3 * np.pi, -1.25, 1.25])
# plt.show()

# 最小二乘拟合
from scipy.linalg import lstsq
from scipy.stats import linregress
x = np.linspace(0,5,100)
y = 0.5*x+np.random.randn(x.shape[-1])*0.5
plt.plot(x,y,'x')

# 最小二乘解
X = np.hstack((x[:,np.newaxis],np.ones((x.shape[-1],1))))
print(X[1:5])

# 求解
C,resid,rank,s = lstsq(X,y)
print(C,resid,rank,s)
p = plt.plot(x, y, 'rx')
p = plt.plot(x, C[0] * x + C[1], 'k--')

# 线性回归
slope,intercept,r_value,p_value,stderr = linregress(x,y)
print(slope,intercept)
p = plt.plot(x,y,'rx')
p = plt.plot(x,slope*x+intercept,'k--')

# 更高级的拟合
from scipy.optimize import leastsq
def function(x,a,b,f,phi):
    result = a * np.exp(-b * np.sin(f * x + phi))
    return result
# 画出原始曲线
x = np.linspace(0,2*np.pi,50)
actual_parameters = [3,2,1.25,np.pi/4]
y = function(x,*actual_parameters)
p = plt.plot(x,y)

# 加入噪声
from scipy.stats import norm
y_noisy = y + 0.8 * norm.rvs(szie=len(x))
p = plt.plot(x,y,'k-')
p = plt.plot(x,y_noisy,'rx')

# 定义误差函数，将要优化的参数放在前面
def f_err(p,y,x):
    return y - function(x,*p)
# 将这个函数作为参数传入leastsq函数，第二个参数为初始值
c,ret_val = leastsq(f_err,[1,1,1,1],args=(y_noisy,x))
print(c,ret_val)
p = plt.plot(x, y_noisy, 'rx')
p = plt.plot(x, function(x, *c), 'k--')

# 更高级做法
from scipy.optimize import curve_fit
p_est, err_est = curve_fit(function, x, y_noisy)
print(p_est)
p = plt.plot(x, y_noisy, "rx")
p = plt.plot(x, function(x, *p_est), "k--")
