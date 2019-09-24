# -*- coding: utf-8 -*-
"""
全局变量的作用域

@Time    : 2019/9/24 19:44
@Author  : shengty
"""


def foo():
    a = 200
    print(a)  # 200


def foo1():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()  # 200，能搜索到局部变量就不搜全局变量了
    print(a)  # 100
