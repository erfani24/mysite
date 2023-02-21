from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('id', 'title', 'status', 'created_date')
    search_fields = ['title','content']
    list_filter = ('status','created_date',)

admin.site.register(Post,PostAdmin)