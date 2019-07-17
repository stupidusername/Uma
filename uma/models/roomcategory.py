from django.db import models


class RoomCategory(models.Model):
    """
    Room category model.
    """
    name = models.CharField(max_length=100, unique=True)
