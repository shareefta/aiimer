from django.db import models

class CourseCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    course_name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    start_date = models.DateField()
    duration = models.CharField(max_length=100)
    fee = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

class Registration(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    house_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post_office = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    course_category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
