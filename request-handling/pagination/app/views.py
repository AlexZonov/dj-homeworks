import urllib
from csv import DictReader
from urllib.parse import urljoin

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

Pages = None


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request: WSGIRequest):
    current_page = int(request.GET.get('page', 1))
    page = get_page(current_page)
    prev_page_url = create_page_url(bus_stations, page.has_previous(), page.previous_page_number)
    next_page_url = create_page_url(bus_stations, page.has_next(), page.next_page_number)

    return render(request, 'index.html', context={
        'bus_stations': page.object_list,
        'current_page': page.number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })


def create_page_url(view_name: str, has_page: bool, page_num_func):
    if has_page:
        url = reverse(view_name)
        params = urllib.parse.urlencode({'page': page_num_func()})
        return f'{url}?{params}'
    else:
        return None


def get_page(num: int):
    global Pages
    if Pages is not None:
        return Pages.get_page(num)

    with open("data-398-2018-08-30.csv", "r", encoding="cp1251") as data_file:
        data = list(DictReader(data_file, ['Name', 'Street', 'District']))

    Pages = Paginator(data, 10)
    return Pages.get_page(num)