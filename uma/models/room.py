from django.db import models


class Room(models.Model):
    """
    Hotel room.
    """
    name = models.CharField(max_length=100, unique=True)
