from django.shortcuts import render
from ServiceBookApp.models import Service

# Create your views here.
def service(request):
    service = Service.objects.all()
    return render(request, 'Service/service.html', {'services': service})