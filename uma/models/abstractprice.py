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
    that if its any field of the model gets changed it will be saved as a new
    record instead of updating the old one.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        See parent doc.
        """
        # If the model was changed, set its PK to None to force an insert.
        if self.has_changed():
            self.pk = None
        super().save(*args, **kwargs)

    def has_changed(self) -> bool:
        """
        Check if a any field of the model was changed but not saved.

        :returns bool: `False` if the models is new or no fields were changed
                       since the last save. `True` otherwise.
        """
        has_changed = False
        # If the model does not have a PK then it is a new one.
        if self.pk:
            # Get old record from the DB.
            old_model = self.__class__._default_manager.get(pk=self.pk)
            # Check if any field was changed.
            for f in self.__class__._meta.fields:
                # Leave the PK out of this.
                if not f.primary_key:
                    if getattr(self, f.name) != getattr(old_model, f.name):
                        has_changed = True
                        break
        return has_changed
