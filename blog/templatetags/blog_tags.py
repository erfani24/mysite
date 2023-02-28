from django import template
from blog.models import Post,Category
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts():
    today = timezone.now()
    posts = Post.objects.filter(published_date__lte = today,status=1).order_by('-published_date')[:5]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-category.html')
def postcategories():
    today = timezone.now()
    posts = Post.objects.filter(published_date__lte = today,status=1)
    cats = Category.objects.all()
    cat_names = {}
    for name in cats:
        cat_names[name] = Post.objects.filter(category=name).count()
    return {'postcategories': cat_names}