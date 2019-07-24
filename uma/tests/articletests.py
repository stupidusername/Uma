from ..models.article import Article, ArticleComponent
from ..models.articlecategory import ArticleCategory
from django.core.exceptions import ValidationError
from django.test import TestCase


class ArticleTests(TestCase):
    """
    Test for the article model.
    """

    def test_circular_component_validation(self):
        """
        An article that depends on itself should not be able to be created.
        """
        # Create an article category.
        category = ArticleCategory.objects.create(name='Category')
        # Create three articles.
        a1 = Article.objects.create(name='1', category=category, public=True)
        a2 = Article.objects.create(name='2', category=category, public=True)
        a3 = Article.objects.create(name='3', category=category, public=True)
        # a2 depends on a1.
        rel = ArticleComponent(parent=a2, child=a1, quantity=1)
        rel.full_clean()  # Use full_clean to test model validation.
        rel.save()
        # a3 depends on a2.
        rel = ArticleComponent(parent=a3, child=a2, quantity=1)
        rel.full_clean()
        rel.save()
        # a1 cannot dependant on a1.
        with self.assertRaises(ValidationError):
            rel = ArticleComponent(parent=a1, child=a1, quantity=1)
            rel.full_clean()
        # a1 cannot dependant on a3.
        with self.assertRaises(ValidationError):
            rel = ArticleComponent(parent=a1, child=a3, quantity=1)
            rel.full_clean()
