"""orm_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from orm import views
from app02 import views as app02

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^transfer/', views.transfer),
    url(r'^books/', views.books),
    url(r'^login/', views.login),
    url(r'^home/', views.home),

    url(r'^app02/transfer/', app02.transfer),
    url(r'^app02/books/', app02.books),
    url(r'^app02/login/', app02.login),
    url(r'^app02/home/', app02.home),
    url(r'^app02/index/', app02.HomeView.as_view()),
]
