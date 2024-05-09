from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all().select_related('genre', 'author').defer('author__phone').order_by(ordering)
    # .prefetch_related('scopes', 'scope_data')
    # .defer('author__phone')
    context = {
        'object_list' : articles
    }
    return render(request, template_name, context)
