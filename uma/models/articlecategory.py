from django.db import models
from safedelete.models import SafeDeleteModel


class ArticleCategory(SafeDeleteModel):
    """
    ArticleCategory model.
    """

    class Meta:
        verbose_name_plural = 'article categories'

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
