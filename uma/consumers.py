from channels.generic.websocket import JsonWebsocketConsumer


class SGHConsumer(JsonWebsocketConsumer):
    """
    Django Channels consumer that handles communications from/to the SGH
    server.
    """

    def receive_json(self, content):
        """
        Echoes a message.

        :param object content: An object decoded from JSON.
        """
        self.send_json(content)
