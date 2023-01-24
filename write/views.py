from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CommentForm, WordArtForm


# About Page
class About(generic.TemplateView):
    def about(request):
        return render(request, 'templates/about.html')


# WordArt Page
class WordartList(generic.ListView):
    model = Post
    context_object_name = 'wordart_list'
    template_name = 'wordart.html'
    queryset = Post.objects.all().filter(
        approved=True).order_by('-created_date')


# WordArt Page - Post Detail view
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
                'commented': False,
                'likes': liked,
                'comment_form': CommentForm()
            },
        )

    # leave a comment

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_date')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists:
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'likes': liked,
                'comment_form': CommentForm()
            },
        )


# Like / Unlike a post
class LikeUnlike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Create a Post
def add_wordart(request):
    context = {}

    form = WordArtForm(request.POST or None)
    if form.is_valid():
        form.instance.author = User.objects.get(username=request.user.username)
        form.save()

        messages.success(
            request, 'Your submission was successful and is awaiting approval')
        return HttpResponseRedirect(reverse('wordart'))

    context['form'] = form
    return render(request, 'add_wordart.html', context)
