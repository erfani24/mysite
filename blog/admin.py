from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('id', 'title','author', 'status', 'created_date', 'published_date')
    search_fields = ['title','content']
    list_filter = ('status','created_date',)
    summernote_fields = ('content',)
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category)