from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
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
    components = models.ManyToManyField(
        'self',
        through='ArticleComponent',
        through_fields=['parent', 'child'],
        symmetrical=False
    )
    public = models.BooleanField()
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to='articles')

    def __str__(self):
        return self.name


class ArticleComponent(models.Model):
    """
    An intermediary model that represents a relationship between two articles.
    The first one would be the parent and the second one its child. The
    parent article its a combination of its children. A parent-child
    combination must be unique. The field `quantity` reprensents how many
    articles of a child class are needed by a parent.
    """

    class Meta:
        unique_together = ['parent', 'child']

    parent = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='child_article_components'
    )
    child = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='parent_article_components'
    )
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def clean(self):
        """
        See parent doc. Validates that an articles is not dependant on itself.

        :raises ValidationError:
        """
        def check_parent_in_children(children):
            if self.parent in children:
                raise ValidationError(
                    'An article cannot be a component of itself.'
                )
            else:
                for child in children:
                    check_parent_in_children(child.components.all())

        try:
            check_parent_in_children([self.child])
        except ArticleComponent.child.RelatedObjectDoesNotExist:
            # The child component is not set. Do nothing.
            pass
