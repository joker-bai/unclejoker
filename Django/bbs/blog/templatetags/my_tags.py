from django import template
from blog import models
from django.db.models import Count
register = template.Library()


@register.inclusion_tag("left_page.html")
def get_left_page(username):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    # 获取个人的所有分类
    # category_list = models.Category.objects.filter(blog=user_obj.blog)
    category_list = models.Category.objects.filter(blog=user_obj.blog).annotate(c=Count("article")).values("title", 'c')
    # 获取文章标签
    tag_list = models.Tag.objects.filter(blog=user_obj.blog).annotate(c=Count("article")).values("title", "c")
    # 按日期归档
    archive_list = models.Article.objects.filter(user=user_obj).extra(
        select={"archive_date": "DATE(create_time)"}
    ).values("archive_date").annotate(c=Count("nid")).values("archive_date", "c")
    return {
        "category_list": category_list,
        "tag_list": tag_list,
        "archive_list": archive_list
    }