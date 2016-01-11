from django.contrib import admin
from .models import Article
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

admin.site.register(Article,MarkdownModelAdmin)