from .roomcategory import RoomCategory
from .roommode import RoomMode
from django.db import models
from safedelete.models import SafeDeleteModel


class Room(SafeDeleteModel):
    """
    Room model.
    """

    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        RoomCategory,
        related_name='rooms',
        on_delete=models.CASCADE,
        null=True
    )
    mode = models.ForeignKey(
        RoomMode,
        related_name='rooms',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name
