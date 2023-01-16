from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('category', 'title', 'created_date', 'approved')
    list_filter = ('category', 'created_date', 'approved')
    search_fields = ['category', 'title', 'content', 'approved']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'comment', 'created_date', 'approved')
    list_filter = ('created_date', 'approved')
    search_fields = ('name', 'post', 'created_date', 'approved')
