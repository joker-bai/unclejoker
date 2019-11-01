from django.db import models

# Create your models here.

#
# class Publisher(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=32, unique=True)
#
#     def __str__(self):
#         return "Object:{}".format(self.name)
#
#
# class Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     price = models.DecimalField(max_digits=5, decimal_places=2, default=99.99)
#     # 库存数
#     kucun = models.IntegerField(default=1000)
#     # 卖出数
#     maichu = models.IntegerField(default=0)
#
#     title = models.CharField(max_length=32)
#     # 外键
#     # related_name="books" 反向查询是用来代替 book_set的
#     publisher = models.ForeignKey(
#         to="Publisher",
#         on_delete=models.CASCADE,
#         related_name="books",
#         related_query_name="xxoo",
#         null=True
#     )
#
#     def __str__(self):
#         return self.title
#
#
# class Author(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=32)
#     books = models.ManyToManyField(to="Book")
#
#     def __str__(self):
#         return self.name
#
#
# class FixedCharField(models.Field):
#     """
#     自定义的char类型的字段类
#     """
#     def __init__(self, max_length, *args, **kwargs):
#         self.max_length = max_length
#         super(FixedCharField, self).__init__(max_length=max_length, *args, **kwargs)
#
#     def db_type(self, connection):
#         """
#         限定生成数据库表的字段类型为char，长度为max_length指定的值
#         """
#         return 'char(%s)' % self.max_length
#
#
# class Person(models.Model):
#     name = models.CharField(max_length=32)
#     age = models.IntegerField(default=18)
#     birthday = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return "<Person Object:{}>".format(self.name)
#
#     # class Meta:
#     #     ordering = ("birthday",)

class Boook(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "book"


class Userinfo(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = "userinfo"
