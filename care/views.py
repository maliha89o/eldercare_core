from django.shortcuts import render
from .models import CareService

def home(request):
    services_from_db = CareService.objects.all()
    context = {
        'app_name': 'ElderCare Link',
        'services': services_from_db,
        'monthly_goal': 50000.00,
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'description': 'A dedicated platform for managing healthcare and services for the elderly.'
    }
    return render(request, 'about.html', context)