from django.db import models
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    published = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to= 'static/img/blog/')
    description = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
class ContactMessages(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    message = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.name