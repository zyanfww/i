from manimlib import *


class TestMatchingStrings(Scene):
    def construct(self):
        e = Tex(R"\frac{x}{y}", isolate=["x", "y"])
        e["x"].set_color(RED)
        self.add(e)