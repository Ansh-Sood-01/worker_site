from django.contrib import admin
from .models import Category, Image

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "image_file")
    search_fields = ("title", "category__name")
    list_filter = ("category",)
