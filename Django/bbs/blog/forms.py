"""
form表单
"""
from django import forms
from django.core.exceptions import ValidationError
from blog import models


class RegForm(forms.Form):
    """注册Form表单"""
    username = forms.CharField(
        label="用户名",
        max_length=12,
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        ),
        error_messages={
            "max_length": "最长不超过12个字符",
            "invalid": "用户名格式错误",
            "required": "用户名不能为空",
        }
    )

    password = forms.CharField(
        label="密码",
        min_length=6,
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
        ),
        error_messages={
            "min_length": "密码不少于6个字符",
            "required": "密码不能为空",
        }
    )

    re_password = forms.CharField(
        label="密码",
        min_length=6,
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
        ),
        error_messages={
            "min_length": "密码不少于6个字符",
            "required": "密码不能为空",
        }
    )

    email = forms.CharField(
        label="邮箱",
        max_length=32,
        widget=forms.widgets.EmailInput(
            attrs={"class": "form-control"},
        ),
        error_messages={
            "max_length": "邮箱名不超过32位",
            "required": "邮箱不能为空",
            "invalid": "邮箱格式错误，示例：xxx@xxx.com"
        }
    )

    # 重新clean_username,检验用户名是否被注册
    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_check = models.UserInfo.objects.filter(username=username)
        if is_check:
            # 用户名已经存在
            self.add_error("username", ValidationError("用户名已经存在"))
        else:
            return username

    # 重新clean_email,检验邮箱是否被注册
    def clean_email(self):
        email = self.cleaned_data.get("email")
        is_check = models.UserInfo.objects.filter(email=email)
        if is_check:
            # 邮箱名已经存在
            self.add_error("email", ValidationError("邮箱已注册"))
        else:
            return email

    # 校验两次密码输入是否一致
    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if re_password and re_password != password:
            self.add_error("re_password", ValidationError("两次密码不一致！"))
        else:
            return self.cleaned_data

