from django.db import models
from django.utils import formats
from safedelete.models import SafeDeleteModel


class Holiday(SafeDeleteModel):
    """
    Holiday model.
    """

    date = models.DateField(unique=True)

    def __str__(self):
        return formats.date_format(self.date)
