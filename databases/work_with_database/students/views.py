from django.shortcuts import render

from students.models import Course
from django.core.cache import cache


# Create your views here.
def list_curses(request):
    template_name = 'students/list.html'
    cache_key = 'students-list-courses'
    cache_courses = cache.get(cache_key)
    if not cache_courses:
        cources = Course.objects.prefetch_related('students').all()
        cache.set(cache_key, cources, timeout=5)
    else:
        cources = cache_courses
    context = {'cources' : cources}
    return render(request, template_name, context)
