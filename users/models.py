from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(verbose_name=_("Email"), max_length=255, unique=True)
    password = models.CharField(max_length=64, verbose_name=_("Password"))
    first_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Last Name")
    )
    profile_picture = models.ImageField(
        upload_to="profile_picture/",
        null=True,
        blank=True,
        verbose_name=_("Profile Picture"),
    )
    is_chef = models.BooleanField(default=False, verbose_name=_("Is Chef"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    is_confirmed = models.BooleanField(default=False, verbose_name=_("Is Confirmed"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Is Staff"))
    is_superuser = models.BooleanField(default=False, verbose_name=_("Is Superuser"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
