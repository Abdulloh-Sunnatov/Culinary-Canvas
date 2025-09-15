from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Recipe(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name=_("Author"),
    )
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, verbose_name=_("Slug")
    )
    description = models.TextField(max_length=500, verbose_name=_("Description"))
    ingredients = models.TextField(
        help_text=_("List ingredients with measurements, one per line"),
        verbose_name=_("Ingredients"),
    )
    image = models.ImageField(
        upload_to="recipe_images/", verbose_name=_("Recipe Image")
    )
    categories = models.ManyToManyField(
        "categories.Category",
        related_name="recipes",
        verbose_name=_("Categories"),
    )
    is_draft = models.BooleanField(default=True, verbose_name=_("Is Draft"))
    is_public = models.BooleanField(default=True, verbose_name=_("Is Public"))

    class Meta:
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")

    def __str__(self):
        return self.title


class Comment(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Author"),
    )
    recipe = models.ForeignKey(
        "recipes.Recipe",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Recipe"),
    )
    text = models.TextField(max_length=500, verbose_name=_("Comment Text"))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"{self.author.email} - {self.recipe.title}"


class Rating(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ratings",
        verbose_name=_("Author"),
    )
    recipe = models.ForeignKey(
        "recipes.Recipe",
        on_delete=models.CASCADE,
        related_name="ratings",
        verbose_name=_("Recipe"),
    )
    score = models.PositiveSmallIntegerField(verbose_name=_("Score"))

    class Meta:
        unique_together = ("author", "recipe")
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")

    def __str__(self):
        return f"{self.score} ★ by {self.author.email} for {self.recipe.title}"
