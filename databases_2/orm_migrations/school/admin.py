from django.contrib import admin

from .models import Student, Teacher


class StudentTeachers(admin.TabularInline):
    model = Student.teacher.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentTeachers]
    exclude = ('teacher', )
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [StudentTeachers]
    pass

