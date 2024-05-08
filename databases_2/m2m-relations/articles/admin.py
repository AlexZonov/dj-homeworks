from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        mainTagsCount = sum(1 for form in self.forms if 'is_main' in form.cleaned_data and form.cleaned_data['is_main'])
        if mainTagsCount > 1:
            raise ValidationError('Основным тегом может быть только 1 тег')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopes(admin.TabularInline):
    model = Article.scopes.through
    verbose_name = "Тематики статьи"
    verbose_name_plural = "Тематики статьи"
    formset = RelationshipInlineFormset
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_scopes']
    inlines = [ArticleScopes]
    exclude = ('scopes', )
    pass

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['topic']