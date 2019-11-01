from django.shortcuts import render, HttpResponse, redirect
from app01 import models

# # Create your views here.
#
#
# def index(request):
#     return render(request, "index.html")
#
#
# def ajax_add(request):
#     print(request.POST)
#     i1 = int(request.POST.get("i1"))
#     i2 = int(request.POST.get("i2"))
#     print(type(i1), type(i2))
#     ret = i1 + i2
#     print(ret)
#     return HttpResponse(ret)
#
#
# def user_registration(request):
#     return render(request, "user.html")
#
#
# def user_check(request):
#     data = request.POST.get("text_data")
#     if not data:
#         flag = '用户名不能为空'
#     else:
#         select_res = models.User.objects.filter(username=data)
#         if not select_res:
#             flag = '检验通过'
#         else:
#             flag = '用户名存在'
#     return HttpResponse(flag)
#
#
# def user_add(request):
#     username = request.POST.get("username")
#     passwd = request.POST.get("password")
#     models.User.objects.last().add(username=username)
#     return redirect("/user_registration/")
#
#
# def person(request):
#     ret = models.User.objects.all()
#     return render(request, "sweetalert.html", {"persons": ret})
#
#
# def delete(request):
#     del_id = request.POST.get("id")
#     models.User.objects.filter(id=del_id).delete()
#     return HttpResponse("删除成功！")
#
# def login(request):
#     return render(request, "login.html")
#
#
# # Django版Form表单
# from django import forms
# from django.forms import widgets
# from django.core.validators import RegexValidator
# from django.core.exceptions import ValidationError
#
#
# class TestForm(forms.Form):
#     username = forms.CharField(
#         max_length=24,
#         label="用户名",
#         error_messages={
#             "required": "用户名不能为空",
#             "invalid": "用户名格式错误",
#             "max_length": "用户名最长24位",
#         },
#         widget=widgets.TextInput(attrs={"class": "form-control"})
#     )
#     pwd = forms.CharField(
#         min_length=6,
#         label="密码",
#         widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
#         error_messages={
#             "min_length": "密码不得少于6位",
#             "required": "该字段不能为空",
#         }
#     )
#     re_pwd = forms.CharField(
#         min_length=6,
#         label="确认密码",
#         widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
#         error_messages={
#             "min_length": "密码不得少于6位",
#             "required": "该字段不能为空",
#         }
#     )
#     email = forms.EmailField(
#         max_length=32,
#         label="邮箱",
#         widget=widgets.EmailInput(attrs={"class": "form-control"}),
#         error_messages={
#             "max_length": "密码不得少于6位",
#             "required": "该字段不能为空",
#         }
#     )
#     mobile = forms.CharField(
#         max_length=11,
#         min_length=11,
#         label="手机号码",
#         validators=[
#             RegexValidator(r'^[0-9]{11}$', '请输入数字'),
#             RegexValidator(r'^1[^012][0-9]{9}$', '手机号码不正确'),
#         ],
#         widget=widgets.TextInput(attrs={"class": "form-control"}),
#         error_messages={
#             "min_length": "密码不得少于11位",
#             "max_length": "密码不得多于11位",
#             "required": "该字段不能为空",
#         }
#     )
#
#     # 检查注册用户名
#     def clean_username(self):
#         value = self.cleaned_data.get("username")
#         name_check = models.User.objects.filter(username=value)
#         if name_check:
#             raise ValidationError("改用户名已注册")
#         ban_list = ["金瓶梅"]
#         for ban in ban_list:
#             if ban in value:
#                 raise ValidationError("改用户名不可用于注册")
#         return value
#
#     # 检查密码两次密码输入是否相同
#     def clean(self):
#         pwd = self.cleaned_data.get("pwd")
#         re_pwd = self.cleaned_data.get("re_pwd")
#         if re_pwd != pwd:
#             self.add_error("re_pwd", ValidationError("两次密码输入不一致"))
#             raise ValidationError("两次密码输入不一致")
#         return self.cleaned_data
#
# def form_test(request):
#     form_obj = TestForm()
#
#     if request.method == 'POST':
#         form_obj = TestForm(request.POST)
#         print(form_obj.errors)
#         if form_obj.is_valid():
#             print(form_obj.cleaned_data)
#             del form_obj.cleaned_data["re_pwd"]
#             models.User.objects.create(**form_obj.cleaned_data)
#             return HttpResponse('注册成功')
#     return render(request, "from_test.html", {"form_obj": form_obj})
#
#
# from functools import wraps
#
#
# def check_login(f):
#     @wraps(f)
#     def inner(request, *args, **kwargs):
#         if request.session["is_login"] == '1':
#             return f(request, *args, **kwargs)
#         else:
#             return HttpResponse("/login/")
#     return inner
#
#
# @check_login
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         # 校验用户名和密码
#         check_user = models.User.objects.filter(username=username, pwd=password)
#         if check_user:
#             request.session["is_login"] = '1'
#             return render(request, 'test.html')
#     return render(request, "login.html")


from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def test(request):
    return render(request, 'test.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return render(request, "test.html")
    return render(request, "login.html")


def register(request):
    User.objects.create_user(username="alex", password="alex123456")
    return HttpResponse("用户名创建成功")


def logout(request):
    auth.logout(request)
    return redirect("/login/")
