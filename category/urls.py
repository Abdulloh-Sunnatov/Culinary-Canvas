# category/urls.py
from django.urls import path

from category.views import (
    CategoryCreateAPIView,
    CategoryDeleteAPIView,
    CategoryDetailAPIView,
    CategoryListAPIView,
    CategoryUpdateAPIView,
)

urlpatterns = [
    path("", CategoryListAPIView.as_view(), name="category-list"),
    path("create/", CategoryCreateAPIView.as_view(), name="category-create"),
    path("<int:id>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("<int:id>/update/", CategoryUpdateAPIView.as_view(), name="category-update"),
    path("<int:id>/delete/", CategoryDeleteAPIView.as_view(), name="category-delete"),
]
