from unittest import TestCase

from slackbuilder.blocks import TextBlock, DEFAULT_TEXT_TYPE


class TestTextBlock(TestCase):
    def test_generate(self):
        test_text = "hello world"
        block = TextBlock(test_text).generate()
        self.assertEquals(
            block,
            {"type": "section", "text": {"type": DEFAULT_TEXT_TYPE, "text": test_text}},
        )
