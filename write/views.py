from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm


class About(generic.TemplateView):
    def about(request):
        return render(request, 'templates/about.html')


class WordartList(generic.ListView):
    model = Post
    context_object_name = 'wordart_list'
    template_name = 'wordart.html'
    queryset = Post.objects.all().filter(
        approved=True).order_by('-created_date')


class Register(generic.TemplateView):
    def register(request):
        return render(request, 'templates/register.html')


class PostWordArt(generic.TemplateView):
    def add_wordart(request):
        return render(request, 'templates/add_wordart.html')
