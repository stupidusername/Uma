from .abstractprice import AbstractPrice, NonEditablePriceMixin
from .roomcategory import RoomCategory
from .stay import Stay
from django.db import models


class StayRate(AbstractPrice):
    """
    Stay rate model. This model is used to keep a record of the prices at a
    given point in time. A stay rate is established for one room category.
    """

    category = models.ForeignKey(
        RoomCategory,
        related_name='rates',
        on_delete=models.CASCADE
    )
    stay = models.ForeignKey(
        Stay,
        related_name='rates',
        on_delete=models.CASCADE
    )


class NonEditableStayRate(NonEditablePriceMixin, StayRate):
    """
    A proxy model that makes its record non-editable. For more information read
    the documentation of the used mixin: `NonEditablePriceMixin`.
    """

    class Meta:
        proxy = True
