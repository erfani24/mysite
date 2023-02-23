from django.shortcuts import render, get_object_or_404
from .models import Post
from datetime import datetime
# Create your views here.

def blog_view(request):
    today = datetime.now()
    posts = Post.objects.filter(published_date__lte = today) 
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single (request,pid):
    post = get_object_or_404(Post,id = pid)
    post.counted_views += 1
    post.save()
    context = {"post" : post}
    return render(request, 'blog/blog-single.html', context)

def test(request,pid):
    post = Post.objects.get(id=pid)
    context = {'post': post}
    return render(request,'blog/test.html', context)