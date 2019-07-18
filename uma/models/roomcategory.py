from django.db import models
from safedelete.models import SafeDeleteModel


class RoomCategory(SafeDeleteModel):
    """
    Room category model.
    """

    class Meta:
        verbose_name_plural = 'room categories'

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
