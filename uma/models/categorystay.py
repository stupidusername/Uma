from .roomcategory import RoomCategory
from .stay import Stay
from django.core.exceptions import ValidationError
from django.db import models
from safedelete.models import SafeDeleteModel


class CategoryStay(SafeDeleteModel):
    """
    Many-to-many relationship between room categories and stays. A pair
    category-stay must be unique. Deleted category-stay relationships must be
    left out from this validation.
    """

    unique_together = ['category', 'stay']

    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    stay = models.ForeignKey(Stay, on_delete=models.CASCADE)

    def clean(self):
        """
        See parent doc. Validates that a pair category-stat is unique without
        taking into account record that were marked as deleted.

        :raises ValidationError:
        """
        duplicated = self.__class__.objects.\
            filter(category=self.category, stay=self.stay).exists()
        if duplicated:
            raise ValidationError('This record already exists.')
