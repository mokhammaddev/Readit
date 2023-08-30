from django.contrib import admin
from .models import Article, Category, Tag, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_date']
    list_filter = ['category', 'tags']
    search_fields = ['id', 'title']
    date_hierarchy = 'created_date'
    filter_horizontal = ['tags', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'article', 'created_date']
    date_hierarchy = 'created_date'
    search_fields = ['article__title', 'author__username']
    autocomplete_fields = ['author', 'article']


