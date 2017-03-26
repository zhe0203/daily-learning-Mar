# -*- coding: utf-8 -*-
"""
韩信带着 10000 金币和纠结，来到了神秘的古老商店，他仅有如下装备选择：
影忍之足 690;巨人之握 1500;破甲弓 2100;泣血之刃 1740;无尽战刃 2140;贤者的庇护 2080
在不考虑装备重复的情况之下，即可以多次购买一件装备，要填满六格物品栏，有多少种购买方式？写一个程序，输出所有可行的购买组合。
附加题：
1、如果没有6格物品栏限制，有多少种购买方式？
2、在 1 的前提下，影忍之足最多购买一次，现在有多少种购买方式？
"""
from itertools import product
shop = {'影忍之足':690,'巨人之握':1500,'破甲弓':2100,'泣血之刃':1740,'无尽战刃':2140,'贤者的庇护':2080}
result = []
for i in product(shop.keys(),repeat=6):
    price = 0
    for j in range(6):
        price = price + shop[i[j]]
    if price <= 10000 and sorted(i) not in result:
        result.append(sorted(i))
print(len(result))
print(result)

# 考虑购买先后次序问题，将其认为是同一种结果，进行去重
# sort_result = []
# for x in result:
#     sort_result.append(':'.join(sorted(x)))
# print([k.split(':') for k in sort_result])
# print(len(set(sort_result)))

# 统计每种商品购买的次数
# result_1 = {}
# for k in result:
#     for i in range(6):
#         if i not in result_1.keys():
#             result_1[i] = 1
#         else:
#             result_1[i] += 1
# print(result_1)
