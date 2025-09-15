from rest_framework import serializers

from .models import Comment, Rating, Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            "id",
            "author",
            "title",
            "slug",
            "description",
            "ingredients",
            "image",
            "categories",
            "is_draft",
            "is_public",
            "created_at",
            "updated_at",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "recipe",
            "text",
            "created_at",
            "updated_at",
        ]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            "id",
            "author",
            "recipe",
            "value",
            "created_at",
            "updated_at",
        ]
