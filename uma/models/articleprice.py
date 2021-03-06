from .abstractprice import AbstractPrice, NonEditablePriceMixin
from .article import Article
from django.db import models


class ArticlePrice(AbstractPrice):
    """
    Article price model. This is used to keep a record of the prices at a given
    point in time.
    """

    article = models.ForeignKey(
        Article,
        related_name='prices',
        on_delete=models.CASCADE
    )


class NonEditableArticlePrice(NonEditablePriceMixin, ArticlePrice):
    """
    A proxy model that makes its record non-editable. For more information read
    the documentation of the used mixin: `NonEditablePriceMixin`.
    """

    class Meta:
        proxy = True
