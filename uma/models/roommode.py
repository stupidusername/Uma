from django.db import models
from safedelete.models import SafeDeleteModel


class RoomMode(SafeDeleteModel):
    """
    Room mode model. A room mode determines the customer-staying schema of a
    room.
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
