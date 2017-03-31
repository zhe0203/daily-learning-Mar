# -*- coding: utf-8 -*-
# 解微分方程
import numpy as np
def dy_dt(y,t):
    return np.sin(t)

# 积分求解
from scipy.integrate import odeint
from matplotlib.pyplot import plot as plt
t = np.linspace(0,2*np.pi,100)
result = odeint(dy_dt,0,t)

# 高阶微分方程
def dy_dt(y, t):
    """Governing equations for projectile motion with drag.
    y[0] = position
    y[1] = velocity
    g = gravity (m/s2)
    D = drag (1/s) = force/velocity
    m = mass (kg)
    """
    g = -9.8
    D = 0.1
    m = 0.15
    dy1 = g - (D/m) * y[1]
    dy0 = y[1] if y[0] >= 0 else 0.
    return [dy0, dy1]
position_0 = 0
velocity_0 = 100
t = np.linspace(0,12,100)
y = odeint(dy_dt,[position_0,velocity_0],t)

# 稀疏矩阵
# 构建稀疏矩阵
from scipy.sparse import *
print(coo_matrix((2,3)))
A = coo_matrix([[1,2,0],[0,0,3],[4,0,5]])
print(A)
print(type(A))
B = A.tocsr()   # 不同格式的稀疏矩阵可以相互转化
# print(B)

# 可以转化为普通矩阵
C = A.todense()
print(C)

# 还可以传入元素来构建稀疏矩阵
I = np.array([0,3,1,0])
J = np.array([0,3,1,2])
V = np.array([4,5,7,9])
A = coo_matrix((V,(I,J)),shape=(4,4))
print(A)

# COO 格式的稀疏矩阵在构建的时候只是简单的将坐标和值加到后面，对于重复的坐标不进行处理：
I = np.array([0,0,1,3,1,0,0])
J = np.array([0,2,1,3,1,0,0])
V = np.array([1,1,1,1,1,1,1])
B = coo_matrix((V,(I,J)),shape=(4,4))
print(B)
# 转换成CSR格式会自动将相同坐标的值合并
C = B.tocsr()
print(C)

# 求解微分方程
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from numpy.linalg import solve,norm
from numpy.random import rand

A = lil_matrix((1000,1000))
A[0,:100] = rand(100)
A[1,100:200] = A[0,:100]
A.setdiag(rand(1000))

# 转化为CSR后，用spsolve求解AX=B
A = A.tocsr()
b = rand(1000)
x = spsolve(A,b)

# 转化成正常数组之后求解
x_ = solve(A.toarray(),b)
# 查看误差
err = norm(x-x_)
print(err)

# sparse.find函数
# 返回一个三元组，表示稀疏矩阵中非零元素的（row,col,value)
from scipy import sparse
row,col,val = sparse.find(C)
print(row,col,val)

# sparse.issparse函数
# 查看一个对象是否为稀疏矩阵
print(sparse.issparse(B))
print(sparse.isspmatrix(B.todense()))
# 还可以查询是否为指定格式的稀疏矩阵
print(sparse.isspmatrix_coo(B))
print(sparse.isspmatrix_csr(B))

# 线性代数
# numpy和scipy中，负责进行线性代数部分计算的模块叫linalg
import numpy.linalg
import scipy as sp
import scipy.linalg
import matplotlib.pyplot as plt
from scipy import linalg
# 在使用时，我们一般使用 scipy.linalg 而不是 numpy.linalg
print("number of items in numpy.linalg:", len(dir(numpy.linalg)))
print("number of items in scipy.linalg:", len(dir(scipy.linalg)))
# 支持类似 MATLAB 创建矩阵的语法
# 矩阵乘法默认用 * 号
# .I 表示逆，.T 表示转置
A = np.mat('[1,2;3,4]')
print(repr(A))
A = np.matrix('[1,2;3,4]')
print(repr(A))
# 转置和逆
print(repr(A.I))
print(repr(A.T))

