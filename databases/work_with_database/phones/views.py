from django.shortcuts import render

from phones.models import Phone

SORTS = {
    '-price': 'Greater price',
    'price': 'Lower price',
    '-release_date': 'Release date',
}

def validate_sort(value):
    if value == '' or value not in SORTS:
        return next(iter(SORTS))
    return value

def show_catalog(request):
    template = 'catalog.html'

    sort_current = validate_sort(request.GET.get('order_by'))
    sort = {
        'data': SORTS,
        'current': sort_current,
    }

    phones = Phone.objects.all().order_by(sort_current)
    context = {'phones': phones, 'sort': sort}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    context = {'phone': phone}
    return render(request, template, context)
