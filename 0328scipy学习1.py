# -*- coding: utf-8 -*-
# http://nbviewer.jupyter.org/github/lijin-THU/notes-python/tree/master/04.%20scipy/
# scipy是python中进行科学计算的第三方库，以numpy为基础
# statsmodels是一个统计库，着重于统计模型

import numpy as np
import matplotlib.pyplot as plt
# 设置numpy浮点数显示格式
np.set_printoptions(precision=2,suppress=True)

# 插值
data = np.genfromtxt('JANAF_CH4.txt',
                     delimiter='\t',names=True,
                     missing_values='INFINITE',
                     filling_values=np.inf)
# 显示部分数据
for row in data[:7]:
    print("{}\t{}".format(row['TK'],row['Cp']))
print("...\t...")

# 绘图
p = plt.plot(data['TK'],data['Cp'],'kx')
t = plt.title('JANAF data for Methane $CH_4$')
a = plt.axis([0,6000,30,120])
x = plt.xlabel('Temperature (K)')
y = plt.ylabel(r"$C_p$ ($\frac{kJ}{kg K}$)")
# plt.show()

# 假设我们要对这组数据进行插值，先导入一维插值函数interp1d
from scipy.interpolate import interp1d
ch4_cp = interp1d(data['TK'], data['Cp'])
# interp1d 的返回值可以像函数一样接受输入，并返回插值的结果。
ch4_cp(382.2)   # 39.565144
ch4_cp([32.2,323,2])   # 10.71  36.71
# 通过参数设置允许超出范围的值存在
ch4_cp = interp1d(data['TK'],data['Cp'],bounds_error=False)
ch4_cp(8752)   # nan

# 可以使用指定值替代这些非法值
ch4_cp = interp1d(data['TK'],data['Cp'],bounds_error=False,fill_value=-999)

# 线性插值
# 其基本思想是，已知相邻两点 x1,x2x1,x2 对应的值 y1,y2y1,y2 ，
# 那么对于 (x1,x2)(x1,x2) 之间的某一点 xx ，
# 线性插值对应的值 yy 满足：点 (x,y)(x,y) 在 (x1,y1),(x2,y2)(x1,y1),(x2,y2) 所形成的线段上。

T = np.arange(100,355,5)
# for i in T:
#     print(ch4_cp(i))         显示每一个数值的插值结果
plt.plot(T,ch4_cp(T),'+k')
p = plt.plot(data['TK'][1:7],data['Cp'][1:7],'ro',markersize=8)
# 其中红色的圆点为原来的数据点，黑色的十字点为对应的插值点，可以明显看到，相邻的数据点的插值在一条直线上。
# plt.show()

# 多项式插值  通过kind来设置
## nearest最紧邻插值;zero 0阶插值;linear线性插值;quadratic二次插值;
## cubic三次插值;4,5,6更高阶插值

# 最近邻插值
cp_ch4 = interp1d(data['TK'],data['Cp'],kind='nearest')
p = plt.plot(T,cp_ch4(T),'k+')
p = plt.plot(data['TK'][1:7],data['Cp'][1:7],'ro',markersize=8)
# plt.show()

# 0阶插值
p_ch4 = interp1d(data['TK'], data['Cp'], kind="zero")
p = plt.plot(T, cp_ch4(T), "k+")
p = plt.plot(data['TK'][1:7], data['Cp'][1:7], 'ro', markersize=8)
# plt.show()

# 二次插值
cp_ch4 = interp1d(data['TK'],data['Cp'],kind='quadratic')
p = plt.plot(T,cp_ch4(T),'k+')
p = plt.plot(data['TK'][1:7],data['Cp'][1:7],'ro',markersize=8)
# plt.show()

# 三次插值
cp_ch4 = interp1d(data['TK'], data['Cp'], kind="cubic")
p = plt.plot(T, cp_ch4(T), "k+")
p = plt.plot(data['TK'][1:7], data['Cp'][1:7], 'ro', markersize=8)

# 四次多项式插值
cp_ch4 = interp1d(data['TK'], data['Cp'], kind=4)
p = plt.plot(T, cp_ch4(T), "k+")
p = plt.plot(data['TK'][1:7], data['Cp'][1:7], 'ro', markersize=8)

# 对于二维乃至更高维度的多项式插值
from scipy.interpolate import interp2d,interpnd

# 径向基函数
# 径向基函数简单来说就是点x的函数值只依赖于x与某点c的距离
x = np.linspace(-3,3,100)
plt.plot(x,np.exp(-1*x**2))
plt.plot(x,np.sqrt(1+x**2))
plt.plot(x,1./np.sqrt(1+x**2))

# 径向基函数插值
from scipy.interpolate.rbf import Rbf
cp_rbf = Rbf(data['TK'],data['Cp'],function='multiquadric')
plt.plot(data['TK'],data['Cp'],'k+')
p = plt.plot(data['TK'],cp_rbf(data['TK']),'r--')
# plt.show()

# 使用 gaussian 核
cp_rbf = Rbf(data['TK'], data['Cp'], function = "gaussian")
plt.plot(data['TK'], data['Cp'], 'k+')
p = plt.plot(data['TK'], cp_rbf(data['TK']), 'r-')

# 高维 RBF 插值
from mpl_toolkits.mplot3d import Axes3D
x, y = np.mgrid[-np.pi/2:np.pi/2:5j, -np.pi/2:np.pi/2:5j]
z = np.cos(np.sqrt(x**2 + y**2))
fig = plt.figure(figsize=(12,6))
ax = fig.gca(projection="3d")
ax.scatter(x,y,z)
zz = Rbf(x, y, z)

xx, yy = np.mgrid[-np.pi/2:np.pi/2:50j, -np.pi/2:np.pi/2:50j]
fig = plt.figure(figsize=(12,6))
ax = fig.gca(projection="3d")

