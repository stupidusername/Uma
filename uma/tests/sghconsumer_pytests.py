"""
SGHConsumer tests.
"""

from channels.testing import WebsocketCommunicator
from project.routing import application
import pytest


@pytest.mark.asyncio
async def test_echo():
    """
    Simple echo test.
    """
    communicator = WebsocketCommunicator(application, 'ws/sgh/')
    connected, subprotocol = await communicator.connect()
    assert connected
    message = 'Hello, friend.'
    content = {
        'jsonrpc': '2.0',
        'method': 'Tests.Echo',
        'id': 1,
        'params': {'message': message}
    }
    await communicator.send_json_to(content)
    response = await communicator.receive_json_from()
    assert response['result'] == message
