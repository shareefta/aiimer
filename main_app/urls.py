from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('teachers/', views.teachers, name='teachers'),
    path('register/', views.register, name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
