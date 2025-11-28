from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    nombre = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    imagen = models.ImageField(upload_to='SocialApp', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title     