from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    start_date = models.DateField()
    duration = models.CharField(max_length=100)
    fee = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name
