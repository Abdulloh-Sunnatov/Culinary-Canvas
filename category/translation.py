from modeltranslation import translator
from modeltranslation.translator import TranslationOptions
from .models import Category

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

