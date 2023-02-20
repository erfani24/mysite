from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message =models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)