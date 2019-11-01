#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 16:49
# @Author  : Joker Bai
# @Email   : unclejoker520@163.com
# @File    : orm_test.py
# @Software: PyCharm
# @Function:
# @Version :
import  os
if __name__ == '__main__':
    # 加载Django项目的配置信息
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_test.settings")
    # 导入Django，并启动Django项目
    import django
    django.setup()

    from orm import models

    # # 查询所有的人
    # ret = models.Person.objects.all()
    # print(ret)
    #
    # # get查询，返回的是<class 'orm.models.Person'>
    # ret = models.Person.objects.get(id=1)
    # print(ret,type(ret))
    #
    # # filter查询，返回的是<class 'django.db.models.query.QuerySet'>
    # ret = models.Person.objects.filter(id=1)
    # print(ret,type(ret))
    #
    # # exclude
    # ret = models.Person.objects.exclude(id=1)
    # print(ret)
    #
    # # values，返回的是QuerySet对象，里面都是字典，不写的话默认查出所有
    # ret = models.Person.objects.values()
    # print(ret)
    #
    # # value_list，返回的是QuerySet对象，里面都是元组，不写的话默认返回所有
    # ret = models.Person.objects.values_list()
    # print(ret)
    #
    # # order_by，安装指定的顺序排序
    # ret = models.Person.objects.order_by("name")
    # print(ret)
    #
    # # reverse，将一个有序的的QuerySet进行反转
    # ret = models.Person.objects.order_by("name").reverse()
    # print(ret)
    #
    # # count，返回QuerySet的数量
    # ret = models.Person.objects.all().count()
    # print(ret)
    #
    # ret = models.Publisher.objects.all().count()
    # print(ret)
    #
    # # first, 返回QuerySet中第一个对象
    # ret = models.Publisher.objects.all().first()
    # print(ret)
    #
    # ret = models.Publisher.objects.first()
    # print(ret, type(ret))
    #
    # # last，返回QuerySet中最后一个对象
    # ret = models.Publisher.objects.all().last()
    # print(ret, type(ret))
    #
    # print("单表查询之双下划线".center(80, "*"))
    # # 查询id值大于1小于4的结果
    # ret = models.Publisher.objects.filter(id__gt=1, id__lt=4)
    # print(ret)
    #
    # # in，查询id在[1,3,5]中的结果
    # ret = models.Publisher.objects.filter(id__in=[1,3,5, 10])
    # print(ret)
    #
    # # containers 字段包含
    # ret = models.Book.objects.filter(title__contains="python")
    # print(ret)
    #
    # # icontainers 忽略大小写
    # ret = models.Book.objects.filter(title__icontains="PYTHON")
    # print(ret)
    #
    # # range 在什么范围之内，相当于between...and...
    # ret = models.Book.objects.filter(id__range=[3, 7])
    # print(ret)
    #
    # print("外键查询".center(80, "*"))
    # # 正向查询
    # book_obj = models.Book.objects.first()
    # print(book_obj, type(book_obj))
    # print(book_obj.publisher.name)
    #
    # # 查询ID=3的书的出版社的名称，双下划线跨表查询
    # print(models.Book.objects.filter(id=3))
    # ret = models.Book.objects.filter(id=3).values_list("publisher__name")
    # print(ret)
    #
    # # 反向查询
    # # 1、基于对象查询
    # publisher_obj = models.Publisher.objects.get(id=1)
    # ret = publisher_obj.books.all()
    # print(ret)
    #
    # # 2、基于双下划线，查询出版社id=1的所有书籍
    # ret = models.Publisher.objects.filter(id=1).values_list("xxoo__title")
    # print(ret)
    #
    # print("多对多查询".center(80, "*"))
    # # 查询
    # author_obj = models.Author.objects.get(id=1)
    # print(author_obj)
    #
    # # 查询Alex写过的书
    # ret = author_obj.books.all()
    # print(ret)
    #
    # # create 通过作者创建一本书
    # # author_obj.books.create(title="全民出击", publisher_id=1)
    #
    # # add 添加一本书id=7的书
    # # book_obj = models.Book.objects.get(id=7)
    # # author_obj.books.add(book_obj)
    #
    # # 添加多个书籍
    # # book_obj = models.Book.objects.filter(id__gt=6)
    # # print(book_obj)
    # # author_obj.books.add(*book_obj)
    #
    # # 直接添加id
    # # author_obj.books.add(9)
    #
    # # remove 把alex的全民出击删掉
    # # book_obj = models.Book.objects.filter(title="全民出击")
    # # print(book_obj)
    # # author_obj.books.remove(*book_obj)
    #
    # # 删除id=7的书籍
    # # author_obj.books.remove(7)
    #
    # # clear 把jack的书都清掉
    # # jack_obj = models.Author.objects.get(name="jack")
    # # jack_obj.books.clear()
    #
    # # 外键的反向操作
    # # 找到id=1的出版社
    # # publisher_obj = models.Publisher.objects.get(id=1)
    # # publisher_obj.books.clear()
    #
    # print("聚合操作".center(80, "*"))
    # from django.db.models import Avg, Sum, Max, Min, Count
    # # 计算所有书籍的平均值
    # ret = models.Book.objects.all().aggregate(price_avg = Avg("price"))
    # print(ret)
    #
    # # 查找所有书籍中价格最高、最低、总和
    # ret = models.Book.objects.all().aggregate(price_max = Max("price"), price_min =Min("price"), price_sum=Sum("price"))
    # print(ret)
    #
    # print("分组查询".center(80, "*"))
    # # 查询每一本书的作者个数
    # ret = models.Book.objects.all().annotate(author_num = Count("author"))
    # print(ret)
    # for book in ret:
    #     print("书名：{}  >>>>>>  作者个数：{}".format(book.title, book.author_num))
    #
    # # 查询作者数量大于0的书
    # ret = models.Book.objects.all().annotate(author_num = Count("author")).filter(author_num__gt=0)
    # print(ret)
    # for book in ret:
    #     print("书名：{}  >>>>>>  作者个数：{}".format(book.title, book.author_num))
    #
    # # 查询每个作者出的书的总价格
    # ret = models.Author.objects.all().annotate(price_sum = Sum("books__price"))
    # print(ret)
    # for author in ret:
    #     print("作者：{} >>>>>> 总价格：{}".format(author, author.price_sum))
    #
    # print("F和Q查询".center(80, "*"))
    # from django.db.models import F,  Value, Q
    # from django.db.models.functions import Concat
    # # 查询库存数大于卖出书的所有书
    # ret = models.Book.objects.filter(kucun__gt=F("maichu"))
    # print(ret)
    #
    # # 把每一本的卖出数都乘3
    # # models.Book.objects.update(maichu=(F("maichu")+1)*3)
    #
    # # 把每一本书的书名后面加上“第一版”
    # # models.Book.objects.update(title=Concat(F("title"), Value("第一版")))
    #
    # # 查询卖出数大于1000，价格小于100的书
    # ret = models.Book.objects.filter(maichu__gt=1000, price__lt=100)
    # print(ret)
    #
    # # 查询卖出数大于1000，或者价格小于100的书
    # ret = models.Book.objects.filter(Q(maichu__gt=1000) | Q(price__lt=100))
    # print(ret)
    #
    # # Q查询和字段查询同时存在时， 字段查询要放在Q查询的后面
    # ret = models.Book.objects.filter(Q(maichu__gt=1000) | Q(price__lt=100), title__contains="python")
    # print(ret)

    obbj = [models.Boook(name="学会写作第{}版".format(i)) for i in range(1000)]
    models.Boook.objects.bulk_create(obbj, 10)

    # models.Boook.objects.all().delete()