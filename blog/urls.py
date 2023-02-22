
from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('',blog_view, name="index"),
    path('single/',blog_single,name='blog-single'),
    path('post-<int:pid>/',test)
    
    
]
