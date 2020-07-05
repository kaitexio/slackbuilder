DEFAULT_TEXT_TYPE = "mrkdwn"


class BaseBlock:
    def generate(self):
        raise NotImplemented("Subclass missing generate implementation")


class TextBlock(BaseBlock):
    def __init__(self, text, _type=DEFAULT_TEXT_TYPE):
        self._text = text
        self._type = _type

    def __repr__(self):
        return f"TextBlock({self._text}, _type={self._type})"

    def generate(self):
        return {"type": "section", "text": {"type": self._type, "text": self._text}}
