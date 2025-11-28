from django.shortcuts import render
from .models import Post, Category  


# Create your views here.

def social(request):
    SocialAp=Post.objects.all()
    return render(request, 'SocialApp/social.html', {'SocialApps': SocialAp})

def category(request, category_id):
    category=Category.objects.get(id=category_id)
    SocialAp=Post.objects.filter(category=category_id)
    return render(request, 'SocialApp/category.html', {'category': category, 'SocialApps': SocialAp})