# -*- coding: utf-8 -*-
"""
寻找“水仙花数”：水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153
寻找“完美数”：如果一个数恰好等于它的因子之和，则称该数为“完全数”
百鸡百钱问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
斐波那契数列: 这个数列从第3项开始，每一项都等于前两项之和。

@Time    : 2019/9/24 10:50
@Author  : shengty
"""

# 寻找水仙数
for i in range(100, 1000):
    b = int(i / 100)
    s = int((i - b*100) / 10)
    g = i - b*100 - s*10
    if i == b**3 + s**3 + g**3:
        print('水仙数为%d' % i)

# 寻找完美数（1000以内）
for i in range(1, 1001):
    sumj = 0
    for j in range(i-1, 0, -1):
        if i % j == 0:
            sumj += j
    if sumj == i:
        print('find a perfect number: %d' % i)

# 百鸡百钱问题
for i in range(1, 21):
    for j in range(1, 34):
        k = 100 - (i * 5 + j * 3)  # 3只小鸡值1钱
        if i + j + 3 * k == 100:
            print('%d 只公鸡，%d 只母鸡，%d 只小鸡' % (i, j, 3*k))

# 斐波那契数列
a = 1
b = 1
print('1\n1')
for i in range(2, 1000):
    if i == a + b:
        print('%d' % i)
        a = b
        b = i