A = np.array([[1,2],[3,4]])
print(repr(A))
# 转置和逆
print(repr(linalg.inv(A)))   # 求矩阵的逆
repr(A.T)                    # 求矩阵的转置

# 矩阵乘法
b = np.array([5,6])
print(repr(A.dot(b)))  # 矩阵的乘法

# 普通的矩阵乘法，对应的元素相乘
print(repr(A * b))

# linalg.inv()可以求一个可逆矩阵的逆

# 求解线性方程组
# 可以使用linalg.solve 求解方程组，也可以求逆在相乘，两者中solve比较快
import time
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
b = np.array([10,8,3])
tic = time.time()   # 当前时间
for i in range(1000):
    x = linalg.inv(A).dot(b)
print(x)
print(A.dot(x)-b)
print('inv and dot:{} s'.format(time.time()-tic))
tic = time.time()
for i in range(1000):
    x = linalg.solve(A,b)
print(x)
print(A.dot(x)-b)
print('solve :{} s'.format(time.time()-tic))

# 计算行列式
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
print(linalg.det(A))

# 计算矩阵或者向量的模
A = np.array([[1,2],[3,4]])
print(linalg.norm(A))
linalg.norm(A,'fro')    # frobenius norm默认值
linalg.norm(A,1)        # L1 norm 最大列和
linalg.norm(A,-1)       # L-1norm最小列和
linalg.norm(A,np.inf)   # L inf norm 最大列和

# 最小二乘解和伪逆
c1,c2 = 5.0,2.0
i = np.r_[1:11]
xi = 0.1 * i
yi = c1*np.exp(-xi) + c2*xi
zi = yi + 0.05*np.max(yi) * np.random.randn(len(yi))
A = np.c_[np.exp(-xi)[:,np.newaxis],xi[:,np.newaxis]]

# 求解最小二乘问题
c,resid,rank,sigma = linalg.lstsq(A,zi)
print(c)

# 矩阵的分解 特征值和特征向量
# linalg.eig(A)  返回矩阵的特征值和特征向量
# linalg.eigvals(A) 返回矩阵的特征值
# linalg.eig(A,B)   # 求解Av = uBv的问题

A = np.array([[1, 5, 2],
              [2, 4, 1],
              [3, 6, 2]])
la, v = linalg.eig(A)
# 验证是否归一化
print(np.sum(abs(v**2),axis=0))
l1 = la[0]
v1 = v[:,0].T
# 验证是否为特征是和特征向量对
print(linalg.norm(A.dot(v1)-l1*v1))

# 奇异值分解
# u,s,vh = linalg.svd(A)
# sig = linalg.diagsvg(s,M,N)  从奇异值恢复 Σ矩阵
A = np.array([[1,2,3],[4,5,6]])
U, s, Vh = linalg.svd(A)
M, N = A.shape
Sig = linalg.diagsvd(s,M,N)

# LU 分解 A = PLU
# PP 是 M×M 的单位矩阵的一个排列，L 是下三角阵，U 是上三角阵
# linalg.lu
A = np.array([[1,2,3],[4,5,6]])
P,L,U = linalg.lu(A)
print(P,L,U)
print(P.dot(L).dot(U))

# Cholesky 分解（A=AH）
# 可以用 linalg.cholesky 求解。

# QR 分解  A = QR R 为上三角形矩阵，Q 是正交矩阵。
# 可以用 linalg.qr 求解

# Schur 分解 A=ZTZH 其中 Z 是正交矩阵，T 是一个上三角矩阵。
# linalg.schur(A)

# 指数和对数函数
# linalg,expm3使用的是泰勒展开的方法计算结果
A = np.array([[1,2],[3,4]])
print(linalg.expm3(A))

# linalg.logm实现对数的逆运算
# linalg.sinm linalg.cosm linalg.tanm
