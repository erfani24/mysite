from django.shortcuts import render
from .models import Post

# Create your views here.

def blog_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single (request):
    return render(request, 'blog/blog-single.html')

def test(request,pid):
    post = Post.objects.get(id=pid)
    context = {'post': post}
    return render(request,'blog/test.html', context)