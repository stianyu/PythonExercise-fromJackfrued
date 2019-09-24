# -*- coding: utf-8 -*-
"""
计算两个数的最大公约数和最小公倍数
find the greatest common dividisor and the least common multiple of two number

@Time    : 2019/9/24 9:08
@Author  : shengty
"""

num1 = int(input('input the first number:'))
num2 = int(input('input the second number:'))

min_num = min(num1, num2)
gcd = min_num

while 1:
    if num1 % gcd == 0 and num2 % gcd == 0 or gcd < 1:
        break
    else:
        gcd -= 1
        
print('The greatest common divisior of %d and %d is %d, the least common multiple is %d. \n'
      % (num1, num2, gcd, num1 * num2 / gcd))
