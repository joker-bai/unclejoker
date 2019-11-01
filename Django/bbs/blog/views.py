import json
from bs4 import BeautifulSoup
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from blog import models
from django.contrib import auth
from geetest import GeetestLib
from blog import forms
from django.db.models import Count
from django.db.models import F

# Create your views here.
# 请在官网申请ID使用，示例ID不可使用
pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"


def login(request):
    if request.method == 'POST':
        # 初始化一个给AJAX返回的数据
        ret = {"status": 0, "msg": ""}
        # 从提交过来的数据中 取到用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 获取极验 滑动验证码相关的参数
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]

        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            # 验证码正确
            # 利用auth模块做用户名和密码的校验
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 用户名密码正确
                # 给用户做登录
                auth.login(request, user)
                ret["msg"] = "/index/"
            else:
                # 用户名密码错误
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"

        return JsonResponse(ret)
    return render(request, "login.html")


def index(request):
    article_list = models.Article.objects.all()
    return render(request, "index.html", {"article_list": article_list})


def get_geetest_register(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


def file(request):
    if request.method == "POST":
        file_obj = request.FILES.get("file")
        print(file_obj)
        with open(file_obj.name, 'wb') as f:
            for line in file_obj.chunks():
                f.write(line)
        return HttpResponse("上传成功")
    return render(request, "file.html")


# 注册视图
def register(request):
    reg_form_obj = forms.RegForm()

    if request.method == "POST":
        # 定义一个字典，保存信息
        check_res = {"status": 0, "msg": ""}
        reg_form_obj = forms.RegForm(request.POST)
        if reg_form_obj.is_valid():
            # 注册成功，在数据库中创建用户
            del reg_form_obj.cleaned_data["re_password"]
            # 获取头像
            avatar_img = request.FILES.get("avatar")
            models.UserInfo.objects.create_user(**reg_form_obj.cleaned_data, avatar=avatar_img)
            # 注册成功，将需要跳转的页面保存到msg中
            check_res["msg"] = "/index/"
            return JsonResponse(check_res)
        else:
            # 注册失败，将错误信息保存到msg
            check_res["status"] = 1
            check_res["msg"] = reg_form_obj.errors
            # print(check_res)
            return JsonResponse(check_res)
    return render(request, "register.html", {"reg_form_obj": reg_form_obj})


# 检查用户名
def check_username(request):
    ret = {"status": 0, "msg": ""}
    username = request.POST.get("username")
    is_check = models.UserInfo.objects.filter(username=username)
    if is_check:
        ret["status"] = 1
        ret["msg"] = "用户名已经存在"
        print(ret)
        return JsonResponse(ret)


# 注销用户
def logout(request):
    auth.logout(request)
    return redirect("/index/")


# 用户个人页面
def home(request, username):
    # 找到用户对象
    user_obj = models.UserInfo.objects.filter(username=username).first()
    # 如果用户不存在，返回404页面，如果用户存在就返回用户对象
    if not user_obj:
        return render(request, '404.html')
        # return HttpResponse("404")
    # 获取文章列表
    article_list = models.Article.objects.filter(user=user_obj)
    return render(request, 'home.html', {
        "username": username,
        "user_obj": user_obj,
        "article_list": article_list,
    })


def article_detial(request, username, pk):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    if not user_obj:
        return HttpResponse("404")
    article_obj = models.Article.objects.filter(pk=pk).first()
    # 评论列表
    comment_list = models.Comment.objects.filter(article_id=pk)
    return render(request, "article_detial.html",
                  {
                      "username": username,
                      "article_obj": article_obj,
                      "user_obj": user_obj,
                      "comment_list": comment_list
                  })


# 处理点赞或点踩视图
def up_down(request):
    user = request.user
    article_id = request.POST.get("article_id")
    is_up = json.loads(request.POST.get("is_up"))
    ret = {"status": True, "msg": ""}
    # 如果这个用户登录了，就更新
    try:
        models.ArticleUpDown.objects.create(user=user, article_id=article_id, is_up=is_up)
        # 如果is_up为True，就更新Article的up_count字段，否则更新down_count字段
        if is_up:
            models.Article.objects.filter(pk=article_id).update(up_count=F("up_count") + 1)
        else:
            models.Article.objects.filter(pk=article_id).update(down_count=F("down_count") + 1)
        ret["msg"] = "感谢推荐"
    except Exception as e:
        ret["status"] = False
        if not user.username:
            ret["msg"] = '请<a href="/login/">登录</a>'
            # ret["msg"] = '请登录'
        else:
            status = models.ArticleUpDown.objects.filter(user=user, article_id=article_id).first().is_up
            if status:
                ret["msg"] = "您已经推荐过"
            else:
                ret["msg"] = "您已经反对过"
    return JsonResponse(ret)


# 处理评论的方法
def comment(request):
    response = {}
    # print(request.POST)
    pid = request.POST.get("pid")
    content = request.POST.get("content")
    article_id = request.POST.get("article_id")
    user_id = request.user.pk
    # 如果Pid为空，则为父评论
    if not pid:
        comment_obj = models.Comment.objects.create(article_id=article_id, content=content, user_id=user_id)
    else:
        comment_obj = models.Comment.objects.create(article_id=article_id, content=content, user_id=user_id,
                                                    parent_comment_id=pid)
    response["content"] = comment_obj.content
    response["username"] = comment_obj.user.username
    return JsonResponse(response)


# 处理评论数
def comment_tree(request, article_id):
    # 获取对应文章的所有评论
    print(article_id)
    response = []
    comment_obj = models.Comment.objects.filter(article_id=article_id)
    for i in comment_obj:
        ret = {"pk": i.pk, "content": i.content, "parent_comment_id": i.parent_comment_id, "user": i.user.username}
        response.append(ret)
    return JsonResponse(response, safe=False)


# 后台文章
def backend_article(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("article_title")
        article_content = request.POST.get("article_content")
        # 对文章内容做格式化
        bs = BeautifulSoup(article_content, "html.parser")
        desc = bs.text[0:150] + "......"
        # 防止xss攻击，处理非法标签
        illegal_tags = ["script", "link"]
        for tag in bs.find_all():
            if tag in illegal_tags:
                tag.decompose()
        # 插入数据库
        article_obj = models.Article.objects.create(title=title, desc=desc, user=user)
        models.ArticleDetail.objects.create(content=str(bs), article=article_obj)
        return HttpResponse("OK")

    return render(request, "backend_article.html")


# 后台文件上传
from bbs import settings
import os


def upload(request):
    # print(request.FILES)
    files_obj = request.FILES.get("imgFile")
    # 将上传得文件保存到服务器
    path = os.path.join(settings.MEDIA_ROOT, "article_upload", files_obj.name)
    with open(path, 'wb') as f:
        for line in files_obj:
            f.write(line)

    # 获取上传结果
    res = {
        "error": 0,
        "url": "/media/article_upload/" + files_obj.name
    }
    return JsonResponse(res)
    # return HttpResponse(json.dumps(res))
