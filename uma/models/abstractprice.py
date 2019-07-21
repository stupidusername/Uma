from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from safedelete.models import SafeDeleteModel


class AbstractPrice(SafeDeleteModel):
    """
    An abstract class that represents a price that was created at a given
    datetime.
    """

    class Meta:
        abstract = True

    price = MoneyField(
        decimal_places=2,
        max_digits=10,
        validators=[MinMoneyValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
