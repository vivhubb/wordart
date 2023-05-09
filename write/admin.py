from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from django.utils.text import slugify


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('category', 'title', 'created_date', 'approved')
    list_filter = ('category', 'created_date', 'approved')
    search_fields = ['category', 'title', 'content', 'approved']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    actions = ['approve_posts', 'save_model']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        obj.slug = slugify(form.cleaned_data.get('title')) + '-' + str(obj.id)
        super().save_model(request, obj, form, change)

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'comment', 'created_date', 'approved')
    list_filter = ('created_date', 'approved')
    search_fields = ('name', 'post', 'created_date', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
