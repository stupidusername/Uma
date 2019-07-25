from .daytype import DayType
from django.db import models
from django.utils import formats
from safedelete.models import SafeDeleteModel


class Holiday(SafeDeleteModel):
    """
    Holiday model.
    """

    date = models.DateField(unique=True)
    day_type = models.ForeignKey(DayType, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return formats.date_format(self.date)
