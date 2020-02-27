from channels.generic.websocket import WebsocketConsumer
from jsonrpc import JSONRPCResponseManager, dispatcher
import logging


class SGHConsumer(WebsocketConsumer):
    """
    Django Channels consumer that handles communications from/to the SGH
    server. It implements the JSON-RPC protocol.
    """

    _logger = logging.getLogger('uma.consumers.SGHConsumer')

    def accept(self, subprotocol=None):
        """
        Accepts an incoming socket.

        :param [None, str] subprotocol: Connection subprotocol (optional).
        """
        super().accept(subprotocol)
        self._logger.info(
            f"Accepted connection from {self.scope['client'][0]}."
        )

    def receive(self, text_data=None, bytes_data=None):
        """
        Called with either text_data or bytes_data for each frame. See parent
        doc.

        :param str text_data:
        :param bytes_data bytes:
        """
        # Dispatch the JSON-RPC method and get the response.
        response = JSONRPCResponseManager.handle(text_data, dispatcher)
        # Send the response to the client.
        self.send(text_data=response.json)

    @dispatcher.add_method(name='Tests.Echo')
    def echo(message):
        """
        Echoes any message.
        """
        return message
