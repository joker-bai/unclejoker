#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 14:55
# @Author  : Joker Bai
# @Email   : unclejoker520@163.com
# @File    : test.py
# @Software: PyCharm
# @Function:
# @Version :
import objgraph

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

objgraph.show_refs([a])
