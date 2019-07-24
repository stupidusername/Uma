"""
Register models for the admin panel.
"""
from .models.article import Article, ArticleComponent
from .models.articlecategory import ArticleCategory
from .models.articleprice import NonEditableArticlePrice
from .models.holiday import Holiday
from .models.room import Room
from .models.roomcategory import RoomCategory
from django.contrib import admin
from django.forms import BaseInlineFormSet


class LastModelFormset(BaseInlineFormSet):
    """
    Inline formset that limits the query result to the last created model.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _kwargs = {self.fk.name: kwargs['instance']}
        self.queryset = \
            kwargs['queryset'].filter(**_kwargs).order_by('-id')[:1]


class AbstractPriceInline(admin.StackedInline):
    """
    Inline representation of a price. This model is not meant to be used
    directly because it is abstract. You should subclass it and define a
    `model` attribute.
    """
    max_num = min_num = 1  # Only display one inline form for new models.
    can_delete = False  # Existing models cannot be deleted.
    formset = LastModelFormset  # Only display the current price model.


class ArticlePriceInline(AbstractPriceInline):
    """
    Inline representation of an article price.
    """
    # Use NonEditableArticlePrice to keep record of the price changes.
    model = NonEditableArticlePrice


class ArticleComponentInline(admin.StackedInline):
    """
    Inline representation of an article component.
    """
    model = ArticleComponent
    fk_name = 'parent'
    extra = 0  # Don't show components forms by default.


class ArticleAdmin(admin.ModelAdmin):
    """
    Representation of an article in the admin interface.
    """
    inlines = [ArticlePriceInline, ArticleComponentInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
admin.site.register(Holiday)
admin.site.register(Room)
admin.site.register(RoomCategory)
