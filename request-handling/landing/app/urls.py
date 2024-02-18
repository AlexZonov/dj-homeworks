from django.urls import path

from app.views import random_landing, stats, index


urlpatterns = [
    path('', index, name='index'),
    path('landing/', random_landing, name='landing'),
    path('stats/', stats, name='stats'),
]
