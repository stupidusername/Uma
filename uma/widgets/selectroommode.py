from ..models.roommode import RoomMode
from django.forms.widgets import Select


class SelectRoomMode(Select):
    """
    A select field for the room modes. It also displays the room mode
    description when an option is selected.
    """

    template_name = 'widgets/select_room_mode.html'

    def get_context(self, name, value, attrs):
        """
        Add the room mode models to the context.

        :returns dict:
        """
        context = super().get_context(name, value, attrs)
        context['room_modes'] = RoomMode.objects.all()
        return context
