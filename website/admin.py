from django.contrib import admin
from .models import Contact,Newsletter

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy= 'created_date'
    list_display = ['name', 'email','subject','created_date']
    search_fields = ['name', 'email', 'message']
    list_filter = ['email']
admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter,)