from django.shortcuts import render
from .models import Course

def home(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def teachers(request):
    return render(request, 'team.html')

def register(request):
    return render(request, 'registration_form.html')