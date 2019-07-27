from django.forms.widgets import Select


class SelectRoomMode(Select):
    """
    A select field for the room modes. It also displays the room mode
    description when an option is selected.
    """
