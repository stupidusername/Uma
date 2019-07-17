from django.db import models
from safedelete.models import SafeDeleteModel


class RoomCategory(SafeDeleteModel):
    """
    Room category model.
    """

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'room categories'

    def __str__(self):
        return self.name
