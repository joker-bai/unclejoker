from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'backend/backend_article/', views.backend_article),
    url(r'up_down/$', views.up_down),
    url(r'comment/$', views.comment),
    url(r'comment_tree/(\d+)/', views.comment_tree),
    url(r'(\w+)/(\d+)/', views.article_detial),
    url(r'(\w+)', views.home),
]