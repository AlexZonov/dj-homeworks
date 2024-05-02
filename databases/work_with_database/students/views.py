from django.shortcuts import render

from students.models import Course


# Create your views here.
def list_curses(request):
    template_name = 'students/list.html'
    cources = Course.objects.prefetch_related('students').all()
    context = {'cources' : cources}
    return render(request, template_name, context)
