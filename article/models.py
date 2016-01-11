# coding=utf-8
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django_markdown.models import MarkdownField
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)  # 博客题目
    category = models.CharField(max_length=50, blank=True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = MarkdownField()  # 博客文章正文   这里为了使用django_markdown将Text换成了MarkdownField

    # 获取URL并转换成url的表示格式  这里需不需要改变数据库即进行移植操作？发现并不需要进行数据库的移植就可以改变。
    # 还有这里进行了函数的定义是为什么使用这个类的对象的时候能够调用出来绝对的url地址
    def get_absolute_url(self):
        # path = reverse('detail', kwargs={'id':self.id})
        path = reverse('detail', args=[3])
        return "http://127.0.0.1:8000%s" % path  # 注意这里8000后面是没有反斜杠的，md，还看了一会才发现

    # python2使用__unicode__, python3使用__str__      #md,这里python2必须使用unicode，不然标题输入中文的时候会报错
    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序     这里为什么要使用一个类来进行对一个东西的排序
        ordering = ['-date_time']
