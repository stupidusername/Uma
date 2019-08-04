from django.db import models
from safedelete.models import SafeDeleteModel


class Stay(SafeDeleteModel):
    """
    Stay model. It represents a customer-staying mode, like 3 hours long or
    overnight.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
