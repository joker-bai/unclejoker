#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 14:46
# @Author  : Joker Bai
# @Email   : unclejoker520@163.com
# @File    : app01_filter_test.py
# @Software: PyCharm
# @Function:
# @Version :
from django import template

register = template.Library()


@register.filter(name="add_sb")
def add_sb(value):
    return "{} SB".format(value)


@register.simple_tag(name="my_sum")
def my_sum(v1, v2, v3):
    return "{}-{}-{}".format(v1, v2, v3)
