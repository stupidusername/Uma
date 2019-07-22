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


class NonEditablePriceMixin(models.Model):
    """
    Use this mixin if you want to make a price model non-editable. This means
    that if its price gets changed it will be saved as a new record instead of
    updating the old one.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        See parent doc.
        """
        # Check if the PK was set to determine whether this in an update.
        if self.pk:
            # Get old record from the DB.
            old_model = self.__class__._default_manager.get(pk=self.pk)
            # Unset the PK if the price is not the same.
            # This will force a new model creation.
            if self.price != old_model.price:
                self.pk = None
        super().save(*args, **kwargs)
