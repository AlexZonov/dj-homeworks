import datetime

from django.urls import path, converters

import app.views

class DateForvardConverter:
    regex = "[0-9]{4}-[0-9]{2}-[0-9]{2}"

    def to_python(self, value: str):
        return datetime.datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value: datetime.datetime):
        return value.strftime('%Y-%m-%d')

class DateBackwardConverter:
    regex = "[0-9]{2}-[0-9]{2}-[0-9]{4}"

    def to_python(self, value: str):
        return datetime.datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value: datetime.datetime):
        return value.strftime('%d-%m-%Y')

converters.register_converter(DateForvardConverter, 'dateforward')
converters.register_converter(DateBackwardConverter, 'datebackward')

urlpatterns = [
    path('', app.views.file_list, name='file_list'),
    path('<dateforward:date>/', app.views.file_list, name='file_list'),
    path('<datebackward:date>/', app.views.file_list, name='file_list'),
    path('file/<name>/', app.views.file_content, name='file_content'),
]
