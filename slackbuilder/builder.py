class BlockBuilder:
    def __init__(self, channel=None):
        self._channel = channel
        self._blocks = []
        self._attachments = []

    @property
    def blocks(self):
        for block in self._blocks:
            yield block

    @property
    def attachments(self):
        for attachment in self._attachments:
            yield attachment

    def add_block(self, block):
        if not hasattr(block, "generate"):
            raise Exception(f"Type {type(block)} is not a valid block.")
        self._blocks.append(block)

    def add_attachment(self, attachment):
        if not hasattr(attachment, "generate"):
            raise Exception(f"Type {type(attachment)} is not a valid block.")
        self._attachments.append(attachment)

    def create_post(self):
        post = {}
        if self._channel:
            post["channel"] = self._channel
        post["blocks"] = [block.generate() for block in self._blocks]
        post["attachments"] = [
            attachment.generate() for attachment in self._attachments
        ]
        return post
