from django.contrib import admin
from .models import Category
from modeltranslation.admin import TranslationAdmin

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
