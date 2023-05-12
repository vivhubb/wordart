import re
from .models import Post, Comment
from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class WordArtForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = True

    class Meta:
        model = Post
        fields = (
            'category', 'title', 'content', 'ownership', 'creator'
        )
        widgets = {
            'content': SummernoteWidget(
                attrs={
                    'summernote': {'width': '100%'}
                }
            )
        }

    def clean_content(self):
        content = self.cleaned_data['content']
        tmp = re.sub(r'<.*?>', '', content)
        if len(tmp.replace('&nbsp;', ' ').strip()) == 0:
            raise forms.ValidationError('The Content* field is required!')
        return content
