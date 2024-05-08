import functools
import time

from django.db import connection, reset_queries
from django.db import models


class Scope(models.Model):
    topic = models.CharField(verbose_name='Раздел', max_length=50)

    def __str__(self):
        return self.topic


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scopes = models.ManyToManyField(Scope, through='ScopeThrough', through_fields=('article', 'scope'),
                                    related_name='articles')
    author = models.CharField(max_length=50, verbose_name='Автор', default='Зонов А.В.')

    @property
    def tags(self): return self.scopes_data.select_related('scope').all().order_by('-is_main')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_scopes(self):
        return "|".join([scope.topic for scope in self.scopes.all()])


class ScopeThrough(models.Model):
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='scopes_data', verbose_name='Раздел')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes_data')
    is_main = models.BooleanField(verbose_name='Основной')

    @property
    def topic(self): return self.scope.topic


def query_debugger(echo=False):
    def decorator(func):
        @functools.wraps(func)
        def inner_func(*args, **kwargs):
            reset_queries()

            start_queries = len(connection.queries)

            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()

            end_queries = len(connection.queries)
            out_func = print if echo else logging.error
            out_func(f"Function : {func.__name__}")
            out_func(f"Number of Queries : {end_queries - start_queries}")
            out_func(f"Finished in : {(end - start):.2f}s")
            return result

        return inner_func

    return decorator
