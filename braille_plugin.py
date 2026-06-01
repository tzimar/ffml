from parse import Plugin
import math

class BraillePlugin(Plugin):
    @classmethod
    def after_render_text(cls, s: str) -> str:
        t = ""
        for i in range(0, math.ceil(len(s) / 6)):
            part = s[i*6 : i*6 + 6]
            n = 0
            for j, char in enumerate(part):
                if char == "d":
                    n += 1 << j
            t += chr(0x2800 + n)
        return t