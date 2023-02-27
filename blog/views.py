from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime
# Create your views here.

def blog_view(request,cat_name=None, writer_name=None):
    today = datetime.now()
    posts = Post.objects.filter(published_date__lte = today,status = 1) 
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if writer_name:
        posts = posts.filter(author__username=writer_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single (request,pid):
    post = get_object_or_404(Post,id = pid, status = 1)
    post.counted_views += 1
    post.save()
    
    # finding next and previous posts
    today = datetime.now()
    posts = Post.objects.filter(published_date__lte = today,status = 1)
    post_list = []
    for index, obj in enumerate(posts):
        post_list.append(obj)
    post_list.reverse()
    ind =post_list.index(post)
    
    if ind > 0:
        pre_post = post_list[ind - 1]
    else:
        pre_post = post_list[ind]
        
    if ind < len(post_list) - 1:
        nex_post = post_list[ind + 1]
    else:
        nex_post = post_list[ind]
    context = {'post' : post,
               'pre_post': pre_post,
               'nex_post': nex_post
               }
    return render(request, 'blog/blog-single.html', context)

def test(request,pid):
    post = Post.objects.get(id=pid)
    context = {'post': post}
    return render(request,'blog/test.html', context)

def blog_category(request,cat_name):
    today = datetime.now()
    posts = Post.objects.filter(published_date__lte = today,status = 1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)