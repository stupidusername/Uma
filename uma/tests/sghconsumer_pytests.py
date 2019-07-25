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
    content = {'payload': 'test'}
    await communicator.send_json_to(content)
    response = await communicator.receive_json_from()
    assert response == content
