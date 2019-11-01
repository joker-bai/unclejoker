from django.db import models


# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    pwd = models.CharField(max_length=32, default="123456")
    email = models.CharField(max_length=32, null=True)
    mobile = models.CharField(max_length=11, null=True)

class Userinfo(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = "userinfo"