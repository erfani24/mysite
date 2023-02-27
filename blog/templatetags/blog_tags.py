from django import template
from blog.models import Post
from datetime import datetime

register = template.Library()

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts():
    today = datetime.now()
    posts = Post.objects.filter(published_date__lte = today,status=1).order_by('-published_date')[:5]
    return {'posts': posts}