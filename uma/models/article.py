from django.db import models
from .articlecategory import ArticleCategory
from safedelete.models import SafeDeleteModel


class Article(SafeDeleteModel):
    """
    Article model.
    """

    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        ArticleCategory,
        related_name='articles',
        on_delete=models.CASCADE
    )
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to='articles')

    def __str__(self):
        return self.name
