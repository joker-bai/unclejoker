from django.shortcuts import render, HttpResponse, redirect
from app01 import models

# Create your views here.


def login(request):
    error_message = ''
    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        if email == "joker@163.com" and password == "123456":
            return HttpResponse("登录成功！")
        else:
            error_message = "邮箱或密码错误！"
    return render(request, "login.html", {"error": error_message})


def baobao(request):
    # 获取用户提交的数据
    email = request.POST.get("email", None)
    password = request.POST.get("password", None)
    if email == "joker@163.com" and password == "123456":
        return HttpResponse("登录成功！")
    else:
        return HttpResponse("登录失败！")


# 出版社列表
def publisher_list(request):
    all_publisher = models.Publisher.objects.all()
    print(all_publisher)
    return render(request, "publisher_list.html", {"publisher_list": all_publisher})


# 添加出版社
def add_publisher(request):
    if request.method == "POST":
        print(request.POST)
        p_name = request.POST.get("p_name", None)
        print(p_name)
        models.Publisher.objects.create(name=p_name)
        return redirect("/publisher_list/")
    return render(request, "add_publisher.html")


# 删除
def delete_publisher(request, *args):
    print(args)
    # delete_id = request.GET.get("id", None)
    delete_id = args[0]
    print(delete_id)
    if delete_id:
        del_obj = models.Publisher.objects.get(id=delete_id)
        del_obj.delete()
        return redirect("/publisher_list/")
    else:
        return HttpResponse("要删除的页面不存在")


# 修改
def edit_publisher(request, *args):
    if request.method == "POST":
        edit_id = request.POST.get("id", None)
        edit_name = request.POST.get("edit_name", None)
        edit_obj = models.Publisher.objects.get(id=edit_id)
        edit_obj.name = edit_name
        edit_obj.save()
        return redirect("/publisher_list/")
    # ed_id = request.GET.get("id", None)
    ed_id = args[0]
    if ed_id:
        edit_publisher_obj = models.Publisher.objects.get(id=ed_id)
        return render(request, "edit_publisher.html", {"publisher": edit_publisher_obj})
    else:
        return HttpResponse("编辑的出版社不存在。")


# 书籍列表
def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, "book_list.html", {"book_list": all_book})


# 添加书籍
def add_book(request):
    if request.method == "POST":
        new_book_name = request.POST.get("book_name", None)
        new_p_name = request.POST.get("p_name", None)
        # print(new_book_name, new_p_name)
        models.Book.objects.create(name=new_book_name, publisher_id=new_p_name)
        return redirect("/book_list/")
    all_publisher = models.Publisher.objects.all()
    return render(request, "add_book.html", {"publisher_list": all_publisher})


# 删除页面
def delete_book(request, *args):
    # delete_id = request.GET.get("id", None)
    delete_id = args[0]
    if delete_id:
        models.Book.objects.get(id=delete_id).delete()
        return redirect("/book_list/")
    else:
        return HttpResponse("要删除的书籍不存在。")


# 修改页面
def edit_book(request, *args):
    if request.method == "POST":
        edit_id = request.POST.get("id", None)
        edit_book = request.POST.get("book_name", None)
        edit_pub_id = request.POST.get("publisher", None)
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.name = edit_book
        edit_book_obj.publisher_id = edit_pub_id
        edit_book_obj.save()
        return redirect("/book_list/")
    # edit_id = request.GET.get("id", None)
    edit_id = args[0]
    edit_book_obj = models.Book.objects.get(id=edit_id)
    publish_obj = models.Publisher.objects.all()
    # print(edit_book_obj.id)
    # print(edit_book_obj.name)
    return render(request, "edit_book.html", {"book_list": edit_book_obj, "publisher_list": publish_obj})


# 作者列表
def author_list(request):
    # 取所有作者信息
    all_author = models.Author.objects.all()
    return render(request, "author_list.html", {"author_list": all_author})

# 添加作者信息
def add_author(request):
    if request.method == "POST":
        author_name = request.POST.get("author_name", None)
        books = request.POST.getlist("author_books", None)
        # print(author_name, books)
        author_obj = models.Author.objects.create(name=author_name)
        author_obj.book.set(books)
        return redirect("/author_list/")
    # 读取所有书籍
    all_book = models.Book.objects.all()
    return render(request, "add_author.html", {"book_list": all_book})


# 删除作者信息
def delete_author(request, *args):
    # 读取要删除的ID
    # delete_id = request.GET.get("id", None)
    delete_id = args[0]
    # 找到对象
    models.Author.objects.get(id=delete_id).delete()
    return redirect("/author_list/")


# 编辑作者信息
def edit_author(request, *args):
    if request.method == "POST":
        # 获取到ID
        new_edit_id = request.POST.get("author_id", None)
        # 获取到名字
        new_edit_name = request.POST.get("author_name", None)
        # 获取到书籍
        new_edit_books = request.POST.getlist("author_books", None)
        # 获取对象
        edit_obj = models.Author.objects.get(id=new_edit_id)
        edit_obj.name = new_edit_name
        edit_obj.book.set(new_edit_books)
        edit_obj.save()
        return redirect("/author_list/")
    # 根据ID找到作者信息
    # edit_id = request.GET.get("id", None)
    edit_id = args[0]
    edit_author_obj = models.Author.objects.get(id=edit_id)
    # 找到书籍
    all_book = models.Book.objects.all()
    return render(request, "edit_author.html", {"book_list": all_book, "author": edit_author_obj})


def filter_test(request):
    return render(request, "filter_test.html")
