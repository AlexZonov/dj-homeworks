import csv

from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'

    context = {
        'data': get_inflation_data()
    }

    return render(request, template_name, context)


def get_inflation_data():
    with open('inflation_russia.csv', 'r', encoding='utf-8') as file:
        return list(csv.reader(file, delimiter=';'))