# 概率统计方法
# 导入scipy的统计模块
heights = np.array([1.46, 1.79, 2.01, 1.75, 1.56, 1.69, 1.88, 1.76, 1.88, 1.78])
import scipy.stats.stats as st
print(st.nanmedian(heights))   # 忽略nan值滞后的中位数
print(st.mode(heights))        # 众数及其出现次数
print(st.skew(heights))        # 偏度
print(st.kurtosis(heights))    # 峰度

# 正态分布
from scipy.stats import norm
# norm.cdf 返回对应的累计分布函数值
# norm.pdf 返回对应的概率密度函数值
# norm.rvs 产生指定参数的随机变量
# norm.fit 返回给定数据下，各参数的最大似然估计值
x_norm = norm.rvs(size=500)    # 产生标准正态分布数据500个
x_mean,x_std = norm.fit(x_norm)
print('mean,  ',x_mean)
print('x_std, ',x_std)

# 导入积分函数
import scipy
from scipy.integrate import trapz
# 通积分，计算落在某个区间的概率大小
x1 = np.linspace(-2,2,108)
p = trapz(norm.pdf(x1),x1)
print(p)
# fill_between(x1,norm.pdf(x1),color='red')
# plot(x,norm.pdf(x),'k-')

p = plt.plot(x, norm(loc=0, scale=1).pdf(x))
p = plt.plot(x, norm(loc=0.5, scale=2).pdf(x))
p = plt.plot(x, norm(loc=-0.5, scale=.5).pdf(x))

# 不同自由度的学生 t 分布：
x = np.linspace(-3, 3, 100)

plt.plot(x, t.pdf(x, 1), label='df=1')
plt.plot(x, t.pdf(x, 2), label='df=2')
plt.plot(x, t.pdf(x, 100), label='df=100')
plt.plot(x[::5], norm.pdf(x[::5]), 'kx', label='normal')
plt.legend()

# 离散分布
from scipy.stats import binom,poisson,randint
high = 10
low = -10
x = np.arange(low,high+1,0.5)
p = plt.stem(x,randint(low,high).pmf(x))

# 二项分布
num_trials = 60
x = np.arange(num_trials)
plt.plot(x, binom(num_trials, 0.5).pmf(x), 'o-', label='p=0.5')
plt.plot(x, binom(num_trials, 0.2).pmf(x), 'o-', label='p=0.2')
plt.legend()

# 泊松分布
x = np.arange(0,21)
plt.plot(x, poisson(1).pmf(x), 'o-', label=r'$\lambda$=1')
plt.plot(x, poisson(4).pmf(x), 'o-', label=r'$\lambda$=4')
plt.plot(x, poisson(9).pmf(x), 'o-', label=r'$\lambda$=9')
plt.legend()

# 假设检验
from scipy.stats import norm
from scipy.stats import ttest_ind,ttest_rel,ttest_lsamp
from scipy.stats import t

# 独立样本t检验
## 两组参数不同的正态分布
n1 = norm(loc=0.3,scale=1.0)
n2 = norm(loc=0,scale=1.0)
# 从分布中随机产生两组样本
n1_sample = n1.rvs(size=100)
n2_sample = n2.rvs(szie=100)
# 将两组样本混合在一起
samples = np.hstack((n1_sample,n2_sample))
# 最大似然参数估计
loc,scale = norm.fit(samples)
n = norm(loc=loc,sacle=scale)
# 比较
x = np.linspace(-3,3,100)
plt.hist([samples, n1_sample, n2_sample], normed=True)
plt.plot(x, n.pdf(x), 'b-')
plt.plot(x, n1.pdf(x), 'g-')
plt.plot(x, n2.pdf(x), 'r-')

# 独立双样本t检验的目的在意判断两组样本之间是否存在显著差异
t_val,p = ttest_ind(n1_sample,n2_sample)
print('t = {}'.format(t_val))
print('p-value = {}'.format(p))

# 配对样本t检验
# 配对样本指的是两组样本之间的元素一一对应，例如，假设我们有一组病人的数据
pop_size = 35
pre_treat = norm(loc=0,scale=1)
n0 = pre_treat.rvs(size=pop_size)   # 治疗前的数据
effect = norm(loc=0.05,scale=0.2)   # 治疗后的数据分布
eff = effect.rvs(size=pop_size)    # 治疗效果
n1 = n0 + eff   # 治疗后数据
# 新数据的极大似然故居
loc,sacle = norm.fit(n1)
post_treat = norm(loc=loc,scale=scale)
# 画图
fig = plt.figure(figsize=(10,4))
ax1 = fig.add_subplot(1,2,1)
h = ax1.hist([n0,n1],normed=True)
p = ax1.plot(x,pre_treat.pdf(x),'b-')
p = ax1.plot(x,post_treat.pdf(x),'g-')
ax2 = fig.add_subplot(1,2,2)
h = ax2.hist(eff,normed=True)

# 独立t检验
t_val,p = ttest_ind(n0,n1)
print('t = {}'.format(t_val))
print('pvalue = {}'.format(p))

# 配对t检验
t_val, p = ttest_rel(n0, n1)
print('t = {}'.format(t_val))
print('p-value = {}'.format(p))

# p值计算原理
# p值对应的部分是下图汇总的红色区域，边界范围由t值决定
my_t = t(pop_size)   # 传入参数为自由度，这里自由度为50
p = plt.plot(x,my_t.pdf(x),'b-')
lower_x = x[x <= -abs(t_val)]
upper_x = x[x >= abs(t_val)]
p = plt.fill_between(lower_x,my_t.pdf(lower_x),color='red')
p = plt.fill_between(upper_x,my_t.pdf(upper_x),color='red')
