from . import consumers
from django.conf.urls import url

websocket_urlpatterns = [
    url('ws/sgh/', consumers.SGHConsumer)
]
