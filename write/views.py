from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_date')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists:
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'likes': liked
            }
        )


class PostWordArt(generic.TemplateView):
    def add_wordart(request):
        return render(request, 'templates/add_wordart.html')
