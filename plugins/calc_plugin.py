from parse import Plugin

class CalcPlugin(Plugin):
    @classmethod
    def before_render_text(cls, s: str) -> str:
        return str(eval(s.replace("`", "")))