# coding=utf-8
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404
from article.models import Article


# Create your views here.
def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    print post_list
    return render(request, 'home.html', {'post_list': post_list})
    # return HttpResponse("Hello World!")

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})

def about_me(request) :
    return render(request, 'aboutme.html')
