from .roomcategory import RoomCategory
from .stay import Stay
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from safedelete.models import SafeDeleteModel


class CategoryStay(SafeDeleteModel):
    """
    Many-to-many relationship between room categories and stays. A pair
    category-stay must be unique. Deleted category-stay relationships must be
    left out from this validation.
    """

    class Meta:
        # We need to add a new field to validate unique non-deleted
        # category-stay entries. The field `deleted` won't do it because it is
        # set to null for non-deleted models. For some DB systems like
        # PostgreSQL null values are different from each other. So a set of two
        # rows like (1, 1, NULL) that contains the value for 3 columns that are
        # supposed to be unique together will not raise an integrity error on
        # insert.
        unique_together = ['category', 'stay', 'deleted_not_null']

    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    stay = models.ForeignKey(Stay, on_delete=models.CASCADE)
    # We will use a field that can contain a timestamp built from the deleted
    # datetime. The value `0` represents a non-deleted model. By setting
    # `editable` to false we exclude the field from forms. But in doing so it
    # will be excluded from validations. We will need to take care of this
    # later.
    deleted_not_null = models.BigIntegerField(default=0, editable=False)

    def _get_unique_checks(self, exclude=None):
        """
        See parent doc.
        """
        # Remove the `deleted_not_null` field from the exclude list. This will
        # force the forms to take it into account when performing validations.
        if 'deleted_not_null' in exclude:
            exclude.remove('deleted_not_null')
        return super()._get_unique_checks(exclude)


# Register a signal handler triggered before an instance of the `CategoryStay`
# model gets saved. Be careful with the `pre_save` signal as it won't be
# triggered for batch operations.
@receiver(pre_save, sender=CategoryStay)
def set_delete_boolean(sender, instance, **kwargs):
    """
    Handler for the `pre_save` signal of the `CategoryStay` model. It
    automatically updates the `deleted_not_null` field.

    :param sender type: The model class.
    :param instance CategoryStay: The actual instance being saved.
    """
    if instance.deleted:
        instance.deleted_not_null = instance.deleted.timestamp()
    else:
        instance.deleted_not_null = 0
