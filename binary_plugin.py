from parse import Plugin

class BinaryPlugin(Plugin):
    @classmethod
    def after_render_text(cls, s: str) -> str:
        return " ".join(f"{ord(char):08b}" for char in s)