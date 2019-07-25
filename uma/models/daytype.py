from django.db import models
from safedelete.models import SafeDeleteModel


class DayType(SafeDeleteModel):
    """
    Day type model. A day type can be a day of the week like Monday, Tuesday,
    etc. or a special one like "Special Day 1".
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
