from django.contrib import admin
from .models import CourseCategory, Course, Registration

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'category', 'start_date', 'duration', 'fee', 'is_available')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Course, CourseAdmin)

class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'is_available')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CourseCategory, CourseCategoryAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'place', 'email', 'phone_number', 'course', 'submitted_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Registration, RegistrationAdmin)

