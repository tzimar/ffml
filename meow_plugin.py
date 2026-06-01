from parse import Plugin

class MeowPlugin(Plugin):
    def after_render_text(self, s: str) -> str:
        return " ".join("MEOW" for _ in s.split(" "))