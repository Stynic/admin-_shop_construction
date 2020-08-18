from django.shortcuts import render

from django.shortcuts import render
from blog.models import Post


def post_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_index.html', context)


def post_detail(request, pk):
    posts = Post.objects.get(pk=pk)
    posts.image.name = posts.image.name.split('static/')[1]
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_detail.html', context)