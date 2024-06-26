import django.urls
from django.shortcuts import render


def home_view(request):
    template_name = 'app/home.html'
    return render(request, template_name, context={'page': 'home'})


def about_view(request):
    template_name = 'app/about.html'
    return render(request, template_name, context={'page': 'about'})


def contacts_view(request):
    template_name = 'app/contacts.html'
    return render(request, template_name, context={'page': 'contacts'})


def examples_view(request):
    template_name = 'app/examples.html'

    items = [{
        'title': 'Apple II',
        'text': 'Легенда',
        'img': 'ii.jpg'
    }, {
        'title': 'Macintosh',
        'text': 'Свежие новинки октября 1983-го',
        'img': 'mac.jpg'
    }, {
        'title': 'iMac',
        'text': 'Оригинальный и прозрачный',
        'img': 'imac.jpg'
    }]
    context = {
        'items': items,
        'page': 'examples'
    }
    return render(request, template_name,
                  context)
