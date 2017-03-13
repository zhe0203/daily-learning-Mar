import numpy as np
import pandas as pd

## 计算阶乘的函数
def fun(x):
  if x == 1:
      return 1
   else:
      return x* fun(x-1)

## 计算pi值
pd.set_option('display.max_rows',5)  # 将数据显示设置为5行
def get_pi(n):
  x = pd.Series(np.random.rand(n))   # n的值越大越好
  y = pd.Series(np.random.rand(n))
  df = pd.DataFrame({'x':x,'y':y})  # 将数据组成数据框的形式
  df_1 = pd.DataFrame({'x1':df['x'].apply(lambda x:x**2),
                       'y1':df['y'].apply(lambda x:x**2)})
  df_1['z1'] = df_1.apply(sum,axis=1)
  df_1['z2'] = np.where(df_1['z1'] <= 1,1,0)
  print(df_1.apply(sum)['z2']*4/n)
  
if __name__=="__main__":
  get_pi(999999999)
  
