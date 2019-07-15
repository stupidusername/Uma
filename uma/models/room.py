from .room_category import RoomCategory
from django.db import models


class Room(models.Model):
    """
    Room model.
    """
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        RoomCategory,
        related_name='rooms',
        on_delete=models.PROTECT
    )
