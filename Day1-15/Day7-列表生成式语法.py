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


def run_horse_lamp():  # scroll the marquee
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


def generate_code(code_len=4):  # generate a CAPTCHA
    content = '0123456789abcdefghigklmnopqrstuvwxyz'
    last_pos = len(content)-1
    code = ''
    for _ in range(code_len):
        post = random.randint(0, last_pos)
        code += content[post]
    return code


def how_many_day(year, month, day):  # calculate days passed
    days = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    is_leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    for m in range(month - 1):
        day += days[is_leap_year][m]
    return day


def pascals_triangle(row):  # my code to generate yanghui triangle
    pt = [[]] * row
    for r in range(row):
        pt[r] = [None] * (r+1)
        for c in range(r+1):
            if c == 0 or c == r:
                pt[r][c] = 1
            else:
                pt[r][c] = pt[r-1][c-1] + pt[r-1][c]
    return pt


def print_pt(n):  # my code
    for i, row in enumerate(pascals_triangle(n)):
        print(("   "*(n - i) + "{:6}" * (i + 1)).format(*row))


def pascal_triangle(n):  # code 1 for example
    row = [1]
    yield row
    for _ in range(n):
        row = [1] + [x + y for x, y in zip(row[:-1], row[1:])] + [1]
        yield row


def generate_pascal(n):  # code 2 for example
    p = []
    for i in range(n):
        line = [1]
        if i:
            prev_line = p[-1]
            for j in range(1, i):
                line.append(prev_line[j - 1] + prev_line[j])
            line.append(1)
        p.append(line)
    return p


def print_pascal(p, end=" ", sep=" "):  # code 2 for example
    n = len(p)
    for i, line in enumerate(p):
        print("   " * (n - i), end=end, sep=sep)
        for e in line:
            print('{0:5}'.format(e), end=sep, sep=sep)
        print()


def main():
    # print(how_many_day(2019, 2, 1))
    n = int(input('input n: '))
    print_pt(n)
    p = generate_pascal(n)
    print_pascal(p)


if __name__ == '__main__':
    main()
