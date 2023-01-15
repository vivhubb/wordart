from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('category', 'title', 'created_date', 'approved')
    search_fields = ['category', 'title', 'content', 'approved']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'created_date', 'approved')
    summernote_fields = ('content')
