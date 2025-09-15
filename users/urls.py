from django.urls import path

from users.views.register import (
    EmailConfirmAPIView,
    UserRegisterAPIView,
)
from users.views.user import UserLogoutAPIView, UserProfileAPIView, UserUpdateAPIView
from views.view import index_view

urlpatterns = [
    path("", index_view, name="index"),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path("profile/update/", UserUpdateAPIView.as_view(), name="profile-update"),
    path("register/", UserRegisterAPIView.as_view(), name="register"),
    path("login/", UserLogoutAPIView.as_view(), name="loginout"),
    path(
        "register/confirm/<str:token>/",
        EmailConfirmAPIView.as_view(),
        name="register-confirm",
    ),
]
