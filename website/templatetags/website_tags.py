from django import template
from blog.models import Post,Category
from django.utils import timezone

register = template.Library()


@register.inclusion_tag('website/website-latest-blog.html')
def w_latest_blog():
    today = timezone.now()
    posts = Post.objects.filter(published_date__lte = today,status=1).order_by('-published_date')[:6]
    return {'posts': posts}
