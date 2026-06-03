from parse import Plugin

BRAILLE_MAP = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵',
    '1': '⠂', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢', 
    '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔', '0': '⠴',
    ' ': '⠀', ',': '⠠', ';': '⠰', ':': '⠱', '.': '⠨', 
    '!': '⠮', '?': '⠹', '-': '⠤', '/': '⠌'
}

class BraillePlugin(Plugin):
    @classmethod
    def before_render_text(cls, s: str) -> str:
        return "".join(BRAILLE_MAP.get(c, c) for c in s.lower())

    @classmethod
    def after_render(cls, html: str) -> str:
        return f"<span class=\"braille\">{html}</span>"