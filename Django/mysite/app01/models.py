from django.db import models

# Create your models here.


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=64)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=64)
    publisher = models.ForeignKey(to=Publisher)


# 作者表
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=64)
    # 告诉ORM，这张表和Book表是多对多的关联关系，ORM自动生成第三张表
    book = models.ManyToManyField(to="Book")


# # 作者与书的对应关系
# class AuthorToBook(models.Model):
#     id = models.AutoField(primary_key=True)
#     author = models.ForeignKey(to="Author")
#     book = models.ForeignKey(to="Book")
