# -*- coding: utf-8 -*

## 找出各位数字之和等于n的5位、6位的回文数字
## 第一次写的
def func(n):
    for i in range(10000, 1000000):
        if str(i) == str(i)[::-1] and sum(list(map(int,list(str(i))))) == n:
            print(i)
            
## 将上述函数优化   
def func_1(n):
    if 5 <= n <= 54:
        print([i for i in range(10000,1000000) if str(i) == str(i)[::-1] \
             and sum(list(map(int,list(str(i))))) == n])
    else:
        raise Exception(r"n需满足5 =< n <= 54")

if __name__=="__main__":
    func(2)
    func_1(5)
