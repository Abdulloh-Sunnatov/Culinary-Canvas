from django.contrib import admin
from .models import Recipe, Comment, Rating
from modeltranslation.admin import TranslationAdmin


@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    list_display = ("title", "author", "is_public", "is_draft", "created_at")
    list_filter = ("is_public", "is_draft", "categories", "created_at")
    search_fields = ("title", "description", "ingredients", "author__email")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "created_at"
    filter_horizontal = ("categories",)


@admin.register(Comment)
class CommentAdmin(TranslationAdmin):
    list_display = ("author", "recipe", "text", "created_at")
    search_fields = ("author__email", "recipe__title", "text")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"


@admin.register(Rating)
class RatingAdmin(TranslationAdmin):
    list_display = ("author", "recipe", "score", "created_at")
    search_fields = ("author__email", "recipe__title")
    list_filter = ("score", "created_at")
    date_hierarchy = "created_at"
