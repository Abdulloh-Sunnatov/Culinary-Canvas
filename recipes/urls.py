from django.urls import path

from .views import (
    CommentDeleteAPIView,
    CommentDetailAPIView,
    CommentListCreateAPIView,
    CommentUpdateAPIView,
    RatingDetailAPIView,
    RatingListCreateAPIView,
    RecipeDeleteAPIView,
    RecipeDetailAPIView,
    RecipeListCreateAPIView,
    RecipeUpdateAPIView,
)

urlpatterns = [
    # Recipe
    path("recipes/", RecipeListCreateAPIView.as_view(), name="recipe-list-create"),
    path("recipes/<int:id>/", RecipeDetailAPIView.as_view(), name="recipe-detail"),
    path(
        "recipes/<int:id>/update/", RecipeUpdateAPIView.as_view(), name="recipe-update"
    ),
    path(
        "recipes/<int:id>/delete/", RecipeDeleteAPIView.as_view(), name="recipe-delete"
    ),
    # Comment
    path("comments/", CommentListCreateAPIView.as_view(), name="comment-list-create"),
    path("comments/<int:id>/", CommentDetailAPIView.as_view(), name="comment-detail"),
    path(
        "comments/<int:id>/update/",
        CommentUpdateAPIView.as_view(),
        name="comment-update",
    ),
    path(
        "comments/<int:id>/delete/",
        CommentDeleteAPIView.as_view(),
        name="comment-delete",
    ),
    # Rating
    path("ratings/", RatingListCreateAPIView.as_view(), name="rating-list-create"),
    path("ratings/<int:id>/", RatingDetailAPIView.as_view(), name="rating-detail"),
]
