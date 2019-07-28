from ..models.categorystay import CategoryStay
from ..models.roomcategory import RoomCategory
from ..models.stay import Stay
from django.test import TestCase


class RoomCategoryTests(TestCase):
    """
    Tests for the room category model.
    """

    def test_unique_category_stay_relationships(self):
        """
        A pair category-stay must be unique but deleted category-stay
        relationships must be left out from this validation.
        """
        # Create room category and stay models.
        category = RoomCategory.objects.create(name='Category')
        stay_1 = Stay.objects.create(name='Stay 1')
        stay_2 = Stay.objects.create(name='Stay 2')

        # Add stays to the category.
        category.stays.add(stay_1)
        category.stays.add(stay_2)
        self.assertEqual(CategoryStay.objects.count(), 2)

        # Duplicating an stay should not be possible.
        stay_1_duplicated = Stay.objects.get(pk=stay_1.pk)
        category.stays.add(stay_1_duplicated)
        # There should only be two rows.
        self.assertEqual(CategoryStay.objects.count(), 2)

        # Deleting an stay should mark it as deleted but the row should not be
        # deleted from the DB.
        category.stays.remove(stay_2)
        self.assertEqual(CategoryStay.objects.count(), 1)
        self.assertEqual(CategoryStay.all_objects.count(), 2)

        # Re-adding the deleted say should work, but lefting the deleted record
        # untouched.
        category.stays.add(stay_2)
        self.assertEqual(CategoryStay.objects.count(), 2)
        self.assertEqual(CategoryStay.all_objects.count(), 3)
