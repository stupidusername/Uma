from channels.generic.websocket import WebsocketConsumer
from jsonrpc import JSONRPCResponseManager, dispatcher
import logging
import threading


class SGHConsumer(WebsocketConsumer):
    """
    Django Channels consumer that handles communications from/to the SGH
    server. It implements the JSON-RPC protocol.
    """

    _last_consumer = None  # Instance of the most recent consumer.
    _last_consumer_lock = threading.Lock()

    _logger = logging.getLogger('uma.consumers.SGHConsumer')

    def accept(self, subprotocol=None):
        """
        Accepts an incoming socket. If there was a previous instance, try to
        disconnect it first. We don't want two SGH connections active at the
        same time.

        :param [None, str] subprotocol: Connection subprotocol (optional).
        """
        # Close last consumer (if any).
        with SGHConsumer._last_consumer_lock:
            if SGHConsumer._last_consumer:
                try:
                    # The last connected consumer may be inactive. Calling
                    # close() on it can cause an exception.
                    SGHConsumer._last_consumer.close()
                    SGHConsumer._logger.info(
                        "Previous connection from"
                        f" {SGHConsumer._last_consumer.scope['client'][0]}"
                        " closed."
                    )
                finally:
                    SGHConsumer._last_consumer = None
        # Accept new consumer.
        super().accept(subprotocol)
        SGHConsumer._last_consumer = self
        SGHConsumer._logger.info(
            f"Connection from {self.scope['client'][0]} accepted."
        )

    def receive(self, text_data=None, bytes_data=None):
        """
        Called with either text_data or bytes_data for each frame. See parent
        doc.

        :param str text_data:
        :param bytes_data bytes:
        """
        # We only care about text data.
        SGHConsumer._logger.debug(f'Received text data: {text_data}')
        # Dispatch the JSON-RPC method and get the response.
        response = JSONRPCResponseManager.handle(text_data, dispatcher)
        # Send the response to the client.
        self.send(text_data=response.json)

    def send(self, text_data=None, bytes_data=None, close=False):
        """
        See parent doc.
        """
        # Only text data should be sent through this socket.
        SGHConsumer._logger.debug(f'Sending text data: {text_data}')
        super().send(text_data, bytes_data, close)

    @dispatcher.add_method(name='Tests.Echo')
    def echo(message):
        """
        Echoes any message.
        """
        return message
