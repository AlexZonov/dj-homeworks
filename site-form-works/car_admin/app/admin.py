from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'review_count']
    list_display_links = ['id', 'brand', 'model', 'review_count']
    search_fields = ('brand', 'model',)
    list_filter = ('brand', 'model',)
    verbose_name = "Машины"
    verbose_name_plural = "Машины"

    def get_ordering(self, request):
        return ('-id',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'car', 'title']
    list_display_links = ['id', 'car', 'title']
    search_fields = ('car', 'title',)
    list_filter = ('car', 'title',)
    form = ReviewAdminForm
    verbose_name = "Обзоры"
    verbose_name_plural = "Обзоры"

    def get_ordering(self, request):
        return ('-id',)
