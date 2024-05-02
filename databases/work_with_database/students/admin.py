from django.contrib import admin
from students.models import Student, Course

class InlineCourses(admin.TabularInline):
    model = Course.students.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [InlineCourses]
    exclude = ('courses', )
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [InlineCourses]
    pass

# Register your models here.
