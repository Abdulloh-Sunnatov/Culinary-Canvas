from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Recipe, Comment, Rating

@admin.register(Recipe)
class RecipeTranslationAdmin(TranslationAdmin):
    list_display = ["id", "title", "author", "is_public", "is_draft", "created_at"]
    list_display_links = ["id", "title"]
    search_fields = ["title", "author__email"]
    list_filter = ["is_public", "is_draft", "created_at"]
    date_hierarchy = "created_at"

@admin.register(Comment)
class CommentTranslationAdmin(TranslationAdmin):
    list_display = ["id", "recipe", "author", "created_at"]
    list_display_links = ["id", "recipe"]
    search_fields = ["recipe__title", "author__email", "content"]
    list_filter = ["created_at"]
    date_hierarchy = "created_at"


@admin.register(Rating)
class RatingTranslationAdmin(TranslationAdmin):
    list_display = ["id", "recipe", "author", "score", "created_at"]
    list_display_links = ["id", "recipe"]
    search_fields = ["recipe__title", "author__email"]
    list_filter = ["score", "created_at"]
    date_hierarchy = "created_at"
