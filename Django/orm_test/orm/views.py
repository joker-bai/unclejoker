from django.shortcuts import render, HttpResponse, redirect
from orm import models
from utils.mypage import Page
from functools import wraps

# Create your views here.


# 装饰器
def check_login_status(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        # 获取cookie
        get_cookie = request.get_signed_cookie("is_login", salt="login", default=None)
        next_url = request.path_info
        if get_cookie == "123":
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(next_url))
    return inner


def login(request):
    """用户登录"""
    if request.method == "POST":
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        # 获取跳转url
        next_url = request.GET.get("next")
        check_username = models.Userinfo.objects.filter(username=user)
        if check_username:
            if pwd == check_username[0].password:
                if next_url:
                    ret = redirect("{}".format(next_url))
                else:
                    ret = redirect("/home/")
                ret.set_signed_cookie("is_login", "123", salt="login")
                return ret
    return render(request, "login.html")


@check_login_status
def home(request):
    return render(request, "home.html")


@check_login_status
def transfer(request):
    if request.method == "POST":
        from_ = request.POST.get("from")
        to_ = request.POST.get("to")
        money = request.POST.get("money")

        print("{} 转给 {} {}元".format(from_, to_, money))

        return HttpResponse("转账成功")

    return render(request, "transfer.html")


@check_login_status
def books(request):
    try:
        page = int(request.GET.get("page"))
    except Exception as e:
        page = 1
    # 获取书籍的总数
    total_count = models.Boook.objects.all().count()
    #
    # # 计算可分的页数，每页最多10本书籍
    # page_book_num = 10
    # page_num, other = divmod(total_book, page_book_num)
    # if other:
    #     page_num += 1
    # if page > page_num:
    #     page = page_num
    # # print(page_num, other)
    # start_page = (page - 1) * 10
    # end_page = page * 10
    # # 当前页最大展示页
    # max_page = 9
    # if page_num < max_page:
    #     max_page = page_num
    # half_page_num = max_page // 2
    # # print(half_page_num)
    # if page - half_page_num <= 1:
    #     page_start = 1
    #     page_end = max_page
    # elif page + half_page_num > page_num:
    #     page_end = page_num
    #     page_start = page_num - max_page + 1
    # else:
    #     # 计算分页，用于切片
    #     page_start = page - half_page_num
    #     page_end = page + half_page_num
    # page_list = [i for i in range(page_start, page_end + 1)]
    # print(page_list)
    # 查询所有书籍
    page_obj = Page(page, total_count, url_prefix="/books/")

    all_book = models.Boook.objects.all()[page_obj.start: page_obj.end]
    print(all_book)
    page_html = page_obj.page_html()
    # return  render(request, "books.html", {"all_book": all_book, "page_list": page_list, "page_total": page_num,
    #                                        "page_now": page})
    return render(request, "books.html", {"books": all_book, "page_html": page_html})
