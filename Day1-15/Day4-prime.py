# -*- coding: utf-8 -*-
"""
输入一个正整数判断它是不是素数

@Time    : 2019/9/24 8:40
@Author  : shengty
"""
from math import sqrt

num = int(input('input a number:'))
end = int(sqrt(num))
is_prime = True
for i in range(1, end + 1):
    if num % i == 0 and end != 1:
        is_prime = False
    else:
        is_prime = True
if is_prime:
    print('%d is a prime' % num)
else:
    print('%d is not a prime' % num)

