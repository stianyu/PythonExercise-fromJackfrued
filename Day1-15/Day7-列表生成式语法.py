# -*- coding: utf-8 -*-
"""
列表生成式语法来创建列表

@Time    : 2019/9/25 15:14
@Author  : shengty
"""
import sys
import os
import time
import random


def list_function():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)


def run_horse_lamp():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


def generate_code(code_len=4):
    content = '0123456789abcdefghigklmnopqrstuvwxyz'
    last_pos = len(content)-1
    code = ''
    for _ in range(code_len):
        post = random.randint(0, last_pos)
        code += content[post]
    return code


def how_many_day(year, month, day):
    days = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    is_leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    for m in range(month - 1):
        day += days[is_leap_year][m]
    return day


def pascals_triangle(row):
    colum = row
    pt = [[]] * row
    for r in range(row):
        pt[r] = [None] * (r+1)
        for c in range(r+1):
            if c == 0 or c == r:
                pt[r][c] = 1
            else:
                pt[r][c] = pt[r-1][c-1] + pt[r-1][c]
    return pt


def main():
    # print(how_many_day(2019, 2, 1))
    print(x for x in pascals_triangle(5))


if __name__ == '__main__':
    main()
