from .models import Category, SubCategory, Product
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(SubCategory )
class ProductTranslationOptions(TranslationOptions):
    fields = ('sub_category_name',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name','description')