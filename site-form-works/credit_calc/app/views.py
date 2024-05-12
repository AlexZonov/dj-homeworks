from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    common_result = 0
    result = 0
    has_result = 0


    form = CalcForm(request.GET)
    if form.is_valid():
        fee = form.cleaned_data['initial_fee']
        percents = form.cleaned_data['rate'] / 100
        months = form.cleaned_data['months_count']
        common_result = fee + (fee * percents)
        result = common_result / months
        has_result = True

    context = {
        'form': form,
        'common_result': common_result,
        'result': result,
        'has_result': has_result
    }

    return render(request, template, context)
