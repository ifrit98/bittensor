import pytest
from unittest.mock import AsyncMock
from starlette.responses import Response

from bittensor import BTStreamingResponseModel, StreamingSynapse


# Test case for BTStreamingResponseModel
def test_bt_streaming_response_model():
    async def sample_token_streamer(send):
        await send(b"data")

    model = BTStreamingResponseModel(token_streamer=sample_token_streamer)
    assert model.token_streamer == sample_token_streamer


# Mock StreamingSynapse to test abstract methods
class TestStreamingSynapse(StreamingSynapse):
    async def process_streaming_response(self, response: Response):
        pass

    def extract_response_json(self, response: Response) -> dict:
        return {}
