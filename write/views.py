from django.shortcuts import render
from django.views import generic
from .models import Post


class About(generic.TemplateView,):
    def about(request):
        return render(
            request, 'write/templates/about.html')


class WordartList(generic.ListView):
    model = Post
    context_object_name = 'quotes_list'
    template_name = 'wordart.html'
    # queryset = Post.objects.order_by('-created_date')


class Register(generic.TemplateView):
    def register(request):
        return render(
            request, 'write/templates/register.html')
