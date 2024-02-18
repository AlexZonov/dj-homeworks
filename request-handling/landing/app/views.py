import random
from collections import Counter

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request: WSGIRequest):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    fromSource = request.GET.get("from-landing")
    if fromSource != None:
        counter_click[fromSource] += 1
    return render(request, 'index.html')


def random_landing(request: WSGIRequest):
    if random.randrange(1, 100) <= 50:
        return landing_test(request)
    else:
        return landing_original(request)

def landing_original(request: WSGIRequest):
    counter_show['original'] += 1
    templateName = 'landing.html'
    return render(request, templateName)

def landing_test(request: WSGIRequest):
    counter_show['test'] += 1
    templateName = 'landing_alternate.html'
    return render(request, templateName)


def stats(request: WSGIRequest):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(request, 'stats.html', context={
        'test_conversion': getRelationship('test'),
        'original_conversion': getRelationship('original'),
    })

def getRelationship(name: str):
    click = counter_click[name]
    show = counter_show[name]
    return click / show if show != 0 else 0