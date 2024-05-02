from django.db import models
from django.db.models import JSONField

NAME_LEN = 64

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=NAME_LEN)
    description = models.TextField()
    tag = JSONField(default=list)

    def __str__(self):
        return f'{self.name}'

class Student(models.Model):
    name = models.CharField(max_length=NAME_LEN)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        courses_str = [str(c.name) for c in self.courses.all()]
        return f'{self.name}, courses: {','.join(courses_str)}'