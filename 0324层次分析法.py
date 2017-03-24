# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
from functools import reduce
from operator import mul

# 计算权重
os.chdir('C:/Users/jk/Desktop/层次分析')
for lst in os.listdir():
    print(lst)

for lst in os.listdir():
    mydata = pd.read_excel(lst,index_col=[0], header=[0])
    length = len(mydata)
    result = np.zeros((length, length))
    for m in range(10):
        score = np.zeros((length,length))
        for i in range(length):
            for j in range(i+1):
                if i == j:
                    score[i,j] = 1
                else:
                    if ord(mydata.iloc[i,m]) - ord(mydata.iloc[j,m]) == -4:
                        score[i, j] = 1 / 9
                    elif ord(mydata.iloc[i,m]) - ord(mydata.iloc[j,m]) == -3:
                        score[i,j] = 1/7
                    elif ord(mydata.iloc[i,m]) - ord(mydata.iloc[j,m]) == -2:
                        score[i,j] = 1/5
                    elif ord(mydata.iloc[i,m]) - ord(mydata.iloc[j,m]) == -1:
                        score[i,j] = 1/3
                    elif ord(mydata.iloc[i,m]) - ord(mydata.iloc[j,m]) == 0:
                        score[i,j] = 1
                    elif ord(mydata.iloc[i, m]) - ord(mydata.iloc[j, m]) == 1:
                        score[i, j] = 3
                    elif ord(mydata.iloc[i, m]) - ord(mydata.iloc[j, m]) == 2:
                        score[i, j] = 5
                    elif ord(mydata.iloc[i, m]) - ord(mydata.iloc[j, m]) == 3:
                        score[i, j] = 7
                    elif ord(mydata.iloc[i, m]) - ord(mydata.iloc[j, m]) == 4:
                        score[i, j] = 9

        for i in range(length):
            for j in range(length):
                if j > i:
                    score[i,j] = 1 / score[j,i]


        result = result + score
    my_result = result / 10
    my_result = my_result.T

    # 行内连乘
    df = pd.DataFrame(my_result,index = mydata.index)
    num = []
    for i in range(length):
        num.append(reduce(mul,my_result[i,]))
    df['e'] = num
    df['f'] = list(map(lambda x:x**(1/length),df['e']))
    get_sum = df.sum(axis = 0)
    df['权重'] = list(map(lambda x:x/get_sum.f,df['f']))
    name = lst.split('.')[0] + '_result' + '.xlsx'
    df.to_excel(name,index = True)

    # 求特征值
    # weight = np.array(df['权重'])
    # print(sum(np.dot(my_result,weight) / weight)/4)
    # a,b = np.linalg.eig(my_result)   # 特征值赋值给a，对应特征向量赋值给b
    # print(max(a))
    # 一致性检验
    # ci = ((max(a)-4)/(4-1))
    # print(ci/0.9)

# 根据权重计算最终得分
os.chdir('C:/Users/jk/Desktop/层次分析/计算得分')
factor = [x for x in os.listdir() if 'result' not in x]
weight = [x for x in os.listdir() if 'result' in x]
result = []
for i in range(len(weight)):
    print(factor[i],weight[i])
    factor_1 = pd.read_excel(factor[i],index_col=[0],header=[0])
    weight_1 = list(pd.read_excel(weight[i],index_col=[0],header=[0])['权重'])
    # print(factor_1)
    # print(weight_1)
    result.extend(np.dot(np.dot(weight_1,np.mat(factor_1)),[100,80,60,40]))
print(result)
