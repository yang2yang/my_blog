# coding=utf-8
"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from article import views #这里为什么直接导入article不行？而是需要导入views，说是找不到这个属性
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home,name="home"),
    url(r'^test/$', views.test),
    url(r'^page/(\d+)$', views.detail, name='detail'),#这里我不知道为什么在官方教程中总是有尖括号扩起来是用来表示什么呢？
    url(r'^aboutme/$',views.about_me,name='about_me'),
    url(r'^markdown/', include('django_markdown.urls')), #这里是安装django_markdown的url
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
