#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 15:00
# @Author  : Joker Bai
# @Email   : unclejoker520@163.com
# @File    : mypage.py
# @Software: PyCharm
# @Function:
# @Version :


class Page(object):
    def __init__(self, current_page, total_count, url_prefix, show_data_count=10, max_page_num=11):
        """
        :param current_page:    当前的页码
        :param total_count:     数据的总条数
        :param url_prefix:      a标签herf前缀
        :param show_data_count:     每页展示的数据条数
        :param max_page_num:        页码数量
        """
        self.current_page = current_page
        self.total_count = total_count
        self.url_prefix = url_prefix
        self.show_data_count = show_data_count
        self.max_page_num = max_page_num
        # 计算总共需要多少页码来展示数据
        total_page, other = divmod(self.total_count, self.show_data_count)
        # 如果other数据不为0，则页码数加1
        if other:
            total_page += 1
        # 如果访问的页码数大于总的页码数，更改当前页码数为最后的页码数
        if self.current_page > total_page:
            self.current_page = total_page
        # 定义两个变量保存取数据的区间
        self.data_start = (self.current_page - 1) * 10
        self.data_end = self.current_page * 10

        # 计算页面上总共应该显示多少页码
        if total_page < self.max_page_num:
            self.max_page_num = total_page
        half_max_page = self.max_page_num // 2
        # 页码开始位
        page_start = self.current_page - half_max_page
        # 页码结束位
        page_end = self.current_page + half_max_page
        if page_start <= 1:
            page_start = 1
            page_end = self.max_page_num
        if page_end >= total_page:
            page_start = total_page - self.max_page_num + 1
            page_end = total_page
        self.page_start = page_start
        self.page_end = page_end
        self.total_page = total_page

    @property
    def start(self):
        return self.data_start

    @property
    def end(self):
        return self.data_end

    def page_html(self):
        """
        功能：拼接html代码
        :param self:
        :return:
        """
        html_str_list = []
        # 加上首页
        html_str_list.append('<li><a href="{}?page=1">首页</a></li>'.format(self.url_prefix))
        # 判断如果是第一页，就没有上一页
        if self.current_page <= 1:
            html_str_list.append(
                '<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>')
        else:
            # 加上上一页的标签
            html_str_list.append(
                '<li><a href="{}?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(self.url_prefix,
                                                                                                self.current_page - 1))
        print(self.page_start, self.page_end)
        for i in range(self.page_start, self.page_end + 1):
            # 如果是当前页就加一个active样式类
            if i == self.current_page:
                tmp = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix, i)
            else:
                tmp = '<li><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix, i)
            html_str_list.append(tmp)

        # 加一个下一页的按钮
        # 判断，如果是最后一页，就没有下一页
        if self.current_page >= self.total_page:
            html_str_list.append(
                '<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
        else:
            html_str_list.append(
                '<li><a href="{}?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                    self.url_prefix, self.current_page + 1))
        # 加最后一页
        html_str_list.append(
            '<li><a href="{}?page={}">尾页</a></li>'.format(self.url_prefix, self.total_page))

        page_html_full = "".join(html_str_list)
        return page_html_full
