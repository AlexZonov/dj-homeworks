from django.db import models


class Genre(models.Model):

    name = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=256, verbose_name='Имя')
    phone = models.CharField(max_length=256, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Scope(models.Model):
    topic = models.CharField(max_length=50, verbose_name='Раздел')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Scope, through='ScopeData', verbose_name='Теги')

    @property
    def tags(self): return self.scope_data.select_related('scope').order_by('-is_main')
    # def tags(self): return self.scope_data

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class ScopeData(models.Model):
    scope = models.ForeignKey(Scope, related_name='scope_data', verbose_name='Теги', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='scope_data', verbose_name='Новость', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Разделы'
        verbose_name_plural = 'Разделы'

    @property
    def topic(self): return self.scope.topic