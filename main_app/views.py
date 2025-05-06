from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import CourseCategory, Course, Registration
from django.conf import settings
from django.contrib import messages

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

def registration(request):
    categories = CourseCategory.objects.filter(is_available=True)

    if request.method == 'POST':
        data = request.POST
        try:
            registration = Registration.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                birth_date=data.get('birth_date'),
                email=data.get('email'),
                phone_number=data.get('phone_number'),
                whatsapp_number=data.get('whatsapp_number'),
                gender=data.get('gender'),
                house_name=data.get('house_name'),
                place=data.get('place'),
                post_office=data.get('post_office'),
                district=data.get('district'),
                state=data.get('state'),
                pin_code=data.get('pin_code'),
                course_category_id=data.get('course_category'),
                course_id=data.get('course')
            )

            # Email sending
            send_mail(
                subject='New Course Registration',
                message=f'{registration.first_name} has registered for {registration.course.course_name}.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['shareefta@gmail.com']
            )

            send_mail(
                subject='Registration Confirmation',
                message=f'Thank you {registration.first_name} for registering in {registration.course.course_name}.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[registration.email]
            )

            messages.success(request, "Registration successful! Confirmation email sent.")
            return redirect('registration_success')

        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")

    return render(request, 'registration_form.html', {'categories': categories})

def load_courses(request):
    category_id = request.GET.get('category_id')
    courses = Course.objects.filter(category_id=category_id, is_available=True).values('id', 'course_name')
    return JsonResponse(list(courses), safe=False)

def registration_success(request):
    return render(request, 'registration_success.html')
