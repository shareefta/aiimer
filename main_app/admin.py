from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'start_date', 'duration', 'fee')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Course, CourseAdmin)

