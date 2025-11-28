from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'BookShopApp/home.html')

def store(request):
    return render(request, 'BookShopApp/store.html')

def profile(request):
    return render(request, 'BookShopApp/profile.html')
