from .models import Post, Comment
from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class WordArtForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'category', 'title', 'content', 'ownership', 'creator')
        widgets = {
            'content': SummernoteWidget(
                attrs={
                    'summernote': {'width': '100%'}
                }
            )
        }
