from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "image_file")
    search_fields = ("title", "category__name")
    list_filter = ("category",)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'category__name', 'description')