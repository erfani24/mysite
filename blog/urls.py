
from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('',blog_view, name="index"),
    path('<int:pid>/',blog_single,name='single'),
    path('post-<int:pid>/',test),
    path('category/<str:cat_name>/',blog_view,name='category'),
    path('tag/<str:tag_name>/',blog_view,name='tag'),
    path('writer/<str:writer_name>/',blog_view,name='writer'),
    path('search/',blog_search ,name='search')
]
