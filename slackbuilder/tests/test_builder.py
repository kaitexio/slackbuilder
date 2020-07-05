from unittest import TestCase
from unittest.mock import MagicMock

from slackbuilder.builder import BlockBuilder


class TestBuilder(TestCase):
    test_str = "hello world"
    test_channel = "testa"

    def test_add_block(self):
        builder = BlockBuilder(self.test_channel)
        block = MagicMock(generate=lambda: self.test_str)
        builder.add_block(block)
        self.assertEquals(block, list(builder.blocks)[0])

    def test_create_post(self):
        builder = BlockBuilder(self.test_channel)
        block = MagicMock(generate=lambda: self.test_str)
        builder.add_block(block)
        post = builder.create_post()
        self.assertEquals(
            post,
            {
                "channel": self.test_channel,
                "blocks": [self.test_str],
                "attachments": [],
            },
        )
