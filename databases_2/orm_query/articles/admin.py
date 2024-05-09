from django.contrib import admin

from .models import Article, Genre, Author, Scope

class ScopeDataAdmin(admin.TabularInline):
    model = Article.scopes.through
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeDataAdmin]
    exclude = ('scopes',)
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass